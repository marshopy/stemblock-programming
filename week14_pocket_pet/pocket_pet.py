# ═══════════════════════════════════════════════════════════
#  🐾  POCKET PET  — Complete Version
#  Week 14  |  Level 2 Python  |  The Big Review
# ═══════════════════════════════════════════════════════════
#
#  Take care of a virtual pet for 5 days!
#  Each day you get 2 actions: feed, play, teach a trick, or sleep.
#  Keep your pet fed and happy — and teach it as many tricks
#  as you can.
#
#  EVERY Level 2 concept is in here:
#    variables & types · input · f-strings · if / elif / else
#    and / not · for + range · while · break · functions + return
#    lists · dictionaries · random · classes, objects, methods
#
#  Run it in Thonny with F5 and type your answers in the Shell.
# ═══════════════════════════════════════════════════════════

import random


# ── STEP 1: THE DATA ────────────────────────────────────────

MAX_DAYS = 5

# a DICTIONARY:  food → how much it fills
FOODS = {
    "apple": 2,
    "sandwich": 3,
    "pizza": 5,
}

# a LIST of tricks your pet can learn
TRICKS = ["sit", "roll over", "high five",
          "spin", "play dead"]


def keep_in_range(value):
    """Keep a stat between 0 and 10."""
    if value < 0:
        return 0
    elif value > 10:
        return 10
    else:
        return value


# ── STEP 2: THE PET CLASS ───────────────────────────────────

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5      # 10 = starving
        self.happiness = 5   # 10 = super happy
        self.energy = 5      # 10 = full of energy
        self.tricks = []     # tricks it has learned

    # ── STEP 3: SHOW STATUS ─────────────────────────────────
    def show_status(self):
        print(f"\n🐾 {self.name}")
        print(f"   Hunger:    {self.hunger}/10")
        print(f"   Happiness: {self.happiness}/10")
        print(f"   Energy:    {self.energy}/10")
        if len(self.tricks) == 0:
            print("   Tricks:    none yet")
        else:
            print("   Tricks:")
            for trick in self.tricks:
                print("     -", trick)

    # ── STEP 4: FEED ────────────────────────────────────────
    def feed(self, food):
        if food in FOODS:
            self.hunger = self.hunger - FOODS[food]
            print(f"{self.name} ate the {food}. Yum! 😋")
        else:
            print(f"{self.name} says no to {food}! 🤢")

    # ── STEP 5: PLAY & SLEEP ────────────────────────────────
    def play(self):
        if self.energy >= 2:
            self.energy = self.energy - 2
            self.happiness = self.happiness + 2
            self.hunger = self.hunger + 1
            print(f"{self.name} played fetch! 🎾")
        else:
            print(f"{self.name} is too tired. 😴")

    def sleep(self):
        self.energy = 10
        print(f"{self.name} took a long nap. 💤")

    # ── STEP 6: LEARN A TRICK ───────────────────────────────
    def learn_trick(self):
        trick = random.choice(TRICKS)
        if trick in self.tricks:
            print(f"Already knows {trick}!")
        else:
            self.tricks.append(trick)
            self.happiness = self.happiness + 1
            print(f"New trick: {trick}! 🌟")

    # ── STEP 7: END OF THE DAY ──────────────────────────────
    def end_of_day(self):
        self.hunger = self.hunger + 1
        self.happiness = self.happiness - 1
        # keep every stat between 0 and 10
        self.hunger = keep_in_range(self.hunger)
        self.happiness = keep_in_range(self.happiness)
        self.energy = keep_in_range(self.energy)

    def is_ok(self):
        return self.hunger < 10 and self.happiness > 0


# ── STEP 8: THE MENU & MAKING OUR PET ───────────────────────

def show_menu():
    print("\nWhat do you want to do?")
    print("  1 - Feed")
    print("  2 - Play")
    print("  3 - Teach a trick")
    print("  4 - Sleep")


name = input("What is your pet's name? ")
pet = Pet(name)
print(f"Say hi to {pet.name}! 👋")


# ── STEP 9: THE GAME LOOP ───────────────────────────────────

for day in range(1, MAX_DAYS + 1):
    print(f"\n☀️  ===== DAY {day} =====")
    pet.show_status()

    actions_left = 2
    while actions_left > 0:
        show_menu()
        choice = input("Choose 1-4: ")

        if choice == "1":
            print("Foods:", list(FOODS.keys()))
            food = input("Which food? ")
            pet.feed(food)
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.learn_trick()
        elif choice == "4":
            pet.sleep()
        else:
            print("Please type 1, 2, 3 or 4.")
            # a typo doesn't use up a turn
            actions_left = actions_left + 1

        actions_left = actions_left - 1

    pet.end_of_day()
    if not pet.is_ok():
        print(f"\n😢 Oh no! {pet.name} is not okay...")
        break


# ── STEP 10: GAME OVER ──────────────────────────────────────

print("\n🏁 ===== GAME OVER =====")
pet.show_status()
print(f"\nYou looked after {pet.name} for {day} days")
print(f"and taught them {len(pet.tricks)} trick(s)!")

if pet.happiness >= 7 and len(pet.tricks) >= 3:
    print("⭐⭐⭐  Best pet owner ever!")
elif pet.happiness >= 4:
    print("⭐⭐  Great job!")
else:
    print("⭐  Your pet needs more love — play again!")
