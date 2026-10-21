# Introduction to RAG - Simple Guide for Beginners

## What will you learn?
You will understand what RAG is, why it is useful, and how it works.

### Part 1: What is RAG?
RAG = Retrieval-Augmented Generation.
- Retrieval = Search and find. Like searching pen in bag.
- Augmented = Add extra help. Like adding masala to chai.
- Generation = AI writes answer.
Simple: Give AI a book before exam. AI reads book, then writes answer.

### Part 2: Why need RAG?
Problem: Normal AI knows old data only, sometimes gives wrong answer. This is called hallucination (means guessing wrong answer).
Solution: Give AI your own documents. AI searches them first. So answer is Correct and New.

### Part 3: How does RAG work? 3 Steps
Step 1: Retrieval (Searching) - User asks question. System searches in your files.
Step 2: Augmented (Adding Context) - System takes 3 best pages and gives to AI.
Step 3: Generation (Writing Answer) - AI reads question + pages and writes final answer.
Flow: Question -> Search Files -> Give Pages to AI -> AI Writes Correct Answer

### Part 4: Example - Kirana Store
You have kirana store. You wrote prices in notebook.
Without RAG: Ask AI price of sugar. AI says Maybe Rs 50. Wrong.
With RAG: AI reads notebook, finds 1kg sugar = Rs 60, says Rs 60 as per notebook. Correct!

### Part 5: Important Points
1. RAG = Search + Add + Generate
2. Why? Stop guessing, give fresh answers
3. How? Search documents, then give to AI
