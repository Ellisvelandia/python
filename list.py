users = ["Dave" , "Ellis", "chris"]

data = ["Ellis", 42, True]

emptylist = []

print("Ellis" in users)

print(users[0])

print(users.index('chris'))

print(users[0:2])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Maria")
print(users)

users[2:2] = ["Eddie", "Crisanto"]
print(users)

users[1:3] = ["Roo", "JPJ"]
print(users)

users.remove("Jason")
print(users)

print(users.pop())

del data[0]
print(data)

data.clear()
print(data)

users[1:2] = ['ellis']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,15,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))
print(sorted(nums, reverse=False))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1 , "Neil" , True])
print(mylist)

#Tuples

mytuple = tuple(("Ellis", 30, True))

anothertuple = (1,4,2,8,2,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, two , *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))