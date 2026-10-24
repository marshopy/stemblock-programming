# ═══════════════════════════════════════════════════════════
#  🔑  WEEK 16 — CHALLENGE ANSWERS  (teacher file)
#  Level 2 Python  |  Advanced Types, Conversion & Validation
# ═══════════════════════════════════════════════════════════
#
#  Every challenge from the slides, in order.  Press F5 in Thonny
#  to see the real output — handy for showing the class after
#  they've guessed.
#
#  Bugs that are SUPPOSED to crash are at the bottom as comments.
#  Remove the # from one at a time to see the real error.
# ═══════════════════════════════════════════════════════════

print("\n── 1. Tuples: Pack & Unpack ──")
hero = ("Ava", 5, 1.5)
name, level, speed = hero
print(level + 1, name)
print(len(hero), type(hero).__name__)

print("\n── 2. Sets: No Duplicates ──")
votes = ["cat", "dog", "cat",
         "fish", "dog"]
unique = set(votes)
print(len(votes), len(unique))
print("bird" in unique)

print("\n── 3. Nested Data ──")
bag = {"food": ["apple"], "gold": 12}
bag["food"].append("cheese")
print(len(bag["food"]), bag["food"][-1])
print(type(bag["gold"]).__name__)

print("\n── 4. Converting Numbers & Text ──")
a = "8"
b = 2.5
print(int(a) + b)
print(a * 2, str(b) + "!")

print("\n── 5. Converting Collections ──")
line = "red,blue,red,green"
words = line.split(",")
print(len(words), len(set(words)))
print(words[-1].upper())

print("\n── 6. Truthy & Falsy ──")
print(bool("False"))
print(bool("0"), bool(0))
print(bool(" "))

print("\n── 7. Checking Types: isinstance() ──")
things = [7, "7", 7.0, [7], None]
count = 0
for t in things:
    if isinstance(t, (int, float)):
        count = count + 1
print(count)

print("\n── 8. Checking Text ──")
answers = ["12", "twelve", " 7 ", "3.5"]
for a in answers:
    print(a.strip().isdigit())

print("\n── 9. try / except ──")
for t in ["12", "x", "3.5", "7"]:
    try:
        print(int(t) * 2)
    except ValueError:
        print("oops")

print("\n── 10. The Validation Loop ──")
for a in ["ten", "25", "12"]:
    try:
        age = int(a)
        if 5 <= age <= 18:
            print("ok", age)
        else:
            print("out of range")
    except ValueError:
        print("not a number")

print("\n── Name that type! ──")
print(      '(3,)', "→", type((3,)).__name__)
print(       '(3)', "→", type((3)).__name__)
print(        '{}', "→", type({}).__name__)
print(     'set()', "→", type(set()).__name__)
print(    '{1, 2}', "→", type({1, 2}).__name__)
print(        '""', "→", type("").__name__)
print(      '[[]]', "→", type([[]]).__name__)
print(   '"3" * 2', "→", type("3" * 2).__name__)
print(   '3 > 2.0', "→", type(3 > 2.0).__name__)
print(  'int("7")', "→", type(int("7")).__name__)

print("\n── Bug 4  (no crash!): runs, but gives the WRONG answer ──")
answer = "no"
has_magic = bool(answer)
print(has_magic)


# ── BUGS THAT CRASH ("Will this code work?") ──────────────

# Bug 1  →  ValueError:  int() can't read a dot.  Use  int(float("3.5"))  (or just float)
# num = int("3.5")
# print(num)

# Bug 2  →  TypeError:  Sets have no order, so no [0].  Use  "fast" in tags  or a list
# tags = {"fast", "brave"}
# print(tags[0])

# Bug 3  →  ValueError:  Too many values to unpack.  Use  x, y, z = (4, 5, 6)
# x, y = (4, 5, 6)
# print(x, y)
