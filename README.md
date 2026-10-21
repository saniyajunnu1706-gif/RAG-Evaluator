from src.generator import generate_lesson
from src.evaluator import evaluate_lesson
import json
import os

MAX_RETRIES = 2

def agentic_loop(topic: str):
    rejection_log = []
    os.makedirs("output", exist_ok=True)
    for attempt in range(MAX_RETRIES + 1):
        feedback = rejection_log[-1]["fail_reasons"] if rejection_log else None
        lesson = generate_lesson(topic, feedback=feedback, attempt=attempt)
        result = evaluate_lesson(lesson)
        print(f"Attempt {attempt+1}: Passed={result['passed']}")
        if result["passed"]:
            open("output/final_lesson.md","w",encoding="utf-8").write(lesson)
            open("output/rejection_log.json","w").write(json.dumps(rejection_log,indent=2))
            return lesson
        else:
            rejection_log.append({
                "attempt": attempt+1,
                "failed_checks": result["failed_checks"],
                "fail_reasons": result["fail_reasons"],
                "what_to_fix_next": result["suggestions"]
            })
    return lesson

if __name__ == "__main__":
    agentic_loop("Introduction to RAG")
