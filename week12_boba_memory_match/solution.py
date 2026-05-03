# ═══════════════════════════════════════════════════════════
#  🧋  BOBA MEMORY MATCH  —  TEACHER SOLUTION
#  All 4 gaps are filled in.  Do not share with students!
# ═══════════════════════════════════════════════════════════

import tkinter as tk
import random

# ── DRINK DATA ──────────────────────────────────────────────
DRINK_PAIRS = [
    ("Milk Tea 🧋",       "$3.50"),
    ("Taro Tea 🫧",       "$4.00"),
    ("Matcha Tea 🍵",     "$4.50"),
    ("Strawberry Tea 🍓", "$4.25"),
    ("Mango Tea 🥭",      "$3.75"),
    ("Brown Sugar 🧊",    "$5.00"),
]

# ── GAME STATE VARIABLES ────────────────────────────────────
cards       = []
flipped     = []
matched     = 0
attempts    = 0
card_values = []

# ── WINDOW & WIDGETS ────────────────────────────────────────
window = tk.Tk()
window.title("Boba Memory Match!")
window.geometry("660x580")
window.configure(bg="#FFF0F5")

title_label = tk.Label(
    window,
    text="🧋  Boba Memory Match!",
    font=("Arial", 22, "bold"),
    bg="#FFF0F5",
    fg="#D63384",
)
title_label.pack(pady=10)

score_label = tk.Label(
    window,
    text="Matches: 0 / 6   |   Attempts: 0",
    font=("Arial", 13),
    bg="#FFF0F5",
    fg="#555555",
)
score_label.pack()

info_label = tk.Label(
    window,
    text="Click two cards — match each drink to its price!",
    font=("Arial", 11, "italic"),
    bg="#FFF0F5",
    fg="#999999",
)
info_label.pack(pady=4)

card_frame = tk.Frame(window, bg="#FFF0F5")
card_frame.pack(pady=10)

win_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="#FFF0F5",
    fg="#28A745",
)
win_label.pack(pady=6)

restart_btn = tk.Button(
    window,
    text="🔄  New Game",
    font=("Arial", 12),
    bg="#FFB6C1",
    command=lambda: start_game(),
)
restart_btn.pack(pady=5)


# ── HELPER FUNCTION ─────────────────────────────────────────

def find_pair(value):
    """Return the matching card value for a given card."""
    for name, price in DRINK_PAIRS:
        if value == name:
            return price
        if value == price:
            return name
    return None


# ── GAP 1 SOLUTION ──────────────────────────────────────────

def create_card_values():
    """
    Build a shuffled list of all 12 card values.

    SOLUTION EXPLANATION:
        We loop through DRINK_PAIRS and add both parts of each pair
        to all_values.  After the loop we have 12 items.
        random.shuffle() mixes them up so cards are in a random order.
    """
    all_values = []                         # Step 1: empty list
    for pair in DRINK_PAIRS:               # Step 2: loop through pairs
        all_values.append(pair[0])          # Step 3a: add drink name
        all_values.append(pair[1])          # Step 3b: add price
    random.shuffle(all_values)              # Step 4: shuffle
    return all_values                       # Step 5: return


# ── GAP 2 SOLUTION ──────────────────────────────────────────

def update_score_display():
    """
    Update the score label.

    SOLUTION EXPLANATION:
        score_label.config(text=...) works exactly the same as
        total_label.config(text=...) from the Boba Shop project.
        We use an f-string to insert the variable values.
    """
    score_label.config(
        text=f"Matches: {matched} / 6   |   Attempts: {attempts}"
    )


# ── GAP 3 SOLUTION ──────────────────────────────────────────

def check_win():
    """
    Check if the player has found all 6 pairs.

    SOLUTION EXPLANATION:
        Simple if statement.  When matched reaches 6, all pairs
        have been found and we celebrate with a message.
    """
    if matched == 6:
        win_label.config(text="🎉 You matched all the boba drinks! Amazing! 🧋")


# ── GAP 4 SOLUTION ──────────────────────────────────────────

def check_match():
    """
    Compare the two flipped cards.

    SOLUTION EXPLANATION:
        We read the index of each flipped card from the flipped list,
        look up its value in card_values, and use find_pair() to test
        whether the two values belong together.

        If yes  → disable both buttons, colour them green, add 1 to matched.
        If no   → schedule flip_back() to run after 1 second so the
                  player can see what was under each card before they flip back.

        global matched, flipped is required because we reassign 'matched'
        (matched = matched + 1) and clear 'flipped' inside the function.
    """
    global matched, flipped

    idx1 = flipped[0]                   # Step 1: get card indexes
    idx2 = flipped[1]

    val1 = card_values[idx1]            # Step 2: get card texts
    val2 = card_values[idx2]

    if find_pair(val1) == val2:         # Step 3 + 4a: it's a match!
        cards[idx1].config(state=tk.DISABLED, bg="#98FB98")
        cards[idx2].config(state=tk.DISABLED, bg="#98FB98")
        matched = matched + 1
        flipped.clear()
    else:                               # Step 4b: no match — flip back
        def flip_back():
            cards[idx1].config(text="?", bg="#FFB6C1")
            cards[idx2].config(text="?", bg="#FFB6C1")
            flipped.clear()
        window.after(1000, flip_back)

    update_score_display()              # Step 5
    check_win()


# ── CARD CLICK HANDLER ──────────────────────────────────────

def card_clicked(index):
    """Called when the player clicks a card."""
    global attempts

    if len(flipped) >= 2:
        return
    if index in flipped:
        return

    cards[index].config(text=card_values[index], bg="#FFFACD")
    flipped.append(index)

    if len(flipped) == 2:
        attempts += 1
        update_score_display()
        window.after(500, check_match)


# ── GAME SETUP ──────────────────────────────────────────────

def start_game():
    """Reset and start a new game."""
    global cards, flipped, matched, attempts, card_values

    flipped  = []
    matched  = 0
    attempts = 0
    win_label.config(text="")

    for widget in card_frame.winfo_children():
        widget.destroy()
    cards = []

    card_values = create_card_values()

    for i in range(12):
        row = i // 4
        col = i % 4
        btn = tk.Button(
            card_frame,
            text="?",
            font=("Arial", 12, "bold"),
            width=14,
            height=3,
            bg="#FFB6C1",
            fg="#333333",
            command=lambda idx=i: card_clicked(idx),
        )
        btn.grid(row=row, column=col, padx=6, pady=6)
        cards.append(btn)

    update_score_display()


# ── START ────────────────────────────────────────────────────
start_game()
window.mainloop()
