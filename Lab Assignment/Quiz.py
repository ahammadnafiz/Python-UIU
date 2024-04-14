import json
import random


def load_quiz(filename='questions.txt'):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading quiz: {e}")
        return None

def save_marks(student_id: int, score: int, filename='marks.txt'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if student_id not in data or score > data[student_id]:
        data[student_id] = score

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def review_answers(user_answers, incorrect_answers, score):
    print(f'Your total score: {score}')
    
    print('\nReview Incorrect Answers:')
    for incorrect_answer in incorrect_answers:
        print(f"\nQuestion: {incorrect_answer['question']}")
        print(f"Options: {', '.join(incorrect_answer['options'])}")
        print(f"Your Answer: {incorrect_answer['user_answer']}")
        print(f"Correct Answer: {incorrect_answer['correct_answer']}")

    print('\nScoring Breakdown:')
    print(f'Number of Correct Answers: {len(user_answers) - len(incorrect_answers)}')
    print(f'Number of Incorrect Answers: {len(incorrect_answers)}')


def take_quiz():
    quiz = load_quiz()

    if quiz is None:
        return

    original_order = list(range(len(quiz['questions'])))
    random.shuffle(original_order)

    student_id = input('Enter your student ID: ')

    # Validate that the student ID is provided
    while not student_id:
        print("Please enter a valid student ID.")
        student_id = input('Enter your student ID: ')

    score = 0
    user_answers = []
    incorrect_answers = []

    for question_index in original_order:
        question = quiz['questions'][question_index]
        options = quiz['options'][question_index]
        correct_answer = quiz['answers'][question_index]

        print(f'Question {original_order.index(question_index) + 1}: {question}')

        for option in options:
            print(f'{option}')

        user_ans = input('Enter your answer: ').lower()
        user_answers.append(user_ans)

        if user_ans == correct_answer:
            print('Correct')
            score += 2
        else:
            print('Incorrect')
            incorrect_answers.append({
                'question': question,
                'options': options,
                'user_answer': user_ans,
                'correct_answer': correct_answer
            })

    # After answering all questions, ask if the user wants to submit
    choice = input('Do you want to submit your answers? (yes/no): ').lower()
    if choice == 'yes':
        review_answers(user_answers, incorrect_answers, score)
        
    save_marks(student_id, score)
    # If the user chooses not to submit, the loop breaks
    print('Quiz session ended.')


def main():
    take_quiz()


if __name__ == "__main__":
    main()
