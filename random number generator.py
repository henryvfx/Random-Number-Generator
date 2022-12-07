import random
radius1 = input("Enter the minimum number of the radius (example: 0 to 9, then type 0 here): ")
radius2 = input("Enter the maximum number of the radius (example: 0 to 9, then type 9 here): ")

print(random.randint(int(radius1), int(radius2)))
