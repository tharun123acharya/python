num = [1, 2, 3, 4, 6, 5, 4, 7, 8]

list2sorted = sorted(num)

num.reverse()
list2reverse = num

list2count = num.count(4)

num.extend([10, 11])
list2extend = num

num.insert(3, 9)
list2insert = num

num.pop(4)
list2pop = num

num.remove(3)
list2remove = num

num.clear()
list2clear = num

print("Sorted:", list2sorted)
print("Reversed:", list2reverse)
print("Count of 4:", list2count)
print("Extended:", list2extend)
print("Inserted:", list2insert)
print("After Pop:", list2pop)
print("After Remove:", list2remove)
print("Cleared:", list2clear)