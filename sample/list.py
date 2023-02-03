a=["python","javacsript","html","css"]
# append adding last element
a.append("ruby")
print(a)

# insert particular place insert element

a.insert(1,"cloudComputing")
print(a)

# pop last element delete
a.pop()
print(a)

# particular elment delete using index value
a.pop(0)
print(a)

#remove particular element remove using value
a.remove("html")
print(a)

#delete 
del a[0]
print(a)

# extend
b=["good", "learning", "good1"]
a.extend(b)
print(a)

# count
c=b.count("good")
print(c)

# index
d=b.index("learning")
print(d)

#reverse
b.reverse()
print(b)

#copy
c=b.copy()
print(c)

#sort()

c=["b","a","e","d","c"]
c.sort()
print(c)

#sort 

a=["a","b","i","d","p","r"]
a.sort()
print(a)

# reverse
a.reverse()
print(a)
