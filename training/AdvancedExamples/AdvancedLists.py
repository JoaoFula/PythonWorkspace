# Working with advanced lists

nums = [1, 3, 4, 7, 8, 9]

# Find in which index is the number 4
print(nums.index(4))

# Delete list position 2
del nums[2]
print(nums)

# Insert the number 10 in index 1
nums.insert(1, 10)
print(nums)

# Insert a list whithin the list
nums.insert(0, [33, 44, 22])
print(nums)

# List is composed of the square of every even number up to 10 
nums = [x**2 for x in range(10) if x%2 == 0]
print(nums)