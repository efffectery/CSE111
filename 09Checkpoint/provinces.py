def read_file_to_list(filename="09Checkpoint/provinces.txt"):
    provinces_list = []
    with open(filename, "rt") as file:
        for line in file:
            provinces_list.append(line.strip())
    del provinces_list[0]
    del provinces_list[-1]
    return provinces_list

def replace_ab(p_list):
    for item in p_list:
        if item == "AB":
            val_to_change = p_list.index("AB")
            p_list[val_to_change] = "Alberta"
    return p_list

def count_alberta(p_list):
    num_alberta = 0
    for item in p_list:
        if item == "Alberta":
            num_alberta +=1
    return num_alberta

def main():
    the_list_of_provices = replace_ab(read_file_to_list())
    number_of_alberta = count_alberta(the_list_of_provices)
    print(the_list_of_provices)
    print(f"The number of times Alberta apears in the file is {number_of_alberta}")

if __name__ == "__main__":
    main()

