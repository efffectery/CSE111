import math
num_of_items = int(input("Enter the number of items: "))

num_of_items_per_box = int(input("Enter the number of items the user will pack per box: "))

num_of_boxes = math.ceil(num_of_items / num_of_items_per_box)

print(f"you will need {num_of_boxes} boxes for {num_of_items} packed into {num_of_items_per_box} per box")