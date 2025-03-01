
# Recursion in python
# def f(x):
#     print(x)
#     if x == 1:
#         print("functional")
#     else:
#         f(x - 1)

# f(10)


#Passing functions as parameters


# def f_c(f):
#     c = (f - 32) * 5 / 9
#     return c

# def c_f(c):
#     f = c * 9 / 5 + 32
#     return f


# def pro_temp(function, temps):
#     new_temps = []
#     for temp in temps:
#         t = function(temp)
#         new_temps.append(t)
    
#     return new_temps

# def main():
#     temputeaters = [-10, -100, -23, 0, 32, 100, 212]
#     # print(temputeaters)

#     # temp = pro_temp(f_c, temputeaters)
#     # print(temp)
#     # c_temps = pro_temp(c_f, temp)
#     # print(c_temps)

#     temp = list(map(f_c, temputeaters))
#     print(temp)

#     temp = list(map(lambda f: (f - 32) * 5 / 9 , temputeaters))
#     print(temp)

#     numbers = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
#     even_numbers  = list(filter(lambda n: n % 2, numbers))
#     print(even_numbers)

# if __name__ == "__main__":
#     main()