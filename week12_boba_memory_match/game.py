# ═══════════════════════════════════════════════════════════
#  🧋  BOBA MEMORY MATCH  — Student Version
#  Level 2 Python  |  Fill in the Gaps to make it work!
# ═══════════════════════════════════════════════════════════
#
#  HOW TO PLAY:
#    • 12 cards are face-down, each showing "?"
#    • Click any card to flip it over and see its text
#    • Click a second card — if the drink name matches
#      its price, it's a PAIR and both cards stay green!
#    • If they don't match, both flip back after 1 second
#    • Find all 6 pairs to WIN!
#
#  YOUR JOB:
#    There are 4 gaps marked with  🔧 FIX ME
#    Read the instructions above each gap carefully,
#    then write your code where it says  ✏️ YOUR CODE HERE
#
#  HINT FILE:  Open hints.txt if you get stuck!
# ═══════════════════════════════════════════════════════════

import tkinter as tk
import random

# ── DRINK DATA ──────────────────────────────────────────────
# These are the 6 drink pairs: (name, price)
# A card showing "Milk Tea 🧋" must match a card showing "$3.50"

DRINK_PAIRS = [
    ("Milk Tea 🧋",       "$3.50"),
    ("Taro Tea 🫧",       "$4.00"),
    ("Matcha Tea 🍵",     "$4.50"),
    ("Strawberry Tea 🍓", "$4.25"),
    ("Mango Tea 🥭",      "$3.75"),
    ("Brown Sugar 🧊",    "$5.00"),
]

# ── GAME STATE VARIABLES ────────────────────────────────────
# These track what is happening in the game right now.

cards       = []   # list of all 12 card buttons
flipped     = []   # indexes of the cards currently face-up (max 2)
matched     = 0    # how many pairs the player has found
attempts    = 0    # how many guesses the player has made
card_values = []   # the hidden text on each card (set when game starts)


# ═══════════════════════════════════════════════════════════
#  WINDOW & WIDGETS  (already done for you — do not change)
# ═══════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════
#  HELPER FUNCTION  (already done for you — read it!)
# ═══════════════════════════════════════════════════════════

def find_pair(value):
    """
    Given any card value, return what it should be paired with.

    Examples:
        find_pair("Milk Tea 🧋")  →  "$3.50"
        find_pair("$3.50")        →  "Milk Tea 🧋"
        find_pair("Taro Tea 🫧")  →  "$4.00"
    """
    for name, price in DRINK_PAIRS:
        if value == name:
            return price
        if value == price:
            return name
    return None


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 1  —  create_card_values()
# ═══════════════════════════════════════════════════════════

def create_card_values():
    """
    Build a SHUFFLED list of all 12 card values.

    There are 6 drink pairs, so we need 12 cards total:
        6 drink names  +  6 prices  =  12 values

    HOW TO DO IT:
        Step 1  →  Create an empty list:  all_values = []
        Step 2  →  Loop through DRINK_PAIRS with a for loop
                       Each 'pair' has two parts:
                           pair[0]  =  the drink name   (e.g. "Milk Tea 🧋")
                           pair[1]  =  the price         (e.g. "$3.50")
        Step 3  →  Inside the loop, add BOTH parts to all_values:
                       all_values.append(pair[0])
                       all_values.append(pair[1])
        Step 4  →  After the loop, shuffle the list:
                       random.shuffle(all_values)
        Step 5  →  Return the finished list:  return all_values

    When done, all_values should have 12 items, mixed up randomly.
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 2  —  update_score_display()
# ═══════════════════════════════════════════════════════════

def update_score_display():
    """
    Update score_label to show the current matches and attempts.

    HOW TO DO IT:
        Use score_label.config(text=...) — the same way you
        updated total_label in your Boba Shop project!

        The label should look like this:
            "Matches: 2 / 6   |   Attempts: 5"

        Use an f-string:
            f"Matches: {matched} / 6   |   Attempts: {attempts}"
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 3  —  check_win()
# ═══════════════════════════════════════════════════════════

