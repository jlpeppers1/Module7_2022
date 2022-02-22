#declare a list variable

my_example_list = ["this", "is", "a", "list", 5, 6.7]
my_empty_list = []
print(my_example_list)
print(my_empty_list)
#expected output
#['this', 'is', 'a', 'list', 5, 6.7]
#[]

#-----------------------------------------------------
#finding the length of a list
print(len(my_example_list))
print(len(my_empty_list))
#expected output
#6
#0

#-----------------------------------------------------
#appending (or adding) items to a list
my_example_list.append(["a",6])
print(my_example_list)

my_example_list += 'B'
print(my_example_list)

my_example_list += [4,6,9]
print(my_example_list)
#expected output
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6]]
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B']
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B', 4, 6, 9]

#-----------------------------------------------------
#accessing data in a list
print(my_example_list)
print(my_example_list[3])
# A list item can be assigned to a variable
my_string = my_example_list[3]
# The variable will take on the appropriate datatype (instead of a list of length 1)
print(my_string)
print(type(my_string))
#expected output
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B', 4, 6, 9]
#list
#list
#<class 'str'>

#-----------------------------------------------------
#accessing data in a list - sub list
print(my_example_list)
## When accessing multiple items from a list, you will end up with another list
print(my_example_list[1:3])
# These new lists can be assigned to variable
my_short_list = my_example_list[2:4]
print(my_short_list)
# The new variable in this case will take on a datatype of list
print(type(my_short_list))
#expected output
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B', 4, 6, 9]
#['is', 'a']
#['a', 'list']
#<class 'list'>

#-----------------------------------------------------
print(my_example_list)
# These two things are equivalent
print(my_example_list[len(my_example_list)-1]) #in this case, similar to my_example_list[10]
print(my_example_list[-1])
#expected output
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B', 4, 6, 9]
#9
#9
#<class 'list'>

#-----------------------------------------------------
# The range returned will always include the first item and exclude the last
print(my_example_list)
print(my_example_list[3:5])
print(my_example_list[3:-1])
print(my_example_list[4:])
print(my_example_list[:3])
print(my_example_list[:])
#expected output
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B', 4, 6, 9]
#['list', 5]
#['list', 5, 6.7, ['a', 6], 'B', 4, 6]
#[5, 6.7, ['a', 6], 'B', 4, 6, 9]
#['this', 'is', 'a']
#['this', 'is', 'a', 'list', 5, 6.7, ['a', 6], 'B', 4, 6, 9]

#-----------------------------------------------------
# Item positions in a list can be found using the .index method.
a_list = [1,2,3,1,2,3]
print(str(a_list.index(1)))
#expected output
#0
#<class 'list'>

#-----------------------------------------------------
# Sorting Lists
my_no_string_list = [3,7,9,3.4,115,45]
my_all_string_list = ["word","something","fun","game","simple"]
# I had to create new lists because you can't sort a number/string mixed list
print(sorted(my_no_string_list))
print(sorted(my_all_string_list))

# Please note that my original list is unchanged by this sort.  It only sorts at output.
print(my_all_string_list)

# I could assign my new sorted list to a different variable
my_all_string_sorted_list = sorted(my_all_string_list)
print (my_all_string_sorted_list)
#expected output
#[3, 3.4, 7, 9, 45, 115]
#['fun', 'game', 'simple', 'something', 'word']
#['word', 'something', 'fun', 'game', 'simple']
#['fun', 'game', 'simple', 'something', 'word']
#<class 'list'>

# I could also sort my original list by using the .sort() method
my_all_string_list.sort()
print(my_all_string_list)
#expected output
#['fun', 'game', 'simple', 'something', 'word']
