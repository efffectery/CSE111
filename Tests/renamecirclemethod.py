#python

class circle:
    radius = 0.0

    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def get_area(self):
        area = 3.1415 * self.radius * self.radius
        return area
    
    def get_diameter(self):
        diameter = self.radius * 2
        return diameter

    def get_curcumfrance(self):
        circum = 2 * 3.1415 * self.radius
        return circum


def main():

    my_circle = circle(9)
    print(f"Your radius is {my_circle.get_radius()}, Your Diamerter is {my_circle.get_diameter()}, Your Area is {my_circle.get_area()}, Your curcumfrance is {my_circle.get_curcumfrance()}.")


if __name__ == "__main__":
    main()