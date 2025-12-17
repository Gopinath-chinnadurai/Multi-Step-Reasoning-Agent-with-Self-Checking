from agent.agent_loop import solve_question

EASY_QUESTIONS = [
    "8+7",
    "10+20-5",
    "If a train leaves at 14:30 and arrives at 18:05, how long is the journey?",
    "5 * 6",
    "100 - 45"
]

TRICKY_QUESTIONS = [
    "Alice has 3 red apples and twice as many green apples. How many apples total?",
    "A meeting needs 60 minutes. Free slots: 09:00–09:30, 09:45–10:30, 11:00–12:00.",
    "Train leaves at 23:50 and arrives at 00:20. How long is the journey?",
    "10 + 20 - 33 * 2"
]

def run_tests():
    print("=== EASY TESTS ===")
    for q in EASY_QUESTIONS:
        result = solve_question(q)
        print("\nQuestion:", q)
        print("Final JSON:", result)
        print("Verifier passed:", result["status"] == "success")
        print("Retries:", result["metadata"]["retries"])

    print("\n=== TRICKY TESTS ===")
    for q in TRICKY_QUESTIONS:
        result = solve_question(q)
        print("\nQuestion:", q)
        print("Final JSON:", result)
        print("Verifier passed:", result["status"] == "success")
        print("Retries:", result["metadata"]["retries"])

if __name__ == "__main__":
    run_tests()
