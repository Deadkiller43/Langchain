import json
from datetime import datetime
from langgraph.graph import StateGraph, END
from langchain_community.llms import Ollama
from .agents import ScientistAgent, PhilosopherAgent
from .state import DebateState
from .logger import setup_logger
from langgraph.graph import StateGraph
from pathlib import Path

logger = setup_logger()

class DebateSystem:
    def __init__(self):
        self.scientist = ScientistAgent()
        self.philosopher = PhilosopherAgent()
        self.judge_llm = Ollama(model="bujji", temperature=0.3)
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        graph = StateGraph(DebateState)
        graph.add_node("user_input", self.user_input_node)
        graph.add_node("agent_a", self.agent_a_node)
        graph.add_node("agent_b", self.agent_b_node)
        graph.add_node("memory_update", self.memory_node)
        graph.add_node("judge", self.judge_node)

        graph.set_entry_point("user_input")
        graph.add_edge("user_input", "agent_a")
        graph.add_conditional_edges("agent_a", self.route_after_argument, {
            "memory": "memory_update",
            "judge": "judge"
        })
        graph.add_conditional_edges("agent_b", self.route_after_argument, {
            "memory": "memory_update",
            "judge": "judge"
        })
        graph.add_conditional_edges("memory_update", self.route_after_memory, {
            "agent_a": "agent_a",
            "agent_b": "agent_b",
            "judge": "judge"
        })
        graph.add_edge("judge", END)

        return graph.compile()

    def user_input_node(self, state: DebateState) -> DebateState:
        if not state.topic:
            state.topic = input("Enter topic for debate: ")
        print(f"\nStarting debate on topic: {state.topic}\n")
        return state

    def agent_a_node(self, state: DebateState) -> DebateState:
        if state.current_speaker != "agent_a": return state
        argument = self.scientist.generate_argument(state.topic, state.memory_summary, state.current_round + 1)
        print(f"[Round {state.current_round + 1}] Scientist: {argument}\n")
        state.arguments.append({"round": state.current_round + 1, "speaker": "Scientist", "argument": argument, "timestamp": datetime.now().isoformat()})
        state.current_round += 1
        state.current_speaker = "agent_b"
        return state

    def agent_b_node(self, state: DebateState) -> DebateState:
        if state.current_speaker != "agent_b": return state
        argument = self.philosopher.generate_argument(state.topic, state.memory_summary, state.current_round + 1)
        print(f"[Round {state.current_round + 1}] Philosopher: {argument}\n")
        state.arguments.append({"round": state.current_round + 1, "speaker": "Philosopher", "argument": argument, "timestamp": datetime.now().isoformat()})
        state.current_round += 1
        state.current_speaker = "agent_a"
        return state

    def memory_node(self, state: DebateState) -> DebateState:
        recent_args = state.arguments[-2:]
        summary_prompt = f"""Summarize the following:
        {json.dumps(recent_args)}
        Previous Summary: {state.memory_summary}"""
        state.memory_summary = self.judge_llm.invoke(summary_prompt)
        return state

    def judge_node(self, state: DebateState) -> DebateState:
        all_args = "\n".join([f"Round {a['round']} - {a['speaker']}: {a['argument']}" for a in state.arguments])
        prompt = f"""Topic: {state.topic}\nTranscript:\n{all_args}\nSummary:\n{state.memory_summary}\nJudge and declare winner with justification. Limit your response to under 50 words"""
        state.judgment = self.judge_llm.invoke(prompt)
        state.winner = "Scientist" if "Scientist" in state.judgment else "Philosopher"
        state.debate_finished = True
        print("\n=== DEBATE JUDGMENT ===")
        print(state.judgment)
        return state

    def route_after_argument(self, state: DebateState) -> str:
        return "judge" if state.current_round >= 8 else "memory"

    def route_after_memory(self, state: DebateState) -> str:
        return "judge" if state.current_round >= 8 else state.current_speaker

    def run(self, topic=None):
        state = DebateState(topic=topic or "")
        final_state = self.graph.invoke(state)
        with open("debate_complete_log.json", "w") as f:
            json.dump(final_state, f, indent=2)
        return final_state
    

def export_dag_diagram():
    system = DebateSystem()
    mermaid = system.graph.get_graph().draw_mermaid()
    with open("dag_diagram.md", "w") as f:
        f.write("```mermaid\n" + mermaid + "\n```")

