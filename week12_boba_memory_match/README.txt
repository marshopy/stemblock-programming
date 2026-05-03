═══════════════════════════════════════════════════════════
  🧋  BOBA MEMORY MATCH  —  README
  Level 2 Python  |  Fill-in-the-Gap Game Activity
═══════════════════════════════════════════════════════════


── WHAT IS THIS GAME? ─────────────────────────────────────

  Boba Memory Match is a card-matching game!
  12 cards are placed face-down on the screen.
  Each drink name (e.g. "Milk Tea 🧋") has a matching price
  card (e.g. "$3.50") somewhere on the board.

  Click two cards to flip them over.
  If they match → they stay green and you earn a point!
  If they don't match → they flip back after 1 second.
  Find all 6 pairs to win!


── FILES IN THIS FOLDER ───────────────────────────────────

  game.py       ← STUDENT FILE  (open this in Thonny!)
                   Contains 4 gaps marked with  🔧 FIX ME
                   Fill them in to make the game work.

  solution.py   ← TEACHER FILE  (do not share with students)
                   Complete working version with all gaps filled.

  hints.txt     ← HINTS  (open if you get stuck)
                   Three levels of hints for each gap,
                   plus a list of common errors and fixes.

  README.txt    ← THIS FILE


── HOW TO OPEN IN THONNY ──────────────────────────────────

  1. Open Thonny on your computer.

  2. Click  File  →  Open...

  3. Navigate to this folder and select  game.py

  4. Press  F5  (or click the green Run button ▶) to run.

  5. A window should appear — but some things won't work yet
     until you fill in the gaps!


── WHAT STUDENTS NEED TO DO ───────────────────────────────

  Read each  🔧 FIX ME  section carefully.
  The instructions above each gap explain exactly what to write.
  Delete the word  pass  and replace it with your code.

  GAP 1  create_card_values()
      → Loop through DRINK_PAIRS and build a shuffled list
      → Practices: lists, for loops, append, return

  GAP 2  update_score_display()
      → Update a label using .config(text=...)
      → Practices: f-strings, calling methods on widgets

  GAP 3  check_win()
      → Write an if statement to detect when the game is won
      → Practices: if statements, == operator, updating labels

  GAP 4  check_match()
      → Compare two card values and handle match vs. no-match
      → Practices: list indexing, if/else, global variables,
                   calling functions, window.after() for delay


── SUGGESTED ORDER ────────────────────────────────────────

  Work through the gaps in order: 1 → 2 → 3 → 4.
  After each gap, press F5 to run and test your progress!

  After Gap 1:  Cards should appear shuffled (not always ABAB)
  After Gap 2:  The score label should say "Matches: 0 / 6"
  After Gap 3:  (No visible change yet — Gap 4 triggers this)
  After Gap 4:  The full game works!  Cards match, score updates,
                and "You win!" appears when all pairs are found.


── BONUS CHALLENGES ────────────────────────────────────────

  ⭐  Change the window background color with a hex code
      (hint: window.configure(bg="#your_color_here"))

  ⭐  Add a 7th drink pair to DRINK_PAIRS
      (remember to also update "/ 6" in update_score_display
       and "== 6" in check_win to match the new count!)

  ⭐  Change the card colors — pick your own hex codes for:
         face-down cards   (currently "#FFB6C1"  light pink)
         revealed cards    (currently "#FFFACD"  light yellow)
         matched cards     (currently "#98FB98"  light green)

  ⭐⭐  Add a "Best Attempts" tracker that saves the
       lowest number of attempts across games.


── CONNECTING TO WHAT YOU ALREADY KNOW ───────────────────

  This game uses everything from your Boba Shop project!

  global total            →  global matched, flipped
  total_label.config(...) →  score_label.config(...)
  if total == 0:          →  if matched == 6:
  order_box.insert(...)   →  cards[i].config(...)
  Lists from Week 10      →  card_values list, cards list


═══════════════════════════════════════════════════════════
  Good luck and have fun!  🧋✨
═══════════════════════════════════════════════════════════
