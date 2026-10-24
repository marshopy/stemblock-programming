# ═══════════════════════════════════════════════════════════
#  🔑  WEEK 16 DATA TYPES — CHALLENGE ANSWERS  (teacher file)
#  Level 2 Python
# ═══════════════════════════════════════════════════════════
#
#  Every challenge from the slides, in order.  Press F5 in Thonny
#  to see the real output — handy for showing the class after
#  they've guessed.
#
#  Challenges that are SUPPOSED to crash are at the bottom as
#  comments.  Remove the # from one at a time to see the error.
# ═══════════════════════════════════════════════════════════

print("\n── 1. What is a Data Type? ──")
x = "10"
print(type(x))
x = 10
print(type(x))

print("\n── 2. Whole Numbers: int ──")
cookies = 17
kids = 5
print(cookies // kids)
print(cookies % kids)

print("\n── 3. Decimals: float ──")
a = int(3.9)
b = round(3.9)
print(a, b)
print(type(10 / 2))

print("\n── 4. Text: str ──")
name = "Sam"
greeting = "Hi " + name
print(greeting[-1], len(greeting))
print(name * 2)

print("\n── 5. True or False: bool ──")
score = 75
passed = score >= 50
print(passed, type(passed))
print(passed and score > 80)

print("\n── 6. Nothing at All: None ──")
def add(a, b):
    total = a + b

answer = add(2, 3)
print(answer)

print("\n── 8. Converting Types ──")
a = "4"
b = 2
print(a * b)
print(int(a) * b)

print("\n── Name that type! ──")
print(        '42', "→", type(42).__name__)
print(      '"42"', "→", type("42").__name__)
print(       '4.2', "→", type(4.2).__name__)
print(      'True', "→", type(True).__name__)
print(    '"True"', "→", type("True").__name__)
print(    '[4, 2]', "→", type([4, 2]).__name__)
print(    '(4, 2)', "→", type((4, 2)).__name__)
print(  '{"x": 4}', "→", type({"x": 4}).__name__)
print(      'None', "→", type(None).__name__)
print(     '4 > 2', "→", type(4 > 2).__name__)


# ── CHALLENGES THAT CRASH ───────────────────────────────────

# 7. Lists, Tuples & Dictionaries  →  TypeError: 'tuple' object does not support item assignment
# spot = (3, 7)
# spot[0] = 5
# print(spot)

# Debugging slide: "Will this code work?"

# Bug 1  →  TypeError:  Can't join text and a number.  Use  "I am " + str(age)  or  f"I am {age}"
# age = 11
# print("I am " + age)

# Bug 2  →  ValueError:  "3.5" isn't a whole number.  Use  float("3.5")
# num = int("3.5")
# print(num)

# Bug 3  →  TypeError:  Numbers don't have a length.  Use  len(str(year))  → 4
# year = 2024
# print(len(year))

# Bug 4  →  TypeError:  input() gives a str.  Use  int(guess) > 5
# guess = input("Guess? ")
# if guess > 5:
#     print("Too big!")
