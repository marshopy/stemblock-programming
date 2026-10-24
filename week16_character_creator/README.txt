═══════════════════════════════════════════════════════════
  🧙  CHARACTER CREATOR  —  README
  Week 16  |  Level 2 Python  |  Data Types
═══════════════════════════════════════════════════════════


── WHAT IS THIS? ──────────────────────────────────────────

  Week 16 is all about DATA TYPES — the different kinds of
  values Python works with.

    Part 1  —  Meet the types: one "what's the print value?"
               challenge for each type, then Name That Type
               and Spot the Bug
    Part 2  —  We build the Character Creator together

  Character Creator is a text program that runs in the Thonny
  Shell.  You make a game hero by answering questions, and every
  answer is saved with a different data type:

    str · int · float · bool · list · tuple · None · dict

  After each answer it tells you which type it used.  At the
  end you get a Hero Card — and your hero levels up!


── FILES IN THIS FOLDER ───────────────────────────────────

  character_creator_starter.py ← STUDENT FILE  (open this in Thonny!)
                                  Only has the step headings.
                                  We type the code together from the slides.

  character_creator.py         ← COMPLETE VERSION
                                  The finished program.  Run it at the
                                  start of Part 2 to show the goal.

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
  5. Press  F5  (or the green Run button ▶) after every step.
  6. Answer the questions in the Shell at the bottom and
     check that it says  ✔ saved as ...  with the type you expected.


── THE 10 STEPS ───────────────────────────────────────────

  Step 1   The name           str      input() · .strip() · .title()
  Step 2   The level          int      int() · while · .isdigit()
  Step 3   The speed          float    float()
  Step 4   Magic?             bool     == makes True / False
  Step 5   The backpack       list     for loop · append
  Step 6   Home on the map    tuple    random.randint
  Step 7   A pet?             None     None until we get a name
  Step 8   Stats              dict     values of different types
  Step 9   The Hero Card      all!     loop through a dict
  Step 10  Level up!          all!     math · str() · len()


── TESTING CHECKLIST ──────────────────────────────────────

  ✅ Type five for the level → it asks again
  ✅ Type 2 for the speed → saved as float (2.0)
  ✅ Type Y (capital) for magic → still True
  ✅ Just press Enter for the pet → saved as NoneType
  ✅ Hero Card: every line shows its type
  ✅ Type fast for the speed → ValueError (why?)


── BONUS CHALLENGES ────────────────────────────────────────

  ⭐    Ask for a lucky number (int) and a favourite colour (str)
  ⭐    Show how many letters are in the hero's name with len()
  ⭐⭐   Make the speed safe so typing "fast" can't crash it
  ⭐⭐   A random title like "the Brave" with random.choice
  ⭐⭐⭐  Turn the hero into a class Hero with a level_up() method
  ⭐⭐⭐  Save the Hero Card to hero.txt (you'll need str()!)


═══════════════════════════════════════════════════════════
  Have fun!  🧙
═══════════════════════════════════════════════════════════
