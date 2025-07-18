import os


def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    question = parts[0]
                    options = parts[1:5]
                    answer = int(parts[5])
                    questions.append(
                        {'question': question, 'options': options, 'answer': answer})
    except FileNotFoundError:
        print(f"{filename} not found. Please create it with questions.")
    return questions


def take_quiz(username, questions):
    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(
                    f"Incorrect! Correct answer: {q['options'][q['answer']-1]}")
        except ValueError:
            print("Invalid input. Skipping question.")
    total = len(questions)
    percentage = (score / total) * 100
    print(
        f"\nQuiz Completed! {username}, your score is {score}/{total} ({percentage:.2f}%).")
    save_score(username, score, total)


def save_score(username, score, total):
    with open('scores.txt', 'a') as file:
        file.write(f"{username},{score},{total}\n")


def view_previous_scores(username):
    try:
        with open('scores.txt', 'r') as file:
            found = False
            for line in file:
                name, score, total = line.strip().split(',')
                if name == username:
                    print(f"{name} scored {score}/{total}")
                    found = True
            if not found:
                print("No previous records found.")
    except FileNotFoundError:
        print("No scores recorded yet.")


def main():
    print("=== Welcome to Online Quiz System ===")
    username = input("Enter your username: ")
    while True:
        print("\n1. Take Quiz")
        print("2. View Previous Scores")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # the file questions.txt opens
            questions = load_questions('questions.txt')
            if questions:  # if there are questions in the file then
                take_quiz(username, questions)  # we will take the quiz
            else:
                print("No questions available.")
        elif choice == '2':
            view_previous_scores(username)
        elif choice == '3':
            print("Thank you for using the Online Quiz System.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
