import random
import json
from art import logo
from string import ascii_lowercase

# Reads the questions from 'quiz_questions.txt' and converts it into a dictionary
with open('quiz_questions.txt') as file:
    data = file.read()
questions_dict = json.loads(data)

num_questions = len(questions_dict)
questions = random.sample(list(questions_dict.items()), k=num_questions)

# Starts the quiz
num_correct = 0
print(logo)
for num, (question, alternatives) in enumerate(questions_dict.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f" {question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    # Checks whether the given answer is among the alternatives
    while (answer_label := input("\n Which answer do you choose? ")) not in labeled_alternatives:
        print(f"Please use one of these: {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]

    if answer == correct_answer:
        num_correct += 1
        print(f"  Your answer {answer!r} is correct. ✨ Congratulations! ✨")
    else:
        print(f"  The answer is {correct_answer!r}, not {answer!r}.")

print(f"\n You've got {num_correct} correct answer(s) out of {num} questions.")
