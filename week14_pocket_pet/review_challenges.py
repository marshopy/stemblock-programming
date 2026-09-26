# ═══════════════════════════════════════════════════════════
#  🔑  WEEK 14 REVIEW — CHALLENGE ANSWERS  (teacher file)
#  Level 2 Python  |  The Big Review
# ═══════════════════════════════════════════════════════════
#
#  Every challenge from the slides, in order.  Press F5 in Thonny
#  to see the real output of each one — handy for showing the
#  class the answer after they've guessed.
#
#  (The debugging challenges are at the bottom as comments,
#   because they're SUPPOSED to crash!)
# ═══════════════════════════════════════════════════════════

import random


print("\n── 1. Variables & Types ──")
coins = 5
coins = coins + 3
coins = coins * 2
print(coins)

print("\n── 2. Input, Print & F-Strings ──")
a = "5"
b = "3"
print(a + b)
print(int(a) + int(b))

print("\n── 3. If / Elif / Else ──")
temp = 18
raining = False

if temp > 25:
    print("Beach")
elif temp > 15 and not raining:
    print("Park")
else:
    print("Movies")

print("\n── 4. For Loops & range() ──")
total = 0
for i in range(1, 5):
    total = total + i
print(total)

print("\n── 5. While Loops & break ──")
x = 1
while x < 20:
    x = x * 2
print(x)

print("\n── 6. Functions & Return ──")
def add_bonus(score):
    return score + 10

result = add_bonus(5) + add_bonus(1)
print(result)

print("\n── 7. Scope & Global ──")
lives = 3

def lose_life():
    global lives
    lives = lives - 1

lose_life()
lose_life()
print(lives)

print("\n── 8. Lists ──")
pets = ["cat", "dog", "fish"]
pets.append("bird")
pets.remove("dog")
print(pets[1], len(pets))

print("\n── 9. Dictionaries ──")
player = {"name": "Sam", "score": 0}
player["score"] = player["score"] + 5
player["level"] = 2
print(player["score"], len(player))

print("\n── 10. Tracing Code ──")
scores = {"Ana": 7, "Ben": 4, "Cy": 9}
winners = []

for name in scores:
    if scores[name] > 5:
        winners.append(name)

print(winners)
print(len(winners))

print("\n── 11. Random  (run it a few times!) ──")
print(random.randint(1, 3))

print("\n── 12. Classes & Objects ──")
class Counter:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count = self.count + 1

c = Counter()
c.click()
c.click()
print(c.count)

print("\n── 13. Bonus: Inheritance ──")
# (uses the classes from the example on the slide)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Cat(Animal):        # Cat inherits!
    def speak(self):      # override
        print(self.name, "says meow")

tom = Cat("Tom")
rex = Animal("Rex")
tom.speak()
rex.speak()


# ── DEBUGGING: "Will this code work?" ─────────────────────
#  Remove the # from one bug at a time to see the real error.

# Bug 1  →  SyntaxError:  Use  ==  to compare:  if score == 10:
# score = 10
# if score = 10:
#     print("Ten!")

# Bug 2  →  TypeError:  Can't add text + number.  Use  f"Score: {score}"
# score = 10
# print("Score: " + score)

# Bug 3  →  IndentationError:  Indent the body 4 spaces
# def hello():
# print("hi")

# Bug 4  →  IndexError:  Only [0] and [1] exist.  Use  fruits[1]  or  fruits[-1]
# fruits = ["apple", "kiwi"]
# print(fruits[2])
