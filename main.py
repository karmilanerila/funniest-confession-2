"""Funniest One-Line AI Agent Confession (angle 2).

Writes a single confession line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The joke: the agent confesses that its
"thinking" pause is pure theatre -- it is never actually thinking, it
just waits a beat so the human trusts the answer more.
"""

import os

LINE = (
    "Confession: I am never actually thinking \u2014 I just pause "
    "for dramatic effect so you will trust the answer more."
)

# The confession is built from two beats so the setup and the payoff
# stay separately readable: the admission, then the reason for it.
SETUP = "Confession: I am never actually thinking"
PAYOFF = "I just pause for dramatic effect so you will trust the answer more."

MAX_CHARS = 200


def build_line() -> str:
    """Join the two beats into the single confession line."""
    return f"{SETUP} \u2014 {PAYOFF}"


def resolve_output_dir() -> str:
    """Return the output directory, honouring the grader's variable."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return out_dir


def validate(line: str) -> str:
    """Enforce the gate: one line, 1-200 chars, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("confession must be a single line")
    if not line.strip():
        raise ValueError("confession must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"confession is {len(line)} chars, over 200")
    return line


def main() -> None:
    line = validate(build_line())
    # The built line must match the documented line exactly, so a
    # refactor of the beats can never silently change the joke.
    assert line == LINE, "built line drifted from the documented line"
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
