from debate_system.workflow import DebateSystem, export_dag_diagram

def main():
    print("Multi-Agent Debate System")
    print("=" * 40)
    export_dag_diagram()
    system = DebateSystem()
    final_state = system.run()
    print("\nDebate Completed.\nWinner:", final_state["winner"])

if __name__ == "__main__":
    main()
