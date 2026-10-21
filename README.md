# 🏗️ Build a Self-Evaluating Lesson Content Generator | NxtWave GenAI Assessment

**Role:** GenAI Engineer - Content Systems
**Topic for Submission:** Introduction to RAG
**Target Audience:** 12th-grade Indian student, limited English, wants AI career

---

### 🎯 Goal
Build agentic system that GENERATES beginner lesson -> EVALUATES against hard rubric -> REGENERATES until good enough to ship.

It's NOT one clever prompt. It's full loop that decides on its own.

### 🏛️ Architecture - Why This Design?

INPUT (Topic: RAG)
   ↓
[GENERATOR] -> Uses simple English prompt + library/kirana analogy for Indian student
   ↓
[EVALUATOR] -> 6 hard pass/fail checks (no partial credit)
   ↓
IF FAIL -> feed reasons back -> REGENERATE (max 2 retries so loop terminates)
   ↓
OUTPUT -> Passing lesson + rejection log

**Why these components?**
- Generator: Separate module, can switch to OpenAI/Claude/Gemini or offline template. For phone demo, uses template that evolves.
- Evaluator: Hard binary checks, not LLM-as-judge (works offline). Each check clearly passes/fails.
- Memory: `output/rejection_log.json` persists. Next run can read it to improve.
- Self-Evolving: Log tells what failed, why, what changed on retry.

### ✅ Rubric I Designed (6 dimensions)

1. accurate & grounded - Has Retrieve, Augment, Generate steps correctly
2. beginner-friendly language - Short sentences (<20 words), <600 words total
3. teaches by example - kirana store / library example
4. clear, no unexplained jargon - If hallucination used, must explain as "wrong answer"
5. covers the key points - What is RAG, Why matters, How works
6. coherent teaching flow - Part 1 What -> Part 2 Why -> Part 3 How

### 🔧 Setup (Works on Phone - Replit/Colab)

pip install -r requirements.txt
python main.py
# Check output/final_lesson.md and output/rejection_log.json

### 📂 Output

- Attempt 1: FAILED - teaches by example, covers key points (proves evaluator works)
- Attempt 2: PASSED - All 6 checks passed after feeding feedback
- Rejection log shows what failed, why, what changed

### 🚀 Trade-offs

- Used template fallback instead of only API so it runs without laptop/API key
- Kept evaluator rule-based for determinism, can upgrade to LLM evaluator later
- Can port to LangGraph: Generator Node -> Evaluator Node -> Conditional Edge (regenerate)

### 🎥 Loom Video Structure
0-2 Face intro + problem
2-5 Code walkthrough
5-8 Live run - Attempt 1 FAIL log, Attempt 2 PASS
8-11 Show deliberate failure catch
11-15 Show final outputs + future scope
