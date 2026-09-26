═══════════════════════════════════════════════════════════
  🐾  POCKET PET  —  README
  Week 14  |  Level 2 Python  |  The Big Review
═══════════════════════════════════════════════════════════


── WHAT IS THIS? ──────────────────────────────────────────

  Week 14 is a review of EVERYTHING in Level 2, made for
  new students and returning students together.

    Part 1  —  Concept review: 14 quick "what's the print
               value?" challenges, variables → classes
    Part 2  —  We build Pocket Pet together, step by step

  Pocket Pet is a text game that runs in the Thonny Shell.
  You look after a virtual pet for 5 days.  Each day you get
  2 actions: feed, play, teach a trick, or sleep.  Keep your
  pet fed and happy, and teach it as many tricks as you can!


── FILES IN THIS FOLDER ───────────────────────────────────

  pocket_pet_starter.py  ← STUDENT FILE  (open this in Thonny!)
                            Only has the step headings.
                            We type the code together from the slides.

  pocket_pet.py          ← COMPLETE VERSION
                            The finished game.  Run it at the start
                            of class to show what we're building.

  review_challenges.py   ← TEACHER FILE
                            Every Part 1 challenge — press F5 to see
                            the real answers.

  teacher_notes.txt      ← TEACHER NOTES  (timing, answers, tips)

  README.txt             ← THIS FILE

  The slides are in  week14_Level2_Review.pptx


── HOW TO OPEN IN THONNY ──────────────────────────────────

  1. Open Thonny on your computer.
  2. Click  File  →  Open...
  3. Select  pocket_pet_starter.py
  4. Type the code for each step from the slides.
  5. Press  F5  (or the green Run button ▶) after every step.
  6. The game talks to you in the Shell at the bottom —
     type your answers there and press Enter.


── THE 10 STEPS ───────────────────────────────────────────

  Step 1   The data              variables · dictionary · list · function
  Step 2   The Pet class         class · __init__ · self
  Step 3   Show status           method · f-strings · for loop
  Step 4   Feed                  parameter · dictionary lookup · in
  Step 5   Play & sleep          if / else · >=
  Step 6   Learn a trick         random.choice · list.append
  Step 7   End of the day        return · and
  Step 8   Menu & making our pet input() · making an object
  Step 9   The game loop         for + range · while · if / elif / else · break
  Step 10  Game over             if / elif / else · len()


── TESTING CHECKLIST ──────────────────────────────────────

  ✅ Feed pizza → hunger goes down
  ✅ Feed "rocks" → your pet says no
  ✅ Play 3 times in a row → "too tired"
  ✅ Type 9 at the menu → "Please type 1, 2, 3 or 4" (no turn lost)
  ✅ Teach tricks → the trick list grows
  ✅ Only sleep for 5 days → your pet is not okay!


── BONUS CHALLENGES ────────────────────────────────────────

  ⭐    Add a new food to FOODS and a new trick to TRICKS
  ⭐⭐   Add a 5th action: give your pet a bath 🛁
        (new stat: cleanliness)
  ⭐⭐   A random surprise every morning with random.randint
  ⭐⭐⭐  Two pets!  Keep them in a list and take turns
  ⭐⭐⭐  class Dog(Pet) with its own play() method (inheritance!)


═══════════════════════════════════════════════════════════
  Have fun!  🐾
═══════════════════════════════════════════════════════════
