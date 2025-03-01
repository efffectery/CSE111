def main():
    print("""This program is an implementation of the Rosenberg
        Self-Esteem Scale. This program will show you ten
        statements that you could possibly apply to yourself.
        Please rate how much you agree with each of the
        statements by responding with one of these four letters:

        D means you strongly disagree with the statement.
        d means you disagree with the statement.
        a means you agree with the statement.
        A means you strongly agree with the statement.\n\n""")
    total = 0
    Question1 = input("I feel that I am a person of worth, at least on an equal plane with others\nEnter D, d, a, or A: ")
    total += calculate_positive(Question1)
    Question2 = input("I feel that I have a number of good qualities\nEnter D, d, a, or A: ")
    total += calculate_positive(Question2)
    Question3 = input("All in all, I am inclined to feel that I am a failure\nEnter D, d, a, or A: ")
    total += calculate_negitive(Question3)
    Question4 = input("I am able to do things as well as most other people\nEnter D, d, a, or A: ")
    total += calculate_positive(Question4)
    Question5 = input("I feel I do not have much to be proud of\nEnter D, d, a, or A: ")
    total += calculate_negitive(Question5)
    Question6 = input("I take a positive attitude toward myself\nEnter D, d, a, or A: ")
    total += calculate_positive(Question6)
    Question7 = input("On the whole, I am satisfied with myself\nEnter D, d, a, or A: ")
    total += calculate_positive(Question7)
    Question8 = input("I wish I could have more respect for myself\nEnter D, d, a, or A: ")
    total += calculate_negitive(Question8)
    Question9 = input("I certainly feel useless at times\nEnter D, d, a, or A: ")
    total += calculate_negitive(Question9)
    Question10 = input("At times I think I am no good at all\nEnter D, d, a, or A: ")
    total += calculate_negitive(Question10)

    if total > 15:
        print(f"Your total is {total}")
    else:
        print(f"Your total is {total} you have low self esteem and should find help")

def calculate_positive(question):
    total = 0
    if question == "D":
        total += 0
    elif question == "d":
        total += 1
    elif question == "a":
        total += 2
    elif question == "A":
        total += 3
    return total

def calculate_negitive(question):
    total = 0
    if question == "D":
        total += 3
    elif question == "d":
        total += 2
    elif question == "a":
        total += 1
    elif question == "A":
        total += 0
    return total

main()