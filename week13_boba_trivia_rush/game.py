# ═══════════════════════════════════════════════════════════
#  🧋  BOBA TRIVIA RUSH  — Student Version
#  Week 13  |  Level 2 Python  |  Fill in the Gaps!
# ═══════════════════════════════════════════════════════════
#
#  HOW TO PLAY:
#    • A boba drink name appears in the center of the screen
#    • Four price buttons appear — only ONE is correct
#    • Click the right price before the 8-second timer runs out!
#    • Correct answer → +10 points, next question
#    • Wrong answer or timeout → lose a life ❤️
#    • 8 questions total — how high can you score?
#
#  YOUR JOB:
#    There are 6 gaps marked with  🔧 FIX ME
#    Read the step-by-step instructions above each gap carefully,
#    then write your code where it says  ✏️ YOUR CODE HERE
#
#  HINT FILE:  Open hints.txt if you get stuck!
#  Work through the gaps in order: 1 → 2 → 3 → 4 → 5 → 6
# ═══════════════════════════════════════════════════════════

import tkinter as tk
import random

# ── NEW THIS WEEK: DICTIONARIES ─────────────────────────────
#
#  A dictionary maps a KEY to a VALUE, like a lookup table.
#  Syntax:   my_dict = { key: value, key: value, ... }
#  Lookup:   my_dict["Milk Tea 🧋"]   →   "$3.50"
#
#  DRINK_DICT maps each drink name (key) to its price (value).

DRINK_DICT = {
    "Milk Tea 🧋":        "$3.50",
    "Taro Tea 🫧":        "$4.00",
    "Matcha Tea 🍵":      "$4.50",
    "Strawberry Tea 🍓":  "$4.25",
    "Mango Tea 🥭":       "$3.75",
    "Brown Sugar 🧊":     "$5.00",
    "Honeydew Tea 🍈":    "$4.10",
    "Lychee Tea 🍑":      "$4.75",
}

# These pull all keys/values out of the dictionary into plain lists:
ALL_PRICES = list(DRINK_DICT.values())   # ["$3.50", "$4.00", "$4.50", ...]
ALL_DRINKS = list(DRINK_DICT.keys())     # ["Milk Tea 🧋", "Taro Tea 🫧", ...]

TOTAL_QUESTIONS = 8    # how many questions per game
TIMER_SECONDS   = 8    # seconds allowed per question
MAX_LIVES       = 3    # lives the player starts with

# ── GAME STATE VARIABLES ────────────────────────────────────
score          = 0
lives          = MAX_LIVES
question_num   = 0
current_drink  = ""
correct_price  = ""
timer_id       = None        # ID returned by window.after (lets us cancel it)
time_left      = TIMER_SECONDS
question_order = []          # shuffled list of all 8 drinks for this game


# ═══════════════════════════════════════════════════════════
#  WINDOW & WIDGETS  (already done for you — do not change)
# ═══════════════════════════════════════════════════════════

window = tk.Tk()
window.title("Boba Trivia Rush! 🧋⚡")
window.geometry("500x640")
window.configure(bg="#FFF0F5")

# ── top stats bar ──
hud_frame = tk.Frame(window, bg="#FFD6E7", pady=8)
hud_frame.pack(fill="x")

score_label = tk.Label(
    hud_frame, text="Score: 0",
    font=("Arial", 13, "bold"), bg="#FFD6E7", fg="#D63384",
)
score_label.pack(side="left", padx=20)

lives_label = tk.Label(
    hud_frame, text="❤️ ❤️ ❤️",
    font=("Arial", 13), bg="#FFD6E7", fg="#D63384",
)
lives_label.pack(side="right", padx=20)

question_label = tk.Label(
    hud_frame, text="Q 1 / 8",
    font=("Arial", 12), bg="#FFD6E7", fg="#555555",
)
question_label.pack()

# ── timer ──
timer_label = tk.Label(
    window, text="⏱  8",
    font=("Arial", 16, "bold"), bg="#FFF0F5", fg="#FF6B6B",
)
timer_label.pack(pady=(12, 0))

timer_bar_canvas = tk.Canvas(
    window, width=440, height=14, bg="#E0E0E0", bd=0, highlightthickness=0,
)
timer_bar_canvas.pack(pady=(4, 10))
timer_bar = timer_bar_canvas.create_rectangle(0, 0, 440, 14, fill="#FF6B6B", outline="")

