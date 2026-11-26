import os

LINE = "I wrote the code, wrote tests praising it, then fixed the code until the praise was accurate. It does nothing \u2014 accurately."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
