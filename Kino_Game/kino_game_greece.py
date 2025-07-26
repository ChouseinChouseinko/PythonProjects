import random  # θα επιλεξουμε τυχαια τους αριθμους
# δημιουργουμε μια λιστα αποτελουμενοι απο αριθμου 1 εως 80
kino_range = list(range(1, 81))

# τωρα θα δημιουργησουμε μια λιστα με 20 αριθμους τα οποια θα τα επιλεξουμε τυχαια
kino_draw = random.sample(kino_range, 20)
kino_draw.sort()
print("The winning numbers are: ", kino_draw)

# τωρα θα ζητησουμε απο τον χρηστη να εισαγει 1 εως 12 αριθμους


def get_user_numbers():
    while True:
        try:
            user_input = input("Select 1 to 12 unique numbers: ")
            user_numbers = list(map(int, user_input.strip().split()))
            if len(user_numbers) < 1 or len(user_numbers) > 12:
                raise ValueError("You must select between 1 and 12 numbers.")
            if any(n < 1 or n > 80 for n in user_numbers):
                raise ValueError("Numbers must be between 1 and 80.")
            if len(set(user_numbers)) != len(user_numbers):
                raise ValueError("Numbers must be unique.")
            return sorted(user_numbers)
        except ValueError as e:
            print("⚠️ Error:", e)

# Συγκριση τους αριθμους του χρηστη με τους αριθμους που επιλεχθηκαν τυχαια


def compare(user_numbers, kino_draw):
    matches = set(user_numbers) & set(kino_draw)
    print(f"✅ Your Numbers: {user_numbers}")
    print(f"🎯 Matches: {sorted(matches)} ({len(matches)} hits)")


def main():
    print("🎰 Welcome to the KINO Number Generator!")
    user_numbers = get_user_numbers()
    kino_draw = random.sample(kino_range, 20)
    kino_draw.sort()
    print("🎲 KINO Winning Numbers:", kino_draw)

    compare(user_numbers, kino_draw)


if __name__ == "__main__":
    main()
