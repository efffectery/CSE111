import csv


def read_dictionary(filename):
    student_dict = {}
    with open(filename, newline='') as students_csv:
        reader = csv.reader(students_csv)
        student_list = list(reader)
        del student_list[0]
        for student in student_list:
            student_dict[student[0]] = student[1]
    return student_dict

def main():
    student_dict = read_dictionary("students.csv")
    try:
        requested_id = input("Please Enter The INumber: ")
        print(f"For INumber {requested_id}: Student Name = {student_dict[requested_id]}")
    except KeyError as key:
        print(f"There is no student for key {key}")


if __name__ == "__main__":
    main()
