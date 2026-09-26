# ═══════════════════════════════════════════════════════════
#  🧋  BOBA ORDER TRACKER  — TEACHER SOLUTION
#  Week 15  |  Level 2 Python  |  Review + Code-Together
#  ⚠️  Teacher file — do not share with students
# ═══════════════════════════════════════════════════════════
#
#  Every gap is filled in below, with a short explanation
#  of WHY each line is there.  Search for  ✅ GAP  to jump
#  straight to the answers.
# ═══════════════════════════════════════════════════════════

import tkinter as tk
import random

# ── THE MENU  (a DICTIONARY: drink name → price) ────────────
#
#  Key   = the drink name  (a string)
#  Value = the price       (a number, so we can ADD them up!)
#
#  In Trivia Rush the prices were strings like "$3.50".
#  Today they are real numbers like 3.50 so we can do math.

MENU = {
    "Milk Tea 🧋":        3.50,
    "Taro Tea 🫧":        4.00,
    "Matcha Tea 🍵":      4.50,
    "Mango Tea 🥭":       3.75,
    "Brown Sugar 🧊":     5.00,
    "Strawberry Tea 🍓":  4.25,
}

ALL_DRINKS = list(MENU.keys())   # ["Milk Tea 🧋", "Taro Tea 🫧", ...]

# ── TODAY'S ORDERS  (a LIST: every drink sold, in order) ────
#
#  Every time a drink is ordered it goes on the END of this list.
#  Example after 3 orders:
#      orders = ["Milk Tea 🧋", "Mango Tea 🥭", "Milk Tea 🧋"]

orders = []


# ═══════════════════════════════════════════════════════════
#  WINDOW & WIDGETS  (already done for you — do not change)
# ═══════════════════════════════════════════════════════════

window = tk.Tk()
window.title("Boba Order Tracker! 🧋📋")
window.geometry("560x720")
window.configure(bg="#FFF0F5")

title_label = tk.Label(
    window, text="🧋  Boba Order Tracker",
    font=("Arial", 20, "bold"), bg="#FFF0F5", fg="#D63384",
)
title_label.pack(pady=(12, 0))

subtitle_label = tk.Label(
    window, text="Click a drink to add it to today's orders",
    font=("Arial", 11, "italic"), bg="#FFF0F5", fg="#888888",
)
subtitle_label.pack()

# ── drink buttons: built by LOOPING through the MENU dictionary ──
menu_frame = tk.Frame(window, bg="#FFF0F5")
menu_frame.pack(pady=8)

row = 0
col = 0
for drink in MENU:
    price = MENU[drink]
    b = tk.Button(
        menu_frame, text=f"{drink}\n${price:.2f}",
        font=("Arial", 12, "bold"), width=16, height=2,
        bg="#C8E6FA", fg="#333333",
        command=lambda d=drink: add_order(d),
    )
    b.grid(row=row, column=col, padx=6, pady=6)
    col = col + 1
    if col == 2:          # 2 buttons per row, then start a new row
        col = 0
        row = row + 1

# ── control buttons ──
control_frame = tk.Frame(window, bg="#FFF0F5")
control_frame.pack(pady=4)

surprise_btn = tk.Button(
    control_frame, text="🎲  Surprise Order", font=("Arial", 11),
    bg="#FFD6E7", command=lambda: surprise_order(),
)
surprise_btn.grid(row=0, column=0, padx=5)

undo_btn = tk.Button(
    control_frame, text="↩️  Undo Last", font=("Arial", 11),
    bg="#FFD6E7", command=lambda: undo_last(),
)
undo_btn.grid(row=0, column=1, padx=5)

new_day_btn = tk.Button(
    control_frame, text="🧹  New Day", font=("Arial", 11),
    bg="#FFD6E7", command=lambda: new_day(),
)
new_day_btn.grid(row=0, column=2, padx=5)

# ── bottom area: order list (left) + stats (right) ──
bottom_frame = tk.Frame(window, bg="#FFF0F5")
bottom_frame.pack(padx=20, pady=10, fill="both", expand=True)

list_frame = tk.Frame(bottom_frame, bg="#FFD6E7", bd=2, relief="groove")
list_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

tk.Label(
    list_frame, text="📋  Today's Orders",
    font=("Arial", 12, "bold"), bg="#FFD6E7", fg="#6D2E46",
).pack(pady=(6, 2))

order_box = tk.Listbox(list_frame, font=("Arial", 11), height=11, width=24)
order_box.pack(padx=8, pady=(0, 8), fill="both", expand=True)

stats_frame = tk.Frame(bottom_frame, bg="#FFFFFF", bd=2, relief="groove")
stats_frame.pack(side="right", fill="both", expand=True)

sold_label = tk.Label(
    stats_frame, text="🥤 Drinks sold: 0",
    font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#333333", anchor="w",
)
sold_label.pack(fill="x", padx=10, pady=(10, 2))

total_label = tk.Label(
    stats_frame, text="💰 Total sales: $0.00",
    font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#28A745", anchor="w",
)
total_label.pack(fill="x", padx=10, pady=2)

best_label = tk.Label(
    stats_frame, text="⭐ Best seller: ???",
    font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#D63384", anchor="w",
)
best_label.pack(fill="x", padx=10, pady=2)

tk.Label(
    stats_frame, text="📊  Drink counts",
    font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#6D2E46", anchor="w",
).pack(fill="x", padx=10, pady=(10, 0))

