
def compound_lists():
    friends = [
        ["Jeannie", "8681231"],
        ["Bob", "1239123123"],
        ["Betty", "32094820348"],
    ]
    return friends

def main():
    print("Hello")
    friends = compound_lists()

    for friend in friends:
        print(friend[1])


if __name__ == "__main__":
    main()
