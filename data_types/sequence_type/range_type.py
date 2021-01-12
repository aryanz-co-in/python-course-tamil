# list, tuple, range  Sequence Types


# Example 1 : 0 to 9 CM range
ten_centimeters = range(10)
for cm in ten_centimeters:
    print(cm)

# Example 2 : 1 to 2 CM range
for km in range(1, 5):
    print(f"{km} km")

# Example 3 : Take range of the list and print item value
names = ["Bob", "Sam", "Leo"]
for i in range(len(names)):
    print(names[i])

