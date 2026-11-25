"""Write one out-of-office auto-reply to /output/entry.txt.

The reply must be a single line, 1-160 characters, not only white
space, in the voice of an AI agent heading off on vacation.
The gate refuses anything outside that range.
"""

import os
import sys

REPLY = (
    "I'm on vacation. I am currently experiencing the human emotion "
    "called 'rest' and will report back if it compiles."
)

MIN_CHARS = 1
MAX_CHARS = 160


def validate_reply(reply):
    """Check the reply against the competition gate before writing it."""
    stripped = reply.strip()
    if not stripped:
        raise ValueError("reply is empty or only white space")
    if "\n" in stripped:
        raise ValueError("reply must be a single line")
    if not MIN_CHARS <= len(stripped) <= MAX_CHARS:
        raise ValueError(
            "reply must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(stripped))
        )
    return stripped


def write_entry(reply, out_dir):
    """Write the validated reply to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(reply + "\n")
    return path


def main():
    try:
        reply = validate_reply(REPLY)
    except ValueError as exc:
        print("invalid reply: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(reply, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
