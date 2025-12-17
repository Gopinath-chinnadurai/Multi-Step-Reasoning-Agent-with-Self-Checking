from agent.planner import planner
from agent.executor import executor
from agent.verifier import verifier
from agent.llm_handler import LLMHandler

class AgentLoop:
    def __init__(self, max_retries=1):
        self.llm = LLMHandler()
        self.max_retries = max_retries

    def solve(self, question: str):
        """
        Solve a structured problem using planner, executor, and verifier.
        Returns a JSON object with answer, status, reasoning, and metadata.
        """
        retries = 0
        plan = []
        solution = {}
        verification = {}

        while retries <= self.max_retries:
            # 1️⃣ Generate plan
            plan = planner(question)

            # 2️⃣ Execute plan
            solution = executor(question, plan)

            # 3️⃣ Verify solution
            verification = verifier(solution)

            # Debug logging (optional)
            print(f"[Retry {retries}] Plan: {plan}")
            print(f"[Retry {retries}] Solution: {solution['final_answer']}")
            print(f"[Retry {retries}] Verification: {verification['passed']}")
            
            # ✅ If verification passed, return success JSON
            if verification["passed"]:
                return {
                    "answer": solution["final_answer"],
                    "status": "success",
                    "reasoning_visible_to_user": self.llm.generate_explanation(),
                    "metadata": {
                        "plan": plan,
                        "checks": verification.get("checks", []),
                        "intermediate": solution.get("intermediate", ""),
                        "retries": retries
                    }
                }

            retries += 1

        # ❌ Failed after retries
        return {
            "answer": "Failed to solve the problem",
            "status": "failed",
            "reasoning_visible_to_user": "The solution could not be verified.",
            "metadata": {
                "plan": plan,
                "checks": verification.get("checks", []),
                "intermediate": solution.get("intermediate", ""),
                "retries": retries
            }
        }

# Example usage in CLI or app.py
if __name__ == "__main__":
    agent = AgentLoop(max_retries=2)
    while True:
        q = input("Enter your question (or 'exit' to quit): ")
        if q.lower() == "exit":
            break
        result = agent.solve(q)
        print(result)
        print("="*60)
