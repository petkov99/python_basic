length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_of_aquarium = length * width * height
volume_in_lt = volume_of_aquarium / 1000
used_space = volume_in_lt * (percentage / 100)
results = volume_in_lt - used_space

print(results)

