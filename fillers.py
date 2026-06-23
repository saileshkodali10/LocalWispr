import re


def clean_text(text):
    fillers = [
        "um",
        "uh",
        "you know",
        "like",
        "actually",
        "basically"
    ]

    # Remove fillers
    for filler in fillers:
        text = re.sub(
            rf"\b{re.escape(filler)}\b",
            "",
            text,
            flags=re.IGNORECASE
        )

    # Remove extra spaces
    text = " ".join(text.split())

    if not text:
        return ""

    # Fix standalone i -> I
    text = re.sub(r"\bi\b", "I", text)

    # Capitalize first letter
    text = text[0].upper() + text[1:]

    # Common names you frequently use
    names = [
        "sneha",
        "sailesh"
    ]

    for name in names:
        text = re.sub(
            rf"\b{name}\b",
            name.capitalize(),
            text,
            flags=re.IGNORECASE
        )

    # Remove duplicate punctuation
    text = re.sub(r"[.]{2,}", ".", text)
    text = re.sub(r"[?]{2,}", "?", text)
    text = re.sub(r"[!]{2,}", "!", text)

    # Add ending punctuation
    if not text.endswith((".", "!", "?")):
        text += "."

    return text


if __name__ == "__main__":
    sample = input("Enter text: ")
    print(clean_text(sample))