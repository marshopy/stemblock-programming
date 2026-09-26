# ═══════════════════════════════════════════════════════════
#  🧋  BOBA ORDER TRACKER  — Student Version
#  Week 15  |  Level 2 Python  |  Review + Code-Together!
# ═══════════════════════════════════════════════════════════
#
#  WHAT IT DOES:
#    • Click a drink button to sell that drink
#    • Every order appears in the "Today's Orders" list
#    • The app adds up the total sales for the day
#    • It counts how many of EACH drink were sold
#    • It finds today's ⭐ best seller
#
#  YOUR JOB:
#    There are 5 gaps marked with  🔧 FIX ME
#    We will fill them in TOGETHER as a class:
#        Gap 1  →  👩‍🏫 Teacher types, you follow along
#        Gap 2, 3, 4  →  🤝 We build them together
#        Gap 5  →  🧑‍💻 You try first, then we share
#    Write your code where it says  ✏️ YOUR CODE HERE
#
#  TODAY'S REVIEW:  LISTS  +  DICTIONARIES  (+ loops, if/else,
#                   functions, return, f-strings)
#
#  HINT FILE:  Open hints.txt if you get stuck!
#  The app runs RIGHT NOW — run it (F5) after every gap to see
#  a new part of the screen come to life.
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
#  🔧 GAP 1  —  add_order(drink)            👩‍🏫 Teacher types
# ═══════════════════════════════════════════════════════════

def add_order(drink):
    """
    Add one drink to the END of the orders list, then redraw.

    WHAT YOU HAVE:
        drink          →  the drink name that was clicked,
                          e.g. "Milk Tea 🧋"
        orders         →  the LIST of every drink sold today
        feedback_label →  the message label at the bottom
        refresh_screen()  →  already written — redraws everything

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Add the drink to the END of the orders list:
                       orders.append(drink)

        Step 2  →  Show a message using an f-string:
                       feedback_label.config(
                           text=f"✅ Added {drink}!", fg="#28A745"
                       )

        Step 3  →  Redraw the screen:
                       refresh_screen()

    ──────────────────────────────────────────────────────────
    💡 REVIEW: list.append(item)
        Adds item to the END of a list.
        cups = ["Milk"]  →  cups.append("Taro")  →  ["Milk", "Taro"]

    💡 No 'global' needed here!  .append() CHANGES the list that
       already exists.  (Look at new_day() at the bottom — it DOES
       need global, because it REPLACES the list with  orders = [] )
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 2  —  undo_last()                 🤝 We do it together
# ═══════════════════════════════════════════════════════════

def undo_last():
    """
    Remove the most recent order — but only if there is one!

    WHAT YOU HAVE:
        orders         →  the LIST of every drink sold today
        feedback_label →  the message label at the bottom
        refresh_screen()  →  already written — redraws everything

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Check that the list is NOT empty:
                       if len(orders) > 0:

        Step 2  →  Inside the if: remove the LAST drink.
                   .pop() removes it AND gives it back to you:
                           removed = orders.pop()
                           feedback_label.config(
                               text=f"↩️ Removed {removed}", fg="#D63384"
                           )

        Step 3  →  Otherwise (else): the list is empty — say so:
                       else:
                           feedback_label.config(
                               text="Nothing to undo!", fg="#DC3545"
                           )

        Step 4  →  AFTER the if/else (not inside it!), redraw:
                       refresh_screen()

    ──────────────────────────────────────────────────────────
    💡 REVIEW: len(list)  and  list.pop()
        len(["a", "b", "c"])  →  3
        cups = ["Milk", "Taro"]
        last = cups.pop()     →  last is "Taro", cups is ["Milk"]
        .pop() on an EMPTY list crashes — that's why we check first!
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE  (delete the word 'pass' first!)
    pass   # 🔧 FIX ME


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 3  —  get_total()                 🤝 We do it together
# ═══════════════════════════════════════════════════════════

