# ═══════════════════════════════════════════════════════════
#  🧋  BOBA TRIVIA RUSH  — TEACHER SOLUTION
#  Week 13  |  All 6 gaps are filled in.
#  ⚠️  Do NOT share with students before the activity!
# ═══════════════════════════════════════════════════════════

import tkinter as tk
import random

# ── DRINK DATA ──────────────────────────────────────────────
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

ALL_PRICES = list(DRINK_DICT.values())
ALL_DRINKS = list(DRINK_DICT.keys())

TOTAL_QUESTIONS = 8
TIMER_SECONDS   = 8
MAX_LIVES       = 3

# ── GAME STATE ──────────────────────────────────────────────
score          = 0
lives          = MAX_LIVES
question_num   = 0
current_drink  = ""
correct_price  = ""
timer_id       = None
time_left      = TIMER_SECONDS
question_order: list[str] = []

# ── WINDOW & WIDGETS ────────────────────────────────────────
window = tk.Tk()
window.title("Boba Trivia Rush! 🧋⚡")
window.geometry("500x640")
window.configure(bg="#FFF0F5")

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

feedback_label = tk.Label(
    window, text="",
    font=("Arial", 13, "bold"), bg="#FFF0F5", fg="#28A745",
)
feedback_label.pack(pady=6)

restart_btn = tk.Button(
    window, text="🔄  Play Again",
    font=("Arial", 12), bg="#FFB6C1",
    command=start_game,
)
restart_btn.pack(pady=5)
restart_btn.pack_forget()


# ═══════════════════════════════════════════════════════════
#  GAP 1 SOLUTION  —  build_wrong_answers(correct_price)
# ═══════════════════════════════════════════════════════════

def build_wrong_answers(correct_price):
    """
    Return a list of 3 wrong prices.

    SOLUTION EXPLANATION:
        We loop through ALL_PRICES and keep only those that differ
        from the correct answer — this is our "wrong_pool".
        random.sample then picks 3 unique items from that pool.
        Because all 8 drinks have different prices, wrong_pool
        always has exactly 7 items, so sampling 3 is safe.
    """
    wrong_pool = []                            # Step 1: empty list
    for price in ALL_PRICES:                  # Step 2: loop all prices
        if price != correct_price:            #         skip the right one
            wrong_pool.append(price)          #         keep the wrong ones
    wrong_three = random.sample(wrong_pool, 3) # Step 3: pick 3 at random
    return wrong_three                         # Step 4: return them


# ═══════════════════════════════════════════════════════════
#  GAP 2 SOLUTION  —  load_question()
# ═══════════════════════════════════════════════════════════

def load_question():
    """
    Display the current question and set up the answer buttons.

    SOLUTION EXPLANATION:
        question_order is a pre-shuffled list of all 8 drink names.
        We index into it with (question_num - 1) because list indexes
        start at 0 but question_num starts at 1.

        DRINK_DICT[current_drink] is the dictionary lookup — it gives
        us the price for whichever drink is being asked about.

        The lambda p=price trick "captures" the current price value
        into the button's command so all 4 buttons remember their
        own price even after the loop finishes.
    """
    global current_drink, correct_price

    current_drink = question_order[question_num - 1]     # Step 2: pick drink
    correct_price = DRINK_DICT[current_drink]            # Step 3: look up price

    drink_label.config(text=current_drink)               # Step 4: show drink

    answers = [correct_price] + build_wrong_answers(correct_price)  # Step 5a
    random.shuffle(answers)                                          # Step 5b

    for i in range(4):                                   # Step 6: wire buttons
        price = answers[i]
        answer_buttons[i].config(
            text=price,
            bg="#C8E6FA",
            state=tk.NORMAL,
            command=lambda p=price: answer_clicked(p),
        )

    feedback_label.config(text="")                       # Step 7: clear feedback
    start_timer()                                        #         start clock


# ═══════════════════════════════════════════════════════════
#  TIMER HELPERS
# ═══════════════════════════════════════════════════════════

def start_timer():
    global time_left
    time_left = TIMER_SECONDS
    if timer_id is not None:
        window.after_cancel(timer_id)
    tick()

def stop_timer():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None


# ═══════════════════════════════════════════════════════════
#  GAP 3 SOLUTION  —  tick()
# ═══════════════════════════════════════════════════════════

