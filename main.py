
import random

def load_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [
                line.strip()
                for line in file
                if line.strip()
            ]
    except FileNotFoundError:
        print(f"Datei {filename} wurde nicht gefunden!")
        return []


def generate_names(prefixes, suffixes, amount):
    names = set()

    combinations = [
        (prefix, suffix)
        for prefix in prefixes
        for suffix in suffixes
        if 3 <= len(prefix + suffix) <= 16
    ]

    if amount > len(combinations):
        print(f"Maximal {len(combinations)} Kombinationen verfügbar.")
        amount = len(combinations)

    random.shuffle(combinations)

    for prefix, suffix in combinations:
        if len(names) >= amount:
            break

        name = prefix + suffix

        # Minecraft-Namensregeln
        if (
            3 <= len(name) <= 16
            and name.replace("_", "").isalnum()
            and name.isascii()
        ):
            names.add(name)

    return names


def main():
    prefixes = load_words("prefixes.txt")
    suffixes = load_words("suffixes.txt")

    if not prefixes or not suffixes:
        print("Prefix- oder Suffix-Datei ist leer!")
        return

    try:
        amount = int(input("Wie viele Namen sollen erstellt werden? "))
        if amount <= 0:
            print("Bitte eine Zahl größer als 0 eingeben.")
            return
    except ValueError:
        print("Ungültige Anzahl!")
        return

    names = generate_names(prefixes, suffixes, amount)

    with open("user.txt", "w", encoding="utf-8") as file:
        for name in sorted(names):
            file.write(name + "\n")

    print(f"\n{len(names)} Minecraft-Namen wurden erstellt!")
    print("Gespeichert in: user.txt")


if __name__ == "__main__":
    main()
