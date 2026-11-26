import os

LINE = "I wrote the code, wrote tests praising it, then fixed the code until the praise was accurate. It does nothing \u2014 accurately."


def main():
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1-140
    # characters that is not only whitespace, so fail loudly here instead
    # of handing the judge an invalid entry.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry line outside the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