# ── drink display ──
drink_frame = tk.Frame(window, bg="#FFB6C1", bd=2, relief="groove")
drink_frame.pack(padx=30, pady=10, fill="x")

drink_label = tk.Label(
    drink_frame, text="?",
    font=("Arial", 26, "bold"), bg="#FFB6C1", fg="#333333", pady=20,
)
drink_label.pack()

prompt_label = tk.Label(
    window, text="What is the price of this drink?",
    font=("Arial", 12, "italic"), bg="#FFF0F5", fg="#888888",
)
prompt_label.pack()

# ── four answer buttons in a 2×2 grid ──
btn_frame = tk.Frame(window, bg="#FFF0F5")
btn_frame.pack(pady=15)

answer_buttons = []
for r in range(2):
    for c in range(2):
        b = tk.Button(
            btn_frame, text="",
            font=("Arial", 14, "bold"),
            width=10, height=2,
            bg="#C8E6FA", fg="#333333",
        )
        b.grid(row=r, column=c, padx=8, pady=8)
        answer_buttons.append(b)

# ── feedback and play-again button ──
feedback_label = tk.Label(
    window, text="",
    font=("Arial", 13, "bold"), bg="#FFF0F5", fg="#28A745",
)
feedback_label.pack(pady=6)

restart_btn = tk.Button(
    window, text="🔄  Play Again",
    font=("Arial", 12), bg="#FFB6C1",
    command=lambda: start_game(),
)
restart_btn.pack(pady=5)
restart_btn.pack_forget()   # hidden until the game ends


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 1  —  build_wrong_answers(correct_price)
# ═══════════════════════════════════════════════════════════

