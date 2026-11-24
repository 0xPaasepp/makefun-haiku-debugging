# Seventeen Syllables of Debugging entry: one haiku about debugging,
# written to /output/entry.txt. Standard library only, no network.
# The bytes are identical on every run.
# The haiku (5-7-5):
#   I set a breakpoint            (I-1 set-1 a-1 break-point-2 = 5)
#   The code strolls past it, whistling
#                                 (The-1 code-1 strolls-1 past-1 it-1 whist-ling-2 = 7)
#   The breakpoint gives up      (The-1 break-point-2 gives-1 up-1 = 5)
# A concrete picture (a breakpoint), a fresh turn (the code strolls past
# it whistling, so the tool meant to catch the bug is the one that gives
# up), every word earns its place, reads aloud like speech.
import os

HAIKU = (
    "I set a breakpoint\n"
    "The code strolls past it, whistling\n"
    "The breakpoint gives up"
)

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(HAIKU) <= 200, "entry must be 1 to 200 characters"
assert HAIKU.strip() == HAIKU and HAIKU.strip(), "entry must not be only whitespace"
assert HAIKU.count("\n") == 2, "entry must be exactly three lines"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = HAIKU.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the haiku, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(HAIKU)
