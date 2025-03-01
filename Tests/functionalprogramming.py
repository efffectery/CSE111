def main():
    students = [
    ["Robert", "Smith", 6.7],
    ["Annie", "Smith", 6.2],
    ["Robert", "Lopez", 7.1],
    ["Sean", "Li", 5.6],
    ["Sofia", "Lopez", 5.3],
    ["Lily", "Harris", 6.7],
    ["Alex", "Harris", 5.8],
    ["Billy", "Bob", 6.3],
    ["Jeannie", "Roberts", 5.9],
    ["Bubba", "Bob", 7.9],
    ["Lilly", "Smith", 4.9]]

    print_students(students)

    first_name_sorted = sorted(students, reverse=True)
    print_students(first_name_sorted)

    last_name_sorted = sorted(students, key= lambda x : x[1])
    print_students(last_name_sorted)

    reading_abil = sorted(students, key = lambda x : x[2], reverse=True)
    print_students(reading_abil)

def print_students(students):
    print("")
    for studnet in students:
        print(studnet)





if __name__ == "__main__":
    main()