# To Access Python List by Indexing//Python List Slicing
List = ['foo', 'bar', 'baz', 'quz', 'quux', 'corge']
print(List[2])
print(List[4:6])
print(List[-4:-1])
print(List[1:5:2])
print(List[-1: :-1]) # Reverse List
print()

# Iteration of a List
r = ['a', 'b', 'c', 1, 2, 3]
for x in r:
	print(x)
print()

# adding python list using the concatenation operator(+)
m = ['a', 'b', 'c']
n = ['x', 'y', 'z']
k = m + n
print(k)
print()

# adding python list using the replication operator(*)
m = ['a', 'b', 'c']
print(m * 3)
print()

# Updating a List
data1 = [5, 10, 15, 20, 25]

print("Values of list are: ")
print(data1)
data1[2] = "multiple of 5"
print("Values of a List are: ")
print(data1)
print()

# Deleting an Element in a List
data1 = [5, 10, 15, 20, 25]
print("data in the List are: ", data1)
del(data1[2])
print("New data in the List are: ", data1)
print()

# Python List Functions
# min(list)
x = [1, 2, 3]
y = ['a', 'b', 'c']
print(min(x))
print(min(y))
print()

# max(list)
x = [1, 2, 3]
y = ['a', 'b', 'c']
print(max(x))
print(max(y))
print()

# len(list)
x = [1, 2, 3]
y = []
z = ['a', 'b', 'c', 1, 2, 3]
print(len(x))
print(len(y))
print(len(z))
print()

# list(seq)
t = (1997, 'c++', 'java', 'python')
d = list(t)
print('List Elements : ', d)
string = "ApkZube"
u = list(string)
print("List Elements : ", u)
print()

# Python List Methods
# Counting how many times an Element appered in a List 
# list.count(obj)
w = [1,2,3,'a','b','c',1,2,3]
print(w.count(1))
print(w.count('b'))
print(w.count(4))
print()

# Appending a List
# listname.append()
data1 = [5, 10, 15, 20, 25]
data1.append(1.5)
data1.append('x')
data1.append(['y', 'z'])
print(data1)
print()

# Extending a List
# ListName.extend()
s = [1,2,3]
s.extend([4])
s.extend('ApkZube')
s.extend((['a','b','c']))
print(s)
print()

# Indexing 
# ListName.index()
Rajuu = ['ApkZube','Python','Java','C++',1,2,3]
print(Rajuu.index('Java'))
print(Rajuu[3])
print(Rajuu.index(2))


# Inserting an Element
# listName.insert(index,obj)
Rajuu = ['ApkZube','Python','Java','C++',1,2,3]
Rajuu.insert(3,'C#')
print(Rajuu)
print()

# Removing the Element in the List
# ListName.pop(index)
Rajuu = ['ApkZube','Python','Java','C++',1,2,3]
Rajuu.pop()
print(Rajuu)
Rajuu.pop(2)
print(Rajuu)
print()

# Removing the Element in the List
# ListName.remove()
Rajuu = ['ApkZube','Python','Java','C++',1,2,3]
Rajuu.remove(3)
print(Rajuu)
Rajuu.remove('Python')
print(Rajuu)
print()

# Reversing the List
# ListName.reverse()
Rajuu = ['ApkZube','Python','Java','C++',1,2,3]
Rajuu.reverse()
print(Rajuu)
print()

# Sorting an Element in a List
# ListName.sort()
Rajuu = ['ApkZube','Python','Java','C++']
Leila = [100,45,890,22,9764,10,6453,2]
Frado = ['z','ab','a','abc','n','b','acb','abz']
Rajuu.sort()
Leila.sort()
Frado.sort()
print(Rajuu)
print(Leila)
print(Frado)
print()