def check_win():
    """
    Check whether the player has found all 6 pairs.

    HOW TO DO IT:
        Write an if statement:
            if matched == 6:
                win_label.config(text="🎉 You matched all the boba drinks! Amazing! 🧋")

        That's it!  Just those two lines.
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 4  —  check_match()
# ═══════════════════════════════════════════════════════════

def check_match():
    """
    Compare the two flipped cards to see if they are a matching pair.

    WHAT YOU HAVE TO WORK WITH:
        flipped      →  a list with 2 card indexes, e.g. [3, 7]
        card_values  →  a list of all 12 card texts
                        e.g. card_values[3] might be "Milk Tea 🧋"
                             card_values[7] might be "$3.50"

    STEP-BY-STEP GUIDE:

        Step 1  →  Get the index of each flipped card:
                       idx1 = flipped[0]
                       idx2 = flipped[1]

        Step 2  →  Get the text on each card:
                       val1 = card_values[idx1]
                       val2 = card_values[idx2]

        Step 3  →  Check if they match using find_pair():
                       if find_pair(val1) == val2:

        Step 4a →  IF they MATCH:
                       # Keep both cards face-up and turn them green
                       cards[idx1].config(state=tk.DISABLED, bg="#98FB98")
                       cards[idx2].config(state=tk.DISABLED, bg="#98FB98")
                       # Count the match
                       matched = matched + 1
                       # Clear the flipped list so the player can flip again
                       flipped.clear()

        Step 4b →  IF they DON'T MATCH (the else branch):
                       # After 1 second, flip both cards back to "?"
                       # Copy this code exactly:
                       def flip_back():
                           cards[idx1].config(text="?", bg="#FFB6C1")
                           cards[idx2].config(text="?", bg="#FFB6C1")
                           flipped.clear()
                       window.after(1000, flip_back)

        Step 5  →  After the if/else, call these two functions:
                       update_score_display()
                       check_win()

    IMPORTANT:  Add  global matched, flipped  as the very first line
                inside this function (before Step 1).
    """

    global matched, flipped

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  CARD CLICK HANDLER  (already done for you — read it!)
# ═══════════════════════════════════════════════════════════

def card_clicked(index):
    """Called automatically when the player clicks a card."""
    global attempts

    # Stop if 2 cards are already flipped (waiting for check_match)
    if len(flipped) >= 2:
        return

    # Stop if the player clicks the same card twice
    if index in flipped:
        return

    # Reveal this card (show its real value, turn it yellow)
    cards[index].config(text=card_values[index], bg="#FFFACD")
    flipped.append(index)

    # Once 2 cards are face-up, wait 0.5 sec then check for a match
    if len(flipped) == 2:
        attempts += 1
        update_score_display()          # calls your Gap 2 function!
        window.after(500, check_match)  # calls your Gap 4 function!


# ═══════════════════════════════════════════════════════════
#  GAME SETUP  (already done for you — do not change)
# ═══════════════════════════════════════════════════════════

def start_game():
    """Reset everything and start a new game."""
    global cards, flipped, matched, attempts, card_values

    # Reset all game state
    flipped  = []
    matched  = 0
    attempts = 0
    win_label.config(text="")

    # Remove any old card buttons from the window
    for widget in card_frame.winfo_children():
        widget.destroy()
    cards = []

    # Build the shuffled card list — calls YOUR Gap 1 function!
    card_values = create_card_values()

    # Create 12 card buttons arranged in a 3-row × 4-column grid
    for i in range(12):
        row = i // 4   # which row  (0, 1, or 2)
        col = i % 4    # which column (0, 1, 2, or 3)

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

    update_score_display()   # calls YOUR Gap 2 function!


# ── START THE GAME ──────────────────────────────────────────
start_game()
window.mainloop()
