# ═══════════════════════════════════════════════════════════
#  🐾  POCKET PET  — Starter File
#  Week 14  |  Level 2 Python  |  The Big Review
# ═══════════════════════════════════════════════════════════
#
#  We build this program TOGETHER, one step at a time.
#  Follow the slides and type the code under each STEP heading.
#
#  💡 Tips:
#    • Type it yourself — don't copy and paste. Your fingers learn too!
#    • Watch your indentation (4 spaces).  Steps 3–7 go INSIDE the class.
#    • Press F5 after each step to check for errors.
#    • Stuck?  Compare with your neighbour, then put your hand up.
# ═══════════════════════════════════════════════════════════

import random


# ── STEP 1: THE DATA ────────────────────────────────────────
#   • MAX_DAYS = 5
#   • FOODS dictionary:  food name → how much it fills the pet
#   • TRICKS list:  5 tricks the pet can learn
#   • keep_in_range(value) function:  keeps a number between 0 and 10



# ── STEP 2: THE PET CLASS ───────────────────────────────────
#   class Pet:  with  __init__(self, name)
#   Give every pet:  name, hunger, happiness, energy, tricks = []



    # ── STEP 3: SHOW STATUS  (inside the class — indent 4 spaces!) ──
    #   def show_status(self):   print every stat with an f-string,
    #                            then loop through self.tricks



    # ── STEP 4: FEED  (inside the class) ──
    #   def feed(self, food):   if food is in FOODS, lower hunger



    # ── STEP 5: PLAY & SLEEP  (inside the class) ──
    #   def play(self):    only if energy >= 2
    #   def sleep(self):   energy back to 10



    # ── STEP 6: LEARN A TRICK  (inside the class) ──
    #   def learn_trick(self):   random.choice(TRICKS), then append



    # ── STEP 7: END OF THE DAY  (inside the class) ──
    #   def end_of_day(self):   hunger up, happiness down
    #   def is_ok(self):        return True if the pet is okay



# ── TEST AREA (after Step 3) ────────────────────────────────
#   pet = Pet("Mochi")
#   pet.show_status()
#   (Delete these test lines when you start Step 8.)



# ── STEP 8: THE MENU & MAKING OUR PET  (back at the left edge — no indent) ──
#   • show_menu() function
#   • ask for the pet's name with input(), then make the Pet object



# ── STEP 9: THE GAME LOOP ───────────────────────────────────
#   • for day in range(...):
#         while actions_left > 0:
#             if / elif / else  for the 4 choices



# ── STEP 10: GAME OVER ──────────────────────────────────────
#   • show the final status and a star rating with if / elif / else
