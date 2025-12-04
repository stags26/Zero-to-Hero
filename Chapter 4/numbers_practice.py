for numbers in range(1,21):
    print(numbers)

million = list(range(1,1000001))
print(million)

mini = min(million)
print(mini)
last = max(million)
print(last)
adding = sum(million)
print(adding)

for number in range(1,21,2):
    print(number)

for threes in range(3,31,3):
    print(threes)

for cubes in range(1,11):
    cube = cubes**3
    print(cube)

cube_list = []
for cubic in range(1,11):
    cube_list.append(cubic**3)
print(cube_list)

cubes_list = [cube ** 3 for cube in range(1,11)]
print(cubes_list)