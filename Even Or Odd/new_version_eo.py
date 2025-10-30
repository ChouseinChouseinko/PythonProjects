import csv
import os


def check_even_numbers(num_list):
    return [n for n in num_list if n % 2 == 0]


def check_odd_numbers(num_list):
    return [n for n in num_list if n % 2 != 0]


def show_stats(all_batches):
    total_numbers = sum(len(batch) for batch in all_batches)
    all_numbers = [n for batch in all_batches for n in batch]
    if not all_numbers:
        print("No numbers available for stats.")
        return

    evens = check_even_numbers(all_numbers)
    odds = check_odd_numbers(all_numbers)

    print("\n===== STATISTICS =====")
    print(f"Total numbers entered: {total_numbers}")
    print(f"Even numbers: {len(evens)}")
    print(f"Odd numbers: {len(odds)}")
    if evens:
        print(f"Highest even number: {max(evens)}")
        print(f"Lowest even number: {min(evens)}")
    if odds:
        print(f"Highest odd number: {max(odds)}")
        print(f"Lowest odd number: {min(odds)}")
    print("=======================\n")


def save_to_csv(all_batches, filename="numbers.csv"):
    """Save each batch to CSV, separated by a blank line."""
    if not all_batches:
        print("No numbers to save!")
        return
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Numbers"])  # header
            for batch in all_batches:
                for number in batch:
                    writer.writerow([number])
                writer.writerow([])  # blank row to separate batches
        print(f"Numbers saved successfully to {filename}")
    except Exception as e:
        print("Error saving file:", e)


def main():
    all_batches = []

    while True:
        print("\n===== MENU =====")
        print("1. Add and check numbers")
        print("2. See all batches")
        print("3. See stats")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ").strip()

        if choice == "1":
            user_input = input("Enter numbers separated by commas: ")
            try:
                new_numbers = [int(x.strip()) for x in user_input.split(",")]
                all_batches.append(new_numbers)  # store as a new batch
                print("Even numbers in this batch:",
                      check_even_numbers(new_numbers))
                print("Odd numbers in this batch:",
                      check_odd_numbers(new_numbers))
            except ValueError:
                print("Please enter only valid integers separated by commas.")

        elif choice == "2":
            if not all_batches:
                print("No numbers stored yet.")
            else:
                print("\n===== All Batches =====")
                for i, batch in enumerate(all_batches, start=1):
                    print(f"Batch {i}: {batch}")
                print("=======================\n")

        elif choice == "3":
            show_stats(all_batches)

        elif choice == "4":
            filename = input(
                "Enter a filename (default: numbers.csv): ").strip() or "numbers.csv"
            save_to_csv(all_batches, filename)

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
