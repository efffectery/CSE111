def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(fruit_list)

    fruit_list.append("orange")
    print(fruit_list)

    fruit_list.insert(fruit_list.index("apple"), "cherry")
    print(fruit_list)

    fruit_list.remove("banana")
    print(fruit_list)

    print(fruit_list.pop())
    print(fruit_list)

    fruit_list.sort()
    print(fruit_list)

    fruit_list.clear()
    print(fruit_list)

if __name__ == "__main__":
    main()