counts_label = tk.Label(
    stats_frame, text="",
    font=("Arial", 11), bg="#FFFFFF", fg="#555555",
    justify="left", anchor="nw",
)
counts_label.pack(fill="both", padx=10, pady=(2, 10))

feedback_label = tk.Label(
    window, text="",
    font=("Arial", 12, "bold"), bg="#FFF0F5", fg="#28A745",
)
feedback_label.pack(pady=(0, 10))


# ═══════════════════════════════════════════════════════════
#  ✅ GAP 1  —  add_order(drink)            👩‍🏫 Teacher types
# ═══════════════════════════════════════════════════════════

def add_order(drink):
    """Add one drink to the END of the orders list, then redraw."""

    # .append() puts the new item at the END of the list.
    # No 'global' needed — we are CHANGING the list that already
    # exists, not replacing it with a new one.
    orders.append(drink)

    # An f-string drops the drink name straight into the message.
    feedback_label.config(text=f"✅ Added {drink}!", fg="#28A745")

    # Redraw the order list and all the stats.
    refresh_screen()


# ═══════════════════════════════════════════════════════════
#  ✅ GAP 2  —  undo_last()                 🤝 We do it together
# ═══════════════════════════════════════════════════════════

def undo_last():
    """Remove the most recent order — but only if there is one!"""

    # len(orders) tells us how many items are in the list.
    # We MUST check first: .pop() on an empty list crashes with
    #   IndexError: pop from empty list
    if len(orders) > 0:
        # .pop() removes the LAST item AND gives it back to us,
        # so we can show which drink was removed.
        removed = orders.pop()
        feedback_label.config(text=f"↩️ Removed {removed}", fg="#D63384")
    else:
        feedback_label.config(text="Nothing to undo!", fg="#DC3545")

    refresh_screen()


# ═══════════════════════════════════════════════════════════
#  ✅ GAP 3  —  get_total()                 🤝 We do it together
# ═══════════════════════════════════════════════════════════

def get_total():
    """Add up the price of every drink in the orders list."""

    # The ACCUMULATOR pattern (same idea as total = total + 3.50
    # in the Boba Shop): start at 0, add a bit each loop.
    total = 0

    # LIST loop — visit every order, one at a time.
    for drink in orders:
        # DICTIONARY lookup — the drink name is the key.
        price = MENU[drink]
        total = total + price

    # Give the answer back to whoever called us (refresh_screen).
    return total


# ═══════════════════════════════════════════════════════════
#  ✅ GAP 4  —  count_drinks()              🤝 We do it together
# ═══════════════════════════════════════════════════════════

def count_drinks():
    """Build a dictionary that counts how many of each drink sold."""

    # Start with an EMPTY dictionary.
    counts = {}

    for drink in orders:
        if drink in counts:
            # Seen it before → add 1 to its count.
            counts[drink] = counts[drink] + 1
        else:
            # First time → create the key with a count of 1.
            # (counts[drink] + 1 here would crash with a KeyError!)
            counts[drink] = 1

    # e.g. {"Milk Tea 🧋": 2, "Mango Tea 🥭": 1}
    return counts


# ═══════════════════════════════════════════════════════════
#  ✅ GAP 5  —  find_best_seller(counts)    🧑‍💻 You try first!
# ═══════════════════════════════════════════════════════════

def find_best_seller(counts):
    """Return the drink with the BIGGEST count in the counts dict."""

    # The "king of the hill" pattern: keep track of the best one
    # we've seen so far, and replace it if we find a bigger one.
    best_drink = "None yet"
    best_count = 0

    # Looping through a DICTIONARY gives us each KEY (drink name).
    for drink in counts:
        if counts[drink] > best_count:
            best_count = counts[drink]
            best_drink = drink

    # If two drinks tie, the one found first stays on top,
    # because  >  (not >=)  only replaces on a BIGGER count.
    return best_drink


# ═══════════════════════════════════════════════════════════
#  HELPERS  (already done for you — read and understand!)
# ═══════════════════════════════════════════════════════════

def refresh_screen():
    """Redraw the order list and all the stats.  Calls YOUR gap functions!"""

    # 1) the order list — numbered, with prices from the MENU
    order_box.delete(0, tk.END)
    for i in range(len(orders)):
        drink = orders[i]
        order_box.insert(tk.END, f"{i + 1}.  {drink}   ${MENU[drink]:.2f}")

    # 2) the stats
    total  = get_total()                 # YOUR Gap 3
    counts = count_drinks()              # YOUR Gap 4
    best   = find_best_seller(counts)    # YOUR Gap 5

    sold_label.config(text=f"🥤 Drinks sold: {len(orders)}")
    total_label.config(text=f"💰 Total sales: ${total:.2f}")
    best_label.config(text=f"⭐ Best seller: {best}")

    # 3) the tally — one line per drink on the menu
    tally = ""
    for drink in MENU:
        if drink in counts:
            tally = tally + f"{drink}  ×  {counts[drink]}\n"
        else:
            tally = tally + f"{drink}  ×  0\n"
    counts_label.config(text=tally)


def surprise_order():
    """Add a random drink — great for testing quickly!"""
    drink = random.choice(ALL_DRINKS)
    add_order(drink)                     # YOUR Gap 1


def new_day():
    """Clear every order and start fresh."""
    # This one DOES need 'global' — we REPLACE the whole list
    # with a brand-new empty one using  =
    global orders
    orders = []
    feedback_label.config(text="🧹 New day! All orders cleared.", fg="#6D2E46")
    refresh_screen()


# ── START THE APP ───────────────────────────────────────────
refresh_screen()
window.mainloop()
