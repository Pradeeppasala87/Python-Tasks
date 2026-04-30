import copy

marks1 = [50, 60, 70, 80]
marks2 = copy.copy(marks1)
marks2[0] = 100

print("the changing one affect the other:",marks2)
