Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [23,45,64,12,45,67,89,54,13]
>>> nums
[23, 45, 64, 12, 45, 67, 89, 54, 13]
>>> nums[1]
45
>>> nums[4]
45
>>> nums[2:]
[64, 12, 45, 67, 89, 54, 13]
>>> nums[-]
SyntaxError: invalid syntax
>>> nums[-1]
13
>>> nums[-3:]
[89, 54, 13]
>>> 
>>> names = ['elly', 'dom', 'sarah','caron']
>>> names
['elly', 'dom', 'sarah', 'caron']
>>> values = [45, 'elly', 21]
>>> jar = ['names', 'nums']
>>> jar
['names', 'nums']
>>> jar = [names, nums]
>>> jar
[['elly', 'dom', 'sarah', 'caron'], [23, 45, 64, 12, 45, 67, 89, 54, 13]]
>>> 
>>> 
>>> nums.append(111)
>>> nums
[23, 45, 64, 12, 45, 67, 89, 54, 13, 111]
>>> nums.insert(3,222)
>>> nums
[23, 45, 64, 222, 12, 45, 67, 89, 54, 13, 111]
>>> nums.remove(45)
>>> nums
[23, 64, 222, 12, 45, 67, 89, 54, 13, 111]
>>> nums.pop(4)
45
>>> nums
[23, 64, 222, 12, 67, 89, 54, 13, 111]
>>> 
>>> nums.pop()
111
>>> nums
[23, 64, 222, 12, 67, 89, 54, 13]
>>> 
>>> nums.pop[4:]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nums.pop[4:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> del nums[5:]
>>> nums
[23, 64, 222, 12, 67]
>>> 
>>> nums.extend([12,54,9,234])
>>> nums
[23, 64, 222, 12, 67, 12, 54, 9, 234]
>>> 
>>> #nhfhvf
>>> 
>>> 
>>> min nums
SyntaxError: invalid syntax
>>> min(nums)
9
>>> max(nums)
234
>>> sum(nums)
697
>>> 
>>> 
>>> nums.sort()
>>> nums
[9, 12, 12, 23, 54, 64, 67, 222, 234]
>>> 
>>> 
>>> 
>>> # mutable valus are the values that can be edited
>>> 
>>> # append means adding a number to the end of the list
>>> 
>>> # insert means adding a number when providing a location where to add the number
>>> 
>>> # extend means ading multipe numbers
>>> 
>>> 
>>> remove means delete a chosen number
SyntaxError: invalid syntax
>>> 
>>> # remove means to delete a chosen number
>>> 
>>> # pop means to delete a number by choosng ts location
>>> 
>>> # del means to delete multiple numbers by choosing their locations.
>>> 