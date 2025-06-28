# 🧠 Multi-Agent Debate System (LangGraph-based)

This project simulates a structured debate between two AI agents — a **Scientist** and a **Philosopher** — over a user-defined topic, using LangGraph and a locally running LLM via Ollama (`bujji`, LLaMA 3.2).

The system alternates turns between the agents, maintains debate memory, and uses a judging node to determine a winner. All actions are logged, and a DAG diagram of the workflow is included.

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running
- LLaMA 3.2 pulled and named `bujji`:
  ```bash
  ollama pull llama3
  ollama run bujji
  ```

### 📦 Install Python Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Debate

```bash
python run.py
```

You'll be prompted to enter a topic. The debate runs for 8 rounds (4 per agent), then the judge declares a winner.

---

## 📂 Project Structure

```
debate_system/
├── agents.py          # Defines Scientist and Philosopher agents using bujji
├── state.py           # Shared DebateState dataclass
├── logger.py          # Logs actions to debate_log.txt
├── workflow.py        # LangGraph DAG with all nodes and transitions
run.py                 # CLI entrypoint
```

---

## 🧭 DAG and Node Structure

This LangGraph DAG contains the following nodes:

| Node Name     | Purpose                                                                 |
|---------------|-------------------------------------------------------------------------|
| `user_input`  | Accepts debate topic from user via CLI                                  |
| `agent_a`     | Scientist agent: evidence-based arguments                               |
| `agent_b`     | Philosopher agent: ethical and conceptual reasoning                     |
| `memory_update` | Maintains evolving summary of the debate                            |
| `judge`       | Analyzes the debate and declares a winner with justification            |

### 🔄 Flow

1. `user_input` → `agent_a`
2. Agents alternate (`agent_a` ↔ `agent_b`) for 8 rounds via `memory_update`
3. Final round routes to `judge`
4. `judge` outputs a full summary and verdict

### 📈 DAG Visualization

See:
- `dag_diagram.dot` (Graphviz format)
- `dag_mermaid.md` (for Markdown/GitHub rendering)

---

## 📜 Output Files

- `debate_log.txt`: CLI logs of all transitions and messages
- `debate_complete_log.json`: Structured log of entire debate
- `dag_diagram.dot`, `dag_mermaid.md`: Visual representation of the DAG
- `requirements.txt`: Python dependencies

---

## 🏁 Example CLI Output

```bash
Enter topic for debate: Should AI be regulated like medicine?

[Round 1] Scientist: Regulation is essential due to measurable risk factors...

[Round 2] Philosopher: Regulation might suppress the philosophical evolution of AI...

...

[Judge] Winner: Scientist
Reason: Presented empirically grounded, risk-focused arguments aligned with public safety.
```

---

## 🧠 Powered By

- [LangGraph](https://docs.langgraph.dev/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- LLaMA 3.2 (via local model named `bujji`)