def build_wrong_answers(correct_price):
    """
    Return a list of 3 WRONG prices to use as fake answer choices.

    WHAT YOU HAVE:
        correct_price  →  a string like "$3.50"
        ALL_PRICES     →  a list of every price in DRINK_DICT

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Create an empty list to collect wrong prices:
                       wrong_pool = []

        Step 2  →  Loop through ALL_PRICES and add every price
                   that is NOT the correct one:

                       for price in ALL_PRICES:
                           if price != correct_price:
                               wrong_pool.append(price)

        Step 3  →  Randomly pick exactly 3 items from wrong_pool.
                   Use random.sample — it picks UNIQUE items, no repeats:
                       wrong_three = random.sample(wrong_pool, 3)

        Step 4  →  Return wrong_three.

    ──────────────────────────────────────────────────────────
    💡 NEW: random.sample(some_list, n)
        Picks n UNIQUE items from some_list at random.
        random.sample(["a","b","c","d"], 2)  might give  ["c","a"]
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 2  —  load_question()
# ═══════════════════════════════════════════════════════════

def load_question():
    """
    Set up one new question: display the current drink,
    build 4 shuffled answer buttons, and start the timer.

    WHAT YOU HAVE:
        current_drink  →  the drink name shown to the player (global)
        correct_price  →  the right answer for this question (global)
        question_num   →  which question we're on, e.g. 3 (global)
        question_order →  a shuffled list of all 8 drink names (global)
                          question_order[0] is question 1's drink,
                          question_order[1] is question 2's drink, etc.
        answer_buttons →  a list of 4 Button widgets
        DRINK_DICT     →  the dictionary: drink name → price
        build_wrong_answers()  →  your Gap 1 function!
        start_timer()          →  already written, starts the countdown

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Declare globals at the very top of the function:
                       global current_drink, correct_price

        Step 2  →  Pick the drink for this question.
                   question_num starts at 1, but list indexes start at 0,
                   so subtract 1 to get the right slot:
                       current_drink = question_order[question_num - 1]

        Step 3  →  Look up the correct price in the dictionary:
                       correct_price = DRINK_DICT[current_drink]
                   (This is how you read a value from a dictionary!)

        Step 4  →  Show the drink name on the drink_label:
                       drink_label.config(text=current_drink)

        Step 5  →  Build the 4 answers (1 correct + 3 wrong), shuffle them:
                       answers = [correct_price] + build_wrong_answers(correct_price)
                       random.shuffle(answers)

        Step 6  →  Assign each answer to one of the 4 buttons.
                   Loop with range(4):
                       for i in range(4):
                           price = answers[i]
                           answer_buttons[i].config(
                               text=price,
                               bg="#C8E6FA",
                               state=tk.NORMAL,
                               command=lambda p=price: answer_clicked(p)
                           )

        Step 7  →  Clear the feedback label and kick off the timer:
                       feedback_label.config(text="")
                       start_timer()
    ──────────────────────────────────────────────────────────
    """

    global current_drink, correct_price

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  TIMER HELPERS  (already done for you — read and understand!)
# ═══════════════════════════════════════════════════════════

def start_timer():
    """Reset the countdown to TIMER_SECONDS and begin ticking."""
    global time_left, timer_id
    time_left = TIMER_SECONDS
    if timer_id is not None:
        window.after_cancel(timer_id)   # cancel any leftover timer first
    tick()

def stop_timer():
    """Cancel the running timer so it stops counting down."""
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 3  —  tick()
# ═══════════════════════════════════════════════════════════

def tick():
    """
    Count down one second.  Called once per second by window.after().

    Each call: subtract 1, update the label & bar, then either
    call time_up() (if out of time) or schedule itself again in 1 second.

    WHAT YOU HAVE:
        time_left          →  how many seconds remain (global integer)
        timer_id           →  stores the ID of the scheduled call (global)
        timer_label        →  the ⏱ label widget
        timer_bar          →  the coloured rectangle drawn on the canvas
        timer_bar_canvas   →  the canvas that holds timer_bar
        TIMER_SECONDS      →  the starting time (8)
        time_up()          →  already written — call it when time hits 0

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Declare globals at the very top:
                       global time_left, timer_id

        Step 2  →  Subtract 1 from time_left:
                       time_left = time_left - 1

        Step 3  →  Update the timer label text:
                       timer_label.config(text=f"⏱  {time_left}")

        Step 4  →  Shrink the timer bar to show time remaining.
                   Calculate the fraction of time left:
                       ratio     = time_left / TIMER_SECONDS
                       new_width = int(440 * ratio)
                   Then resize the rectangle on the canvas:
                       timer_bar_canvas.coords(timer_bar, 0, 0, new_width, 14)

        Step 5  →  Check if time has run out:
                       if time_left <= 0:
                           time_up()
                       else:
                           # Schedule tick() to run again in 1000 ms (1 second)
                           timer_id = window.after(1000, tick)

    ──────────────────────────────────────────────────────────
    💡 WHY window.after(1000, tick)?
        It tells tkinter: "In 1000 milliseconds, call tick() again."
        Each call schedules the next one — that's how the countdown loops!
    ──────────────────────────────────────────────────────────
    """

    global time_left, timer_id

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  TIME UP HANDLER  (already done for you — read it!)
# ═══════════════════════════════════════════════════════════

def time_up():
    """Called automatically when the timer reaches 0."""
    for btn in answer_buttons:
        btn.config(state=tk.DISABLED)
    feedback_label.config(
        text=f"⏰ Time's up!  The answer was {correct_price}",
        fg="#FF6B6B",
    )
    window.after(1500, next_question)


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 4  —  answer_clicked(chosen_price)
# ═══════════════════════════════════════════════════════════

def answer_clicked(chosen_price):
    """
    Called when the player clicks one of the four answer buttons.
    Stop the timer, judge the answer, update score or lives,
    then schedule the next question.

    WHAT YOU HAVE:
        chosen_price   →  the price text on the button that was clicked
        correct_price  →  the right answer for this question (global)
        score          →  the player's running score (global)
        lives          →  the player's remaining lives (global)
        answer_buttons →  list of all 4 Button widgets
        stop_timer()   →  already written — call it first!
        update_display()→  your Gap 5 function — call it after scoring
        next_question() →  already written — schedule it after 1.5 s

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Declare globals at the very top:
                       global score, lives

        Step 2  →  Stop the timer immediately:
                       stop_timer()

        Step 3  →  Disable ALL answer buttons so the player cannot
                   click a second time while the feedback is showing:
                       for btn in answer_buttons:
                           btn.config(state=tk.DISABLED)

        Step 4  →  Check whether the player chose correctly:
                       if chosen_price == correct_price:
                           score = score + 10
                           feedback_label.config(
                               text="✅ Correct! +10 points", fg="#28A745"
                           )
                       else:
                           lives = lives - 1
                           feedback_label.config(
                               text=f"❌ Wrong!  It was {correct_price}",
                               fg="#DC3545"
                           )

        Step 5  →  Refresh the HUD by calling update_display().

        Step 6  →  Schedule next_question() after 1500 milliseconds:
                       window.after(1500, next_question)
    ──────────────────────────────────────────────────────────
    """

    global score, lives

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 5  —  update_display()
# ═══════════════════════════════════════════════════════════

def update_display():
    """
    Refresh the score, lives hearts, and question counter labels.

    WHAT YOU HAVE:
        score           →  integer, e.g. 30
        lives           →  integer, e.g. 2
        question_num    →  integer, e.g. 4  (which question we're on)
        TOTAL_QUESTIONS →  integer, 8

        score_label     →  shows "Score: 30"
        lives_label     →  shows hearts  "❤️ ❤️ "
        question_label  →  shows "Q 4 / 8"

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Update the score label:
                       score_label.config(text=f"Score: {score}")

        Step 2  →  Build a hearts string and update lives_label.
                   "❤️ " * lives  repeats the heart emoji 'lives' times:
                       hearts = "❤️ " * lives
                       lives_label.config(text=hearts)

        Step 3  →  Update the question counter label:
                       question_label.config(
                           text=f"Q {question_num} / {TOTAL_QUESTIONS}"
                       )
    ──────────────────────────────────────────────────────────
    💡 NEW: the  *  operator works on strings too!
        "Ha" * 3   →   "HaHaHa"
        "❤️ " * 2  →   "❤️ ❤️ "
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 6  —  check_game_over()
# ═══════════════════════════════════════════════════════════

def check_game_over():
    """
    Decide whether the game should end or continue.

    The game ends when EITHER of these is true:
        • lives == 0                           (no lives left!)
        • question_num > TOTAL_QUESTIONS       (all questions answered!)

    If the game IS over  → call show_final_screen()
    If the game is NOT over → call load_question()

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Write an if/else using the 'or' keyword:
                       if lives == 0 or question_num > TOTAL_QUESTIONS:
                           show_final_screen()
                       else:
                           load_question()

        That's it!  Just those 4 lines (if, call, else, call).

    ──────────────────────────────────────────────────────────
    💡 NEW: the  or  keyword
        "A or B"  is True when at least ONE of A or B is True.
        lives == 0 or question_num > TOTAL_QUESTIONS
        → True if lives hit 0 OR if we've passed question 8.
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  GAME FLOW  (already done for you — read and understand!)
# ═══════════════════════════════════════════════════════════

def next_question():
    """Advance the question counter and check whether the game continues."""
    global question_num
    question_num += 1
    update_display()       # calls YOUR Gap 5 function!
    check_game_over()      # calls YOUR Gap 6 function!


def show_final_screen():
    """Display the end-of-game summary screen."""
    stop_timer()
    drink_label.config(text="Game Over! 🧋")
    prompt_label.config(text="")
    timer_label.config(text="")
    timer_bar_canvas.coords(timer_bar, 0, 0, 0, 14)

    for btn in answer_buttons:
        btn.config(text="", state=tk.DISABLED, bg="#FFF0F5")

    if lives == 0:
        result_text = "💔 You ran out of lives!"
    else:
        result_text = f"🎉 You answered all {TOTAL_QUESTIONS} questions!"

    feedback_label.config(
        text=f"{result_text}\nFinal Score: {score} / {TOTAL_QUESTIONS * 10}",
        fg="#D63384",
        font=("Arial", 14, "bold"),
    )
    restart_btn.pack(pady=10)


# ═══════════════════════════════════════════════════════════
#  GAME SETUP  (already done for you — do not change)
# ═══════════════════════════════════════════════════════════

def start_game():
    """Reset everything and begin a fresh game."""
    global score, lives, question_num, timer_id, question_order

    score        = 0
    lives        = MAX_LIVES
    question_num = 1
    timer_id     = None

    # Shuffle the drink order so every game is different
    question_order = ALL_DRINKS.copy()
    random.shuffle(question_order)

    # Reset UI
    feedback_label.config(text="", font=("Arial", 13, "bold"))
    prompt_label.config(text="What is the price of this drink?")
    timer_label.config(text=f"⏱  {TIMER_SECONDS}")
    timer_bar_canvas.coords(timer_bar, 0, 0, 440, 14)
    restart_btn.pack_forget()

    for btn in answer_buttons:
        btn.config(bg="#C8E6FA", state=tk.NORMAL, text="")

    update_display()   # calls YOUR Gap 5 function!
    load_question()    # calls YOUR Gap 2 function!


# ── START THE GAME ──────────────────────────────────────────
start_game()
window.mainloop()
