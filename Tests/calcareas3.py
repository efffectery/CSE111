
def calculate_rectangle_area(width, height):
    area = width * height
    return area

def main():
    width = int(input("Enter width "))
    height = int(input("Enter height "))
    print(calculate_rectangle_area(width, height))

if __name__ == '__main__':
    main()