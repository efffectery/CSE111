import math

dict_per_can = [
    {"Name": "#1 Picnic", "Diameter": 6.83, "Height": 10.16, "Cost": 0.28},
    {"Name": "#1 Tall", "Diameter": 7.78, "Height": 11.91, "Cost": 0.43},
    {"Name": "#2", "Diameter": 8.73, "Height": 11.59, "Cost": 0.45},
    {"Name": "#2.5", "Diameter": 10.32, "Height": 11.91, "Cost": 0.61},
    {"Name": "#3 Cylinder", "Diameter": 10.79, "Height": 17.78, "Cost": 0.86},
    {"Name": "#5", "Diameter": 13.02, "Height": 14.29, "Cost": 0.83},
    {"Name": "#6Z", "Diameter": 5.40, "Height": 8.89, "Cost": 0.22},
    {"Name": "#8Z short", "Diameter": 6.83, "Height": 7.62, "Cost": 0.26},
    {"Name": "#10", "Diameter": 15.72, "Height": 17.78, "Cost": 1.53},
    {"Name": "#211", "Diameter": 6.83, "Height": 12.38, "Cost": 0.34},
    {"Name": "#300", "Diameter": 7.62, "Height": 11.27, "Cost": 0.38},
    {"Name": "#303", "Diameter": 8.10, "Height": 11.11, "Cost": 0.42}
]


def compute_volume(radius, height):
    volume = math.pi * (radius * radius) * height

    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    
    return surface_area


def storage_efficiency(volume, surface_area):
    storage_efficient = volume / surface_area

    return storage_efficient



def main():
    for can in dict_per_can:
        for key in can:
            name = can["Name"]
            radius = can["Diameter"]
            height = can["Height"]
            cost = can["Cost"]
        volume = round(compute_volume(radius, height), 2)
        surface_area = round(compute_surface_area(radius, height), 2)
        efficeiency = round(storage_efficiency(volume, surface_area), 2)
        print(f"For can {name}")
        print(f"The Volume is {volume}")
        print(f"The Surface Area is {surface_area}")
        print(f"The storage efficeniency is {efficeiency}\n")


main()


    


