import os
import requests

class LLMHandler:
    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"
        self.prompt_dir = os.path.join(os.path.dirname(__file__), "prompts")
        # Load all prompts
        self.prompts = {
            "planner": self._load_prompt("planner_prompt.txt"),
            "executor": self._load_prompt("executor_prompt.txt"),
            "verifier": self._load_prompt("verifier_prompt.txt")
        }

    def _load_prompt(self, filename):
        path = os.path.join(self.prompt_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def _call_llm(self, prompt: str):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        return response.json()["response"]

    # Generate step-by-step plan
    def generate_plan(self, question: str):
        prompt = self.prompts["planner"] + f"\nQuestion:\n{question}"
        text = self._call_llm(prompt)
        # Parse lines starting with - or numbered list
        steps = [line.strip("- ").strip() for line in text.split("\n") if line.strip()]
        return steps

    # Execute plan and get intermediate steps + final answer
    def execute_plan(self, question: str, plan: list):
        plan_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(plan)])
        prompt = self.prompts["executor"] + f"\nQuestion:\n{question}\nPlan:\n{plan_text}"
        text = self._call_llm(prompt)
        return text

    # Verify solution
    def verify_solution(self, question: str, plan: list, intermediate: str, final_answer: str):
        plan_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(plan)])
        prompt = self.prompts["verifier"] + f"""
Question: {question}
Plan: {plan_text}
Intermediate: {intermediate}
Final answer: {final_answer}
"""
        text = self._call_llm(prompt)
        return text

    # Default user-facing explanation
    def generate_explanation(self):
        return "The problem was solved using structured reasoning and validated logic."