def tick():
    """
    Count down one second and reschedule itself.

    SOLUTION EXPLANATION:
        Each call subtracts 1 from time_left, updates the label
        and the bar, then either calls time_up() or schedules
        itself to run again in 1000 ms (1 second).

        The bar width is calculated as a fraction:
            ratio = time_left / TIMER_SECONDS   (e.g. 6/8 = 0.75)
            new_width = int(440 * 0.75) = 330 pixels
        timer_bar_canvas.coords() moves the right edge of the
        rectangle to that new width, making it appear to shrink.

        We store the return value of window.after() in timer_id
        so stop_timer() can cancel the next scheduled tick.
    """
    global time_left, timer_id

    time_left = time_left - 1                                # Step 2: tick down
    timer_label.config(text=f"⏱  {time_left}")              # Step 3: update label

    ratio     = time_left / TIMER_SECONDS                    # Step 4: shrink bar
    new_width = int(440 * ratio)
    timer_bar_canvas.coords(timer_bar, 0, 0, new_width, 14)

    if time_left <= 0:                                       # Step 5: check done
        time_up()
    else:
        timer_id = window.after(1000, tick)                  #  schedule next tick


# ═══════════════════════════════════════════════════════════
#  TIME UP HANDLER
# ═══════════════════════════════════════════════════════════

def time_up():
    for btn in answer_buttons:
        btn.config(state=tk.DISABLED)
    feedback_label.config(
        text=f"⏰ Time's up!  The answer was {correct_price}",
        fg="#FF6B6B",
    )
    window.after(1500, next_question)


# ═══════════════════════════════════════════════════════════
#  GAP 4 SOLUTION  —  answer_clicked(chosen_price)
# ═══════════════════════════════════════════════════════════

def answer_clicked(chosen_price):
    """
    Handle a button click: stop timer, judge answer, schedule next Q.

    SOLUTION EXPLANATION:
        stop_timer() must come first — if we judge the answer before
        cancelling the timer, tick() might fire mid-judgment and call
        time_up() on top of the correct-answer branch.

        Disabling all buttons prevents a double-click while feedback
        is on screen (the buttons are re-enabled by load_question()).

        window.after(1500, next_question) gives the student 1.5 seconds
        to read the feedback before the question changes.
    """
    global score, lives

    stop_timer()                                             # Step 2: stop clock

    for btn in answer_buttons:                               # Step 3: disable all
        btn.config(state=tk.DISABLED)

    if chosen_price == correct_price:                        # Step 4: judge answer
        score = score + 10
        feedback_label.config(text="✅ Correct! +10 points", fg="#28A745")
    else:
        lives = lives - 1
        feedback_label.config(
            text=f"❌ Wrong!  It was {correct_price}", fg="#DC3545"
        )

    update_display()                                         # Step 5: refresh HUD
    window.after(1500, next_question)                        # Step 6: next Q


# ═══════════════════════════════════════════════════════════
#  GAP 5 SOLUTION  —  update_display()
# ═══════════════════════════════════════════════════════════

def update_display():
    """
    Refresh all three HUD labels.

    SOLUTION EXPLANATION:
        "❤️ " * lives repeats the heart string 'lives' times.
        When lives = 3  →  "❤️ ❤️ ❤️ "
        When lives = 1  →  "❤️ "
        When lives = 0  →  ""   (empty string — no hearts shown)

        This is a neat trick: string * integer in Python repeats
        the string, just like list * integer repeats a list.
    """
    score_label.config(text=f"Score: {score}")             # Step 1
    hearts = "❤️ " * lives                                  # Step 2
    lives_label.config(text=hearts)
    question_label.config(                                  # Step 3
        text=f"Q {question_num} / {TOTAL_QUESTIONS}"
    )


# ═══════════════════════════════════════════════════════════
#  GAP 6 SOLUTION  —  check_game_over()
# ═══════════════════════════════════════════════════════════

def check_game_over():
    """
    End the game or load the next question.

    SOLUTION EXPLANATION:
        The 'or' operator means "at least one must be True".
        Either condition ending the game satisfies the check.

        It is critical to use if/else here — NOT two separate ifs.
        If we used two ifs, show_final_screen() and load_question()
        could both run in the same call, breaking the game state.
    """
    if lives == 0 or question_num > TOTAL_QUESTIONS:
        show_final_screen()
    else:
        load_question()


# ═══════════════════════════════════════════════════════════
#  GAME FLOW
# ═══════════════════════════════════════════════════════════

def next_question():
    global question_num
    question_num += 1
    update_display()
    check_game_over()


def show_final_screen():
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
#  GAME SETUP
# ═══════════════════════════════════════════════════════════

def start_game():
    global score, lives, question_num, timer_id, question_order

    score        = 0
    lives        = MAX_LIVES
    question_num = 1
    timer_id     = None

    question_order = ALL_DRINKS.copy()
    random.shuffle(question_order)

    feedback_label.config(text="", font=("Arial", 13, "bold"))
    prompt_label.config(text="What is the price of this drink?")
    timer_label.config(text=f"⏱  {TIMER_SECONDS}")
    timer_bar_canvas.coords(timer_bar, 0, 0, 440, 14)
    restart_btn.pack_forget()

    for btn in answer_buttons:
        btn.config(bg="#C8E6FA", state=tk.NORMAL, text="")

    update_display()
    load_question()


# ── START ────────────────────────────────────────────────────
start_game()
window.mainloop()
