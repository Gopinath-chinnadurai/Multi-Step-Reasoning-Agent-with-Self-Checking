import re
from collections import Counter

def executor(question: str, plan: list = None):
    """
    Execute the plan or solve the question directly.
    Returns final_answer, raw_value (numeric if applicable), and intermediate info.
    """
    question_lower = question.lower()

    times = re.findall(r'(\d{1,2}):(\d{2})', question)
    if len(times) == 2 and any(k in question_lower for k in ["train", "journey", "arrives", "leaves"]):
        sh, sm = map(int, times[0])
        eh, em = map(int, times[1])
        start = sh * 60 + sm
        end = eh * 60 + em
        diff = end - start
        if diff < 0:
            diff += 24 * 60
        intermediate = f"Start={start} min, End={end} min, Duration={diff} min"
        return {
            "final_answer": f"{diff//60} hours {diff%60} minutes",
            "raw_value": diff,
            "intermediate": intermediate
        }

    numbers = list(map(int, re.findall(r'\d+', question)))
    if numbers:
        total = None
        intermediate = ""
        if "twice" in question_lower:
            base = numbers[0]
            total = base + base * 2
            intermediate = f"Base={base}, Twice={base*2}, Total={total}"
        elif "half" in question_lower:
            base = numbers[0]
            total = base / 2
            intermediate = f"Base={base}, Half={total}"
        elif "sum" in question_lower or "+" in question_lower:
            total = sum(numbers)
            intermediate = f"Numbers={numbers}, Sum={total}"
        elif "difference" in question_lower or "-" in question_lower:
            total = numbers[0] - sum(numbers[1:])
            intermediate = f"Numbers={numbers}, Difference={total}"
        elif "product" in question_lower or "times" in question_lower:
            product = 1
            for n in numbers:
                product *= n
            total = product
            intermediate = f"Numbers={numbers}, Product={total}"
        if total is not None:
            return {
                "final_answer": str(total),
                "raw_value": total,
                "intermediate": intermediate
            }

    duration_match = re.search(r'(\d+)\s*minutes', question_lower)
    slots = re.findall(r'(\d{1,2}:\d{2})[–-](\d{1,2}:\d{2})', question)
    if duration_match and slots:
        duration = int(duration_match.group(1))
        valid = []
        for start, end in slots:
            sh, sm = map(int, start.split(":"))
            eh, em = map(int, end.split(":"))
            slot_duration = (eh*60 + em) - (sh*60 + sm)
            if slot_duration >= duration:
                valid.append(f"{start}–{end}")
        intermediate = f"Meeting duration={duration} min, Valid slots={valid}"
        return {
            "final_answer": ", ".join(valid) if valid else "No slots fit",
            "raw_value": len(valid),
            "intermediate": intermediate
        }

    if ',' in question:
        items = re.findall(r'\d+', question)
        if len(items) >= 2:
            nums = list(map(int, items))
        
            diff = nums[1] - nums[0]
            if all(nums[i+1] - nums[i] == diff for i in range(len(nums)-1)):
                next_num = nums[-1] + diff
                return {
                    "final_answer": str(next_num),
                    "raw_value": next_num,
                    "intermediate": f"Arithmetic sequence detected: diff={diff}, Next={next_num}"
                }
            
            ratio = nums[1] / nums[0]
            if all(nums[i+1] / nums[i] == ratio for i in range(len(nums)-1)):
                next_num = int(nums[-1] * ratio)
                return {
                    "final_answer": str(next_num),
                    "raw_value": next_num,
                    "intermediate": f"Geometric sequence detected: ratio={ratio}, Next={next_num}"
                }

        words = [w.strip().lower() for w in question.split(',')]
        if len(words) >= 3 and not any(w.isdigit() for w in words):
            counter = Counter(words)
            
            odd_one = min(counter, key=counter.get)
            return {
                "final_answer": odd_one,
                "raw_value": None,
                "intermediate": f"Odd one out detected among {words}: {odd_one}"
            }

    return {
        "final_answer": "Unable to solve this question",
        "raw_value": 0,
        "intermediate": "No valid calculation found"
    }
