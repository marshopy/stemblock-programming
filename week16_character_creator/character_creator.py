# ═══════════════════════════════════════════════════════════
#  🧙  CHARACTER CREATOR  — Complete Version
#  Week 16  |  Level 2 Python  |  Data Types
# ═══════════════════════════════════════════════════════════
#
#  Build a game hero by answering questions in the Shell.
#  Every answer is saved with the RIGHT data type:
#
#    str · int · float · bool · list · tuple · None · dict
#
#  After each answer the program tells you which type it used.
#  At the end you get a Hero Card — and your hero levels up!
#
#  Run it in Thonny with F5 and type your answers in the Shell.
# ═══════════════════════════════════════════════════════════

import random


# ── STEP 1: THE NAME  (str) ─────────────────────────────────

def show_type(value):
    print(f"   ✔ saved as {type(value).__name__}")


name = input("Hero name? ")
name = name.strip().title()
show_type(name)


# ── STEP 2: THE LEVEL  (int) ────────────────────────────────

level_text = input("Level (1-10)? ")
while not level_text.isdigit():
    print("Whole numbers only, please!")
    level_text = input("Level (1-10)? ")
level = int(level_text)
show_type(level)


# ── STEP 3: THE SPEED  (float) ──────────────────────────────

speed = float(input("Speed (like 1.5)? "))
show_type(speed)


# ── STEP 4: MAGIC  (bool) ───────────────────────────────────

answer = input("Magic? (y/n) ")
has_magic = answer.lower() == "y"
show_type(has_magic)


# ── STEP 5: THE BACKPACK  (list) ────────────────────────────

backpack = []
for i in range(3):
    item = input(f"Backpack item {i + 1}? ")
    backpack.append(item)
show_type(backpack)


# ── STEP 6: HOME ON THE MAP  (tuple) ────────────────────────

x = random.randint(0, 9)
y = random.randint(0, 9)
home = (x, y)
print(f"Home sweet home: {home}")
show_type(home)


# ── STEP 7: A PET?  (None) ──────────────────────────────────

pet = None
pet_name = input("Pet? (Enter for none) ")
if pet_name != "":
    pet = pet_name
show_type(pet)


# ── STEP 8: STATS  (dict) ───────────────────────────────────

stats = {
    "health": level * 10,
    "power": speed * 2,
    "magic": has_magic,
}
show_type(stats)


# ── STEP 9: THE HERO CARD ───────────────────────────────────

hero = {
    "name": name,
    "level": level,
    "speed": speed,
    "magic": has_magic,
    "backpack": backpack,
    "home": home,
    "pet": pet,
    "stats": stats,
}

print("\n🧙 ===== HERO CARD =====")
for key in hero:
    value = hero[key]
    kind = type(value).__name__
    print(f"{key}: {value}   ({kind})")


# ── STEP 10: LEVEL UP! ──────────────────────────────────────

print(f"\n⬆️  {name} LEVELS UP!")
level = level + 1
speed = round(speed * 1.25, 2)
stats["health"] = stats["health"] + 10
backpack.append("golden key")

print("Level: " + str(level))
print(f"Speed: {speed}")
print(f"Health: {stats['health']}")
print(f"Backpack: {len(backpack)} items")
