from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

class DebateAgent:
    def __init__(self, name: str, persona: str, model_name: str = "bujji"):
        self.name = name
        self.persona = persona
        self.llm = Ollama(model=model_name, temperature=0.7)
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.persona),
            ("human", "{input}")
        ])

    def generate_argument(self, topic: str, memory: str, round_num: int) -> str:
        context = f"""
        Debate Topic: {topic}
        Round: {round_num}/8
        Previous Arguments Summary: {memory}
        Provide a strong, logical argument for your position.
        Avoid repeating previous points. Build upon or counter previous arguments.
        Limit your response to under 10 words
        """
        chain = self.prompt_template | self.llm
        return chain.invoke({"input": context})

class ScientistAgent(DebateAgent):
    def __init__(self):
        persona = "You are a scientist. Your approach is evidence-based..."
        super().__init__("Scientist", persona)

class PhilosopherAgent(DebateAgent):
    def __init__(self):
        persona = "You are a philosopher. Your approach is ethical and conceptual..."
        super().__init__("Philosopher", persona)
