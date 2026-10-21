def evaluate_lesson(lesson: str):
    low = lesson.lower()
    failed, reasons, suggestions = [], [], []
    
    if not ("retrieval" in low and "generation" in low):
        failed.append("accurate & grounded")
        reasons.append("No RAG steps")
        suggestions.append("Add RAG steps")

    if len(lesson) < 400:
        failed.append("beginner-friendly language")
        reasons.append("Too short")
        suggestions.append("Add more simple explanation")

    if "kirana" not in low and "example" not in low:
        failed.append("teaches by example")
        reasons.append("No example")
        suggestions.append("Add kirana store example")

    if not ("what is" in low and "why" in low and "how" in low):
        failed.append("covers the key points")
        reasons.append("Missing what/why/how")
        suggestions.append("Add what/why/how")

    if "part 1" not in low and "step 1" not in low:
        failed.append("coherent teaching flow")
        reasons.append("No flow")
        suggestions.append("Add Part 1/2/3")

    return {
        "passed": len(failed)==0,
        "failed_checks": failed,
        "fail_reasons": reasons,
        "suggestions": suggestions
    }
