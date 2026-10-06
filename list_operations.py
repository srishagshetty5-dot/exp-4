integers = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 6, 61]

print("Original List:", integers)

print("Length of list:", len(integers))

integers.append(16)
print("After Append 16:", integers)

integers.insert(5, 40)
print("After Inserting:", integers)

integers.remove(10)
print("After Removing:", integers)

integers.pop(5)
print("After Popping:", integers)

print("Count:", integers.count(6))

print("Index:", integers.index(15))

# Slicing
print("First 5 elements:", integers[0:5])

# Last element
print("Last element:", integers[-1])

# Copy
x = integers.copy()
print("Copied List:", x)

# Extend
integers.extend(x)
print("After Extend:", integers)
