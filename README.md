# Multi-Step Reasoning Agent with Self-Checking

This project implements a multi-step reasoning agent that solves structured math, logic, and constraint-based word problems. The agent produces:

- **A final answer**  
- **A short, user-facing explanation**  
- **Debug metadata** (plan, checks, retries) for internal evaluation

**Note:** The current implementation fully handles four main problem types:

- Arithmetic / logic problems (e.g., 8 + 7, 10 * 5, sum of 3 and 4)

- Number sequences (e.g., 2, 4, 8, 16, _)

- Time differences (e.g., Train leaves 14:30, arrives 18:05)

- Meeting durations / available slots (e.g., Meeting 46 minutes, slots 09:00–09:30, 11:00–12:00)

<img width="1031" height="875" alt="Multistepreasoning" src="https://github.com/user-attachments/assets/259fda21-c417-414e-bdc6-139856485b43" />

**Demo :** https://multi-step-reasoning-app.streamlit.app/

If needed, the executor.py logic can be extended to handle additional problem types such as letter sequences, odd-one-out, and directional/walking problems.

---

##  How to Run

### 1. Clone the repository

- git clone https://github.com/Gopinath-chinnadurai/Multi-Step-Reasoning-Agent-with-Self-Checking.git

- cd **Multistep-reasoning-agent**

### 2. Install dependencies

- pip install -r **requirements.txt**

### 3. Run the Streamlit app

- streamlit run **app.py**
  
### 4. Enter a math/logic/constraint question.Click Solve to see: answer, explanation, and debug info.

### 5. Run test cases

- python **tests/test_cases.py**

## Where Prompts Live

All prompts are in **agent/prompts/**:

**File Purpose :**

- planner_prompt.txt -Guides planner to generate a step-by-step plan

- executor_prompt.txt	-Guides executor to follow plan and show intermediate calculations

- verifier_prompt.txt	-Guides verifier to check consistency and validate constraints

**Keeping prompts separate allows easy experimentation without hard-coding in Python.**

## Assumptions
- Input is structured **math, logic, or constraint** problems.

- LLM API available locally at http://localhost:11434/api/generate.

- Only the final answer and explanation are shown to the user; detailed reasoning is in metadata.

- Verification ensures non-negative results and consistency.

## Prompt Design Documentation
**Why designed this way:**

- Separate prompts for **planner, executor, and verifier** for modularity.

- Each phase can be updated independently.

- Keeps code clean and reasoning structured.

**What didn’t work well initially:**

- Combining all steps in a single prompt produced inconsistent results.

- Hard-coding calculations in Python made it less flexible for different problem types.

**Improvements with more time:**

- Add dynamic prompts based on problem type.

- Include more advanced verification checks.

- Handle more complex, multi-step word problems.
  

## Example Runs

See **example_runs.txt** for sample questions including:

- Input question

- Answer

- Explanation

- Metadata **(plan, checks, retries)**

## Requirements

- Python 3.10+

- Streamlit

- Requests library

- Local LLM API (e.g., LLaMA 3)

## Author

**Gopinath Chinnadurai**

GitHub: https://github.com/Gopinath-chinnadurai

## License

MIT License — for educational and demonstration purposes.
