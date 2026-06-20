═══════════════════════════════════════════════════════════
  🧋  BOBA TRIVIA RUSH  —  README
  Week 13  |  Level 2 Python  |  Fill-in-the-Gap Game Activity
═══════════════════════════════════════════════════════════


── WHAT IS THIS GAME? ─────────────────────────────────────

  Boba Trivia Rush is a timed trivia quiz!
  A boba drink name appears on screen.
  Four price buttons appear — only ONE is correct.
  Click the right price before the 8-second timer runs out!

    Correct answer → +10 points, next question
    Wrong or too slow → lose a life ❤️

  8 questions per game.  3 lives.  Max score: 80 points.
  Find all 6 pairs to win!


── FILES IN THIS FOLDER ───────────────────────────────────

  game.py          ← STUDENT FILE  (open this in Thonny!)
                      Contains 6 gaps marked with  🔧 FIX ME
                      Fill them in to make the game work.

  solution.py      ← TEACHER FILE  (do not share with students)
                      Complete working version with all gaps filled.
                      Each gap has an explanation of the solution.

  hints.txt        ← HINTS  (open if you get stuck)
                      Four levels of hints per gap, plus
                      a list of common errors and their fixes.

  teacher_notes.txt← TEACHER NOTES  (instructor use only)
                      Per-gap teaching notes, common mistakes,
                      differentiation strategies, bonus challenges.

  README.txt       ← THIS FILE


── HOW TO OPEN IN THONNY ──────────────────────────────────

  1. Open Thonny on your computer.
  2. Click  File  →  Open...
  3. Navigate to this folder and select  game.py
  4. Press  F5  (or click the green Run button ▶) to run.
  5. A window appears — but gaps still need to be filled!


── WHAT STUDENTS NEED TO DO ───────────────────────────────

  Work through the 6 gaps IN ORDER.  Run the game after each one!

  GAP 1  build_wrong_answers(correct_price)
      → Filter ALL_PRICES to remove the correct one
      → Use random.sample to pick 3 wrong prices
      → Practices: for loop, if filtering, random.sample (NEW)

  GAP 2  load_question()
      → Pick the drink from question_order using question_num
      → Look up its price in the DRINK_DICT dictionary
      → Wire up the 4 answer buttons with shuffled prices
      → Practices: dictionary lookup (NEW), list indexing, lambda

  GAP 3  tick()
      → Subtract 1 from time_left each second
      → Update the timer label and shrink the progress bar
      → Reschedule itself with window.after, or call time_up()
      → Practices: recursive window.after (NEW), ratio math

  GAP 4  answer_clicked(chosen_price)
      → Stop the timer, disable buttons
      → Compare chosen price to correct price, update score/lives
      → Schedule the next question
      → Practices: calling functions, if/else, global variables

  GAP 5  update_display()
      → Update the score, hearts, and question-counter labels
      → Practices: f-strings, string * integer (NEW), .config()

  GAP 6  check_game_over()
      → If lives == 0 OR past final question: show final screen
      → Otherwise: load the next question
      → Practices: or operator (NEW), if/else decisions


── SUGGESTED TESTING ORDER ────────────────────────────────

  After Gap 1:  Game should start (no crash on load)
  After Gap 2:  A drink name appears on the label;
                4 price buttons show different prices
  After Gap 3:  Timer counts down 8→7→6… and the bar shrinks;
                "Time's up!" appears at 0
  After Gap 4:  Clicking a button shows "✅ Correct!" or "❌ Wrong!"
                and the score/lives change
  After Gap 5:  Score label, heart count, and Q counter all update
  After Gap 6:  Final screen appears after 8 questions or 0 lives;
                "Play Again" button works


── WHAT'S NEW COMPARED TO WEEK 12 ────────────────────────

  Week 12 (Memory Match)         Week 13 (Trivia Rush)
  ─────────────────────────────────────────────────────
  DRINK_PAIRS  (list of tuples)  DRINK_DICT  (dictionary)
  4 gaps                         6 gaps
  window.after for 1-shot delay  window.after for countdown timer
  random.shuffle                 random.sample  (new!)
  if matched == 6                if lives==0 or question_num>8
  string f-strings               string * integer  (new!)


── BONUS CHALLENGES ────────────────────────────────────────

  ⭐   Change TIMER_SECONDS = 5 at the top for a harder mode

  ⭐   Add a 9th drink to DRINK_DICT; update TOTAL_QUESTIONS = 9

  ⭐⭐  After a wrong answer, highlight the CORRECT button green
       and the chosen button red before moving to the next question

  ⭐⭐  Swap the question: show a PRICE and ask for the DRINK NAME

  ⭐⭐⭐ Track the best score across games using a module-level
        variable  best_score = 0  and update it in show_final_screen()


═══════════════════════════════════════════════════════════
  Good luck and have fun!  🧋⚡
═══════════════════════════════════════════════════════════
