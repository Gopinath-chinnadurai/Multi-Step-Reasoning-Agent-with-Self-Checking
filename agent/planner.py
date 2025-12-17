from agent.llm_handler import LLMHandler

# Create a single LLM handler instance
llm = LLMHandler()

def planner(question: str):
    """
    Generates a step-by-step plan for solving the question.
    
    Returns:
        list[str]: A list of steps.
    """
    try:
        steps = llm.generate_plan(question)
        return steps
    except Exception as e:
        print(f"[Planner Error] {e}")
        return []