def get_total():
    """
    Add up the price of every drink in the orders list,
    and RETURN the total.

    WHAT YOU HAVE:
        orders  →  LIST of drink names, e.g. ["Milk Tea 🧋", "Mango Tea 🥭"]
        MENU    →  DICTIONARY of drink name → price, e.g. MENU["Milk Tea 🧋"] → 3.5

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Start a running total at zero:
                       total = 0

        Step 2  →  Loop through every drink in the orders LIST:
                       for drink in orders:

        Step 3  →  Inside the loop: look up the drink's price in
                   the MENU DICTIONARY and add it on:
                           price = MENU[drink]
                           total = total + price

        Step 4  →  AFTER the loop (not inside it!), give it back:
                       return total

    ──────────────────────────────────────────────────────────
    💡 REVIEW: the ACCUMULATOR pattern (from the Boba Shop!)
        total = 0            ← start empty
        total = total + 3.5  ← keep adding, don't replace
    💡 LIST gives us the drinks  →  DICTIONARY gives us the prices
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE
    # When your code has its own  return total , delete the line below.
    return 0   # 🔧 FIX ME  (placeholder — always says $0.00)


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 4  —  count_drinks()              🤝 We do it together
# ═══════════════════════════════════════════════════════════

def count_drinks():
    """
    Build and RETURN a DICTIONARY that counts how many of each
    drink were sold.

        orders = ["Milk Tea 🧋", "Mango Tea 🥭", "Milk Tea 🧋"]
        count_drinks()  →  {"Milk Tea 🧋": 2, "Mango Tea 🥭": 1}

    WHAT YOU HAVE:
        orders  →  LIST of every drink sold today

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Start with an EMPTY dictionary:
                       counts = {}

        Step 2  →  Loop through every drink in the orders list:
                       for drink in orders:

        Step 3  →  Inside the loop, ask: have we seen this drink before?
                           if drink in counts:
                               counts[drink] = counts[drink] + 1
                           else:
                               counts[drink] = 1

        Step 4  →  AFTER the loop, give the dictionary back:
                       return counts

    ──────────────────────────────────────────────────────────
    💡 REVIEW: key in dict   →   True or False
        "Milk Tea 🧋" in {"Milk Tea 🧋": 2}   →  True
    💡 Why the else?  The FIRST time we see a drink it isn't a key
       yet, so  counts[drink] + 1  would crash with a KeyError.
       We have to CREATE the key first:  counts[drink] = 1
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE
    # When your code has its own  return counts , delete the line below.
    return {}   # 🔧 FIX ME  (placeholder — always an empty dictionary)


# ═══════════════════════════════════════════════════════════
#  🔧 GAP 5  —  find_best_seller(counts)    🧑‍💻 You try first!
# ═══════════════════════════════════════════════════════════

def find_best_seller(counts):
    """
    Look through the counts DICTIONARY and RETURN the drink
    with the BIGGEST count.

        find_best_seller({"Milk Tea 🧋": 2, "Mango Tea 🥭": 1})
        →  "Milk Tea 🧋"

    WHAT YOU HAVE:
        counts  →  the dictionary from YOUR Gap 4,
                   drink name (key) → how many sold (value)

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP GUIDE:

        Step 1  →  Make two "best so far" variables:
                       best_drink = "None yet"
                       best_count = 0

        Step 2  →  Loop through the dictionary.
                   Looping a dict gives you each KEY (the drink name):
                       for drink in counts:

        Step 3  →  Inside the loop: is this drink's count BIGGER
                   than the best so far?  If yes, it takes the crown!
                           if counts[drink] > best_count:
                               best_count = counts[drink]
                               best_drink = drink

        Step 4  →  AFTER the loop, give back the winner:
                       return best_drink

    ──────────────────────────────────────────────────────────
    💡 The "king of the hill" pattern:
        Keep the best one you've seen so far.
        Every time you find a bigger one, it becomes the new king.
    ──────────────────────────────────────────────────────────
    """

    # ✏️ YOUR CODE HERE
    # When your code has its own  return best_drink , delete the line below.
    return "???"   # 🔧 FIX ME  (placeholder)


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
