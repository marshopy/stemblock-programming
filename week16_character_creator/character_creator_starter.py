# ═══════════════════════════════════════════════════════════
#  🛡️  CRASH-PROOF CHARACTER CREATOR  — Starter File
#  Week 16  |  Level 2 Python  |  Advanced Types,
#                                 Conversion & Validation
# ═══════════════════════════════════════════════════════════
#
#  We build this program TOGETHER, one step at a time.
#  Follow the slides and type the code under each STEP heading.
#
#  Our goal: the program must NEVER crash, no matter what the
#  player types.  Every answer gets VALIDATED, then CONVERTED.
#
#  💡 Tips:
#    • Steps 1-4 make "validator" functions.  After pressing F5,
#      test each one by typing a call in the Shell, for example:
#          >>> ask_int("Level? ", 1, 10)
#    • Try to BREAK your code: type words, huge numbers, nothing.
#    • Steps 5-10 run from top to bottom like a normal program.
# ═══════════════════════════════════════════════════════════

import random


# ── STEP 1: ASK FOR A WHOLE NUMBER  (try / except) ──────────
#   def ask_int(prompt, low, high):
#   • keep asking (while True) until the answer is a whole number
#     between low and high, then return it as an int



# ── STEP 2: ASK FOR A DECIMAL  (copy & change!) ─────────────
#   def ask_float(prompt, low, high):
#   • copy ask_int and change int → float



# ── STEP 3: ASK YES OR NO  (a set → a bool) ─────────────────
#   • YES and NO sets of allowed answers
#   def ask_yes_no(prompt):  return True or False



# ── STEP 4: ASK FOR A NAME  (checking text) ─────────────────
#   def ask_name(prompt):
#   • letters only (spaces allowed), 12 characters or fewer



# ── STEP 5: ASK THE QUESTIONS ───────────────────────────────
#   • call your 4 validators to get name, level, speed, has_magic



# ── STEP 6: SKILLS  (text → list → set) ─────────────────────
#   • one line of text, split by commas, saved in a set



# ── STEP 7: HOME  (tuple + unpacking) ───────────────────────
#   • a tuple of two random numbers, unpacked into x and y



# ── STEP 8: THE HERO  (nested dict) ─────────────────────────
#   • one dictionary holding everything — with a dict inside it



# ── STEP 9: TYPE CHECK  (isinstance) ────────────────────────
#   • a dictionary of the type each value SHOULD be,
#     then check every one with isinstance()



# ── STEP 10: SAVE & LOAD  (convert to text and back) ────────
#   • turn the hero into one line of text, split it,
#     and convert each piece back to the right type
