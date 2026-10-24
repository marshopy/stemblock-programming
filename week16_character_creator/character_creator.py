# ═══════════════════════════════════════════════════════════
#  🛡️  CRASH-PROOF CHARACTER CREATOR  — Complete Version
#  Week 16  |  Level 2 Python  |  Advanced Types,
#                                 Conversion & Validation
# ═══════════════════════════════════════════════════════════
#
#  Build a game hero — but this time the program NEVER crashes,
#  no matter what the player types.  Every answer is:
#
#    1. VALIDATED  — checked before we trust it
#    2. CONVERTED  — turned into the right type
#    3. STORED     — in an advanced type (set, tuple, nested dict)
#
#  At the end the program runs a TYPE CHECK on the hero,
#  then saves it as text and loads it back.
#
#  Run it in Thonny with F5 and type your answers in the Shell.
# ═══════════════════════════════════════════════════════════

import random


# ── STEP 1: ASK FOR A WHOLE NUMBER  (try / except) ──────────

def ask_int(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if low <= number <= high:
                return number
            print(f"   ✖ Pick from {low} to {high}")
        except ValueError:
            print("   ✖ Whole numbers only!")


# ── STEP 2: ASK FOR A DECIMAL  (copy & change!) ─────────────

def ask_float(prompt, low, high):
    while True:
        try:
            number = float(input(prompt))
            if low <= number <= high:
                return number
            print(f"   ✖ Pick from {low} to {high}")
        except ValueError:
            print("   ✖ Numbers only!")


# ── STEP 3: ASK YES OR NO  (a set → a bool) ─────────────────

YES = {"y", "yes"}
NO = {"n", "no"}


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in YES:
            return True
        if answer in NO:
            return False
        print("   ✖ Please answer y or n")


# ── STEP 4: ASK FOR A NAME  (checking text) ─────────────────

def ask_name(prompt):
    while True:
        name = input(prompt).strip()
        letters = name.replace(" ", "")
        if letters.isalpha() and len(name) <= 12:
            return name.title()
        print("   ✖ Letters only, 12 or fewer")


# ── STEP 5: ASK THE QUESTIONS ───────────────────────────────

name = ask_name("Hero name? ")
level = ask_int("Level (1-10)? ", 1, 10)
speed = ask_float("Speed (0.5-5)? ", 0.5, 5)
has_magic = ask_yes_no("Magic? (y/n) ")


# ── STEP 6: SKILLS  (text → list → set) ─────────────────────

line = input("Skills, split by commas? ")
skills = set()
for word in line.split(","):
    word = word.strip().lower()
    if word != "":
        skills.add(word)
print(f"   ✔ {len(skills)} unique skills")


# ── STEP 7: HOME  (tuple + unpacking) ───────────────────────

home = (random.randint(0, 9),
        random.randint(0, 9))
x, y = home
print(f"   ✔ Home at x={x}, y={y}")


# ── STEP 8: THE HERO  (nested dict) ─────────────────────────

hero = {
    "name": name,
    "level": level,
    "speed": speed,
    "magic": has_magic,
    "skills": skills,
    "home": home,
    "stats": {
        "hp": level * 10,
        "power": speed * 2,
    },
}
print(f"\n🧙 {name}: HP {hero['stats']['hp']}")


# ── STEP 9: TYPE CHECK  (isinstance) ────────────────────────

EXPECTED = {
    "name": str,    "level": int,
    "speed": float, "magic": bool,
    "skills": set,  "home": tuple,
    "stats": dict,
}

print("\n🛡️  TYPE CHECK")
for key in EXPECTED:
    kind = EXPECTED[key]
    if isinstance(hero[key], kind):
        print(f"   ✔ {key}: {kind.__name__}")
    else:
        print(f"   ✖ {key}: NOT {kind.__name__}")


# ── STEP 10: SAVE & LOAD  (convert to text and back) ────────

saved = f"{name}|{level}|{speed}|{has_magic}"
print("\n💾 Saved as text:", saved)

parts = saved.split("|")
loaded_level = int(parts[1])
loaded_speed = float(parts[2])
loaded_magic = parts[3] == "True"
print("📂 Loaded back:")
print(loaded_level, loaded_speed, loaded_magic)
