# ------------------------
# Project 88: Stacks and Queues
# ------------------------

# --- Stack operations (LIFO: Last In, First Out) ---
print("=== STACK QUESTIONS ===")

# Q1: UR pushes ["Lecture1", "Lecture2", "Lecture3"], undo one
stack = ["Lecture1", "Lecture2", "Lecture3"]
print("\nQ1 Before Undo:", stack)
stack.pop()  # undo one
print("Q1 After Undo:", stack)
print("Answer Q1 -> Top element is:", stack[-1])  # should be Lecture2

# Q2: Irembo pushes ["Upload ID", "Fill Address", "Submit"], undo two
stack = ["Upload ID", "Fill Address", "Submit"]
print("\nQ2 Before Undo:", stack)
stack.pop()  # undo 1
stack.pop()  # undo 2
print("Q2 After Undo:", stack)
print("Answer Q2 -> Remaining element is:", stack[-1])  # should be Upload ID

# Q3: Push ["A", "B", "C"], pop all, then push "D"
stack = ["A", "B", "C"]
print("\nQ3 Before Pop All:", stack)
stack.clear()  # pop all
stack.append("D")  # push D
print("Q3 After Operations:", stack)
print("Answer Q3 -> Top element is:", stack[-1])  # should be D

# Q4: Reflection
print("\nQ4 -> Stack is used in undo/redo because the last action is undone first (LIFO).")

# --- Queue operations (FIFO: First In, First Out) ---
print("\n=== QUEUE QUESTIONS ===")

from collections import deque

# Q5: CHUK, 10 patients queue, after 7 served, who is front?
queue = deque([f"P{i}" for i in range(1, 11)])
print("\nQ5 Before Serving:", list(queue))
for _ in range(7):
    queue.popleft()  # serve 7 patients
print("Q5 After Serving:", list(queue))
print("Answer Q5 -> Front patient is:", queue[0])  # should be P8

# Q6: Nyabugogo, 6 buses queue, who is served second?
queue = deque([f"B{i}" for i in range(1, 7)])
print("\nQ6 Before Serving:", list(queue))
queue.popleft()  # first served = B1
print("Q6 After 1 served:", list(queue))
print("Answer Q6 -> Second served is:", queue[0])  # should be B2

# Q7: Concert tickets line
print("\nQ7 -> Queue is correct for concert tickets (FIFO ensures fairness).")

# Q8: Reflection
print("Q8 -> FIFO ensures fairness because the first arrival is the first served.")