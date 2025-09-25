import matplotlib.pyplot as plt

# Function to draw a stack
def draw_stack(elements, title):
    fig, ax = plt.subplots(figsize=(2, 4))
    ax.set_xlim(0, 2)
    ax.set_ylim(0, max(3, len(elements)))
    for i, e in enumerate(elements):
        ax.text(1, i + 0.5, e, ha='center', va='center', fontsize=10,
                bbox=dict(facecolor="skyblue", edgecolor="black"))
    ax.set_title(title, fontsize=10)
    ax.axis('off')
    plt.show()

# Function to draw a queue
def draw_queue(elements, title):
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.set_xlim(0, max(6, len(elements)))
    ax.set_ylim(0, 2)
    for i, e in enumerate(elements):
        ax.text(i + 0.5, 1, e, ha='center', va='center', fontsize=10,
                bbox=dict(facecolor="lightgreen", edgecolor="black"))
    ax.set_title(title, fontsize=10)
    ax.axis('off')
    plt.show()

# Helpers to show before/after diagrams
def stack_before_after(before, after, title_before, title_after):
    draw_stack(before, f"Before: {title_before}")
    draw_stack(after, f"After: {title_after}")

def queue_before_after(before, after, title_before, title_after):
    draw_queue(before, f"Before: {title_before}")
    draw_queue(after, f"After: {title_after}")

# --- Project 88 Stack Cases ---
stack_before_after(["Lecture1","Lecture2","Lecture3"], ["Lecture1","Lecture2"],
                   "UR pushes [Lecture1, Lecture2, Lecture3]",
                   "Undo one → Top = Lecture2")

stack_before_after(["Upload ID","Fill Address","Submit"], ["Upload ID"],
                   "Push [Upload ID, Fill Address, Submit]",
                   "Undo two → Upload ID remains")

stack_before_after(["A","B","C"], ["D"],
                   "Push [A, B, C]",
                   "Pop all, push D → Top = D")

# --- Project 88 Queue Cases ---
queue_before_after([f"P{i}" for i in range(1,11)], [f"P{i}" for i in range(8,11)],
                   "CHUK Queue [P1..P10]",
                   "After 7 served → P8 is front")

queue_before_after([f"B{i}" for i in range(1,7)], [f"B{i}" for i in range(2,7)],
                   "Nyabugogo Queue [B1..B6]",
                   "After B1 served → B2 is second served")
                   
