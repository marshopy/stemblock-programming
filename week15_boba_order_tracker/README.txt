═══════════════════════════════════════════════════════════
  🧋  BOBA ORDER TRACKER  —  README
  Week 15  |  Level 2 Python  |  Review + Code-Together
═══════════════════════════════════════════════════════════


── WHAT IS THIS APP? ──────────────────────────────────────

  The Boba Order Tracker is the app a boba shop uses at the
  counter during the day.

    Click a drink button  → the drink is added to today's orders
    The app shows         → every order, the total sales,
                            a count of each drink, and
                            today's ⭐ best seller
    ↩️ Undo Last          → removes the most recent order
    🎲 Surprise Order     → adds a random drink (fast testing!)
    🧹 New Day            → clears everything

  This week is a REVIEW week.  The whole app is built from
  two things you already know:

    LIST        orders = ["Milk Tea 🧋", "Mango Tea 🥭", ...]
    DICTIONARY  MENU   = {"Milk Tea 🧋": 3.50, ...}


── FILES IN THIS FOLDER ───────────────────────────────────

  game.py          ← STUDENT FILE  (open this in Thonny!)
                      Contains 5 gaps marked with  🔧 FIX ME
                      The app already runs; each gap you
                      fill in turns on a new part of the screen.

  solution.py      ← TEACHER FILE  (do not share with students)
                      Complete working version with all gaps filled.
                      Each gap has an explanation of the solution.

  hints.txt        ← HINTS  (open if you get stuck)
                      Four or five levels of hints per gap, plus
                      a list of common errors and their fixes.

  teacher_notes.txt← TEACHER NOTES  (instructor use only)
                      Review-quiz answers, how to run the
                      code-together, per-gap notes, common mistakes.

  boba_student.zip ← STUDENT ZIP  (game.py + hints.txt + README.txt)
                      Hand this out instead of the whole folder.

  README.txt       ← THIS FILE


── HOW TO OPEN IN THONNY ──────────────────────────────────

  1. Open Thonny on your computer.
  2. Click  File  →  Open...
  3. Navigate to this folder and select  game.py
  4. Press  F5  (or click the green Run button ▶) to run.
  5. The window appears.  Clicking drinks won't work yet —
     that's Gap 1!


── HOW WE'LL WORK TODAY ───────────────────────────────────

  We fill in the gaps TOGETHER, one at a time:

    👩‍🏫  I DO     Teacher types, you type along         (Gap 1)
    🤝  WE DO    Class suggests each line together    (Gaps 2, 3, 4)
    🧑‍💻  YOU DO   Try it yourself first, then we share (Gap 5)

  Run the app (F5) after EVERY gap.


── THE 5 GAPS ─────────────────────────────────────────────

  GAP 1  add_order(drink)                    👩‍🏫 I do
      → Put the drink on the END of the orders list
      → Practices: list.append, f-strings, calling a function

  GAP 2  undo_last()                         🤝 We do
      → If there are orders, remove the last one; else say so
      → Practices: len(), list.pop(), if / else

  GAP 3  get_total()                         🤝 We do
      → Loop through the orders list, look up each price in MENU
      → Practices: for loop, dictionary lookup, accumulator, return

  GAP 4  count_drinks()                      🤝 We do
      → Build a NEW dictionary: drink → how many sold
      → Practices: empty dict, "in" check, adding & changing keys

  GAP 5  find_best_seller(counts)            🧑‍💻 You do
      → Loop through the counts dictionary, keep the biggest
      → Practices: looping a dict, >, "king of the hill" pattern


── SUGGESTED TESTING ORDER ────────────────────────────────

  Before any gaps:  Window opens. Stats show 0 / $0.00 / ???
  After Gap 1:  Click drinks → they appear in "Today's Orders"
                and "Drinks sold" goes up
  After Gap 2:  ↩️ Undo removes the last order.  Undo on an
                empty list says "Nothing to undo!" (no crash)
  After Gap 3:  Total sales shows the right amount
                (Milk Tea + Mango Tea = $7.25)
  After Gap 4:  The 📊 Drink counts panel shows real numbers
  After Gap 5:  ⭐ Best seller shows the drink with the most sales;
                🧹 New Day resets it to "None yet"


── WHAT WE'RE REVIEWING ───────────────────────────────────

  Week 2   Lists & a digital store     →  orders list, append, pop
  Week 3   Dictionaries                →  MENU, counts
  Week 5   Tracing code                →  trace tables for Gaps 3 & 4
  Week 8   Boba Store (OOP)            →  self.items = [] was a list too!
  Week 11  Saving the menu             →  bonus: save orders to a file
  Shop GUI tkinter Boba Shop           →  total = total + price, :.2f
  Week 12  Memory Match                →  lists, loops, if / else
  Week 13  Trivia Rush                 →  DRINK_DICT, keys(), lambda d=drink
  Week 14  Pocket Pet (big review)     →  FOODS dict, tricks list, loops


── BONUS CHALLENGES ────────────────────────────────────────

  ⭐   Add a 7th drink to MENU (e.g. "Lychee Tea 🍑": 4.75).
       A new button appears by itself!  Why?

  ⭐   Change a price in MENU and watch the total change.

  ⭐⭐  Show the AVERAGE price per drink:  total / len(orders)
       (Careful — what happens when there are 0 orders?)

  ⭐⭐  Show how many the best seller sold:
       "⭐ Best seller: Milk Tea 🧋 (3 sold)"

  ⭐⭐  Add a daily goal:  SALES_GOAL = 50
       Show "🎯 $12.50 to go!" or "🎉 Goal reached!"

  ⭐⭐⭐ Save today's orders to orders.txt (Week 11!) and load
        them back when the app starts.


═══════════════════════════════════════════════════════════
  Good luck and have fun!  🧋📋
═══════════════════════════════════════════════════════════
