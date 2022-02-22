#tuples; can't be edited
# Here I'm creating a tuple.  Note that the parantheses are usually unnecessary
my_tuple = (4,5,1,8,16.9)
print(my_tuple)
print(type(my_tuple))
# Once you create a tuple, it can't be directly manipulated or extended
#uncomment this line to see the error
#my_tuple[3]=345
#expected output
#(4, 5, 1, 8, 16.9)
#<class 'tuple'>
#TypeError: 'tuple' object does not support item assignment

#-----------------------------------------------------
#tuples can be created, accessed, copied, etc
my_tuple_extension = (7.9,18)
# I'm creating a new tuple that is two existing tuples appended
my_new_tuple = my_tuple + my_tuple_extension
print(my_new_tuple)
print(type(my_new_tuple))
#expected output
#(4, 5, 1, 8, 16.9, 7.9, 18)
#<class 'tuple'>

#-----------------------------------------------------
#tuples can be recreated during runtime
print(my_tuple)
my_tuple = my_tuple[:2] + (7,2) + my_tuple[4:]
print(my_tuple)
#expected output
#(4, 5, 1, 8, 16.9)
#(4, 5, 7, 2, 16.9)
