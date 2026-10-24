═══════════════════════════════════════════════════════════
  🛡️  CRASH-PROOF CHARACTER CREATOR  —  README
  Week 16  |  Level 2 Python  |  Advanced Types,
                                 Conversion & Validation
═══════════════════════════════════════════════════════════


── WHAT IS THIS? ──────────────────────────────────────────

  Students already know int, float, str and bool from Level 1.
  Week 16 levels up:

    📦  Advanced types   tuples · sets · nested data
    🔄  Conversion       switching between ANY types
                         (and the bool("False") trap!)
    🛡️  Validation       isinstance() · .isdigit() · try / except
                         · the validation loop

    Part 1  —  One challenge per idea, then Name That Type
               and Spot the Bug
    Part 2  —  We build the Crash-Proof Character Creator together

  The Crash-Proof Character Creator is a text program that runs
  in the Thonny Shell.  You make a game hero, and the program
  NEVER crashes — every answer is validated, converted to the
  right type, stored in an advanced type, and type-checked.
  At the end it saves the hero as text and loads it back.


── FILES IN THIS FOLDER ───────────────────────────────────

  character_creator_starter.py ← STUDENT FILE  (open this in Thonny!)
                                  Only has the step headings.
                                  We type the code together from the slides.

  character_creator.py         ← COMPLETE VERSION
                                  Run it at the start of Part 2 and let
                                  the class try to crash it.

  review_challenges.py         ← TEACHER FILE
                                  Every Part 1 challenge — press F5 to
                                  see the real answers.

  teacher_notes.txt            ← TEACHER NOTES  (timing, answers, tips)

  README.txt                   ← THIS FILE

  The slides are in  week16-data-types.pptx


── HOW TO OPEN IN THONNY ──────────────────────────────────

  1. Open Thonny on your computer.
  2. Click  File  →  Open...
  3. Select  character_creator_starter.py
  4. Type the code for each step from the slides.
  5. Steps 1-4 make "validator" functions.  After pressing F5,
     test them by typing a call in the Shell, for example:
         >>> ask_int("Level? ", 1, 10)
  6. Steps 5-10 run like a normal program — answer in the Shell.


── THE 10 STEPS ───────────────────────────────────────────

  Step 1   Ask for a whole number   VALIDATE   try / except · range check
  Step 2   Ask for a decimal        VALIDATE   copy & change: float()
  Step 3   Ask yes or no            VALIDATE   a set of answers → bool
  Step 4   Ask for a name           VALIDATE   .strip() · .isalpha() · len()
  Step 5   Ask the questions        USE        call our validators
  Step 6   Skills                   CONVERT    split() → list → set
  Step 7   Home on the map          STORE      tuple · unpacking
  Step 8   The hero                 STORE      nested dict
  Step 9   Type check               CHECK      isinstance()
  Step 10  Save & load              CONVERT    to text and back again


── TRY TO BREAK IT ────────────────────────────────────────

  ✅ Words, huge numbers, nothing at all → no crash
  ✅ Name R2D2 → "Letters only"
  ✅ Speed 2 → saved as 2.0 (a float)
  ✅ Magic: maybe → asks again;  YES → True
  ✅ Skills: fly, Fly, swim → 2 unique skills
  ✅ Change  speed = 2  in Step 5 → the type check says
     "✖ speed: NOT float"


── BONUS CHALLENGES ────────────────────────────────────────

  ⭐    Accept "yeah" and "nope" in the YES and NO sets
  ⭐    Ask for a lucky number from 1 to 99 with ask_int
  ⭐⭐   Merge ask_int and ask_float into one ask_number()
  ⭐⭐   Only allow skills from a set of ALLOWED_SKILLS
  ⭐⭐⭐  A party: a list of 3 hero dictionaries
  ⭐⭐⭐  Save the hero to hero.txt and load it next time


═══════════════════════════════════════════════════════════
  Have fun — and try to break it!  🛡️
═══════════════════════════════════════════════════════════
