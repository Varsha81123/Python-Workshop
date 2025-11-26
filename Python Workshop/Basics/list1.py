
items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original List:", items)
items.append(110)
print("After append(110):", items)
items.remove(40)
print("After remove(40):", items)
items.insert(2, 25)    
print("After insert(2, 25):", items)
popped_item = items.pop()
print("After pop():", items)
print("Popped item:", popped_item)
