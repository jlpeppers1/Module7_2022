#def my_function(score, score2=0, score3=0...):
def my_function(*inputs):
    total = 0
    for num in inputs:
        total += num
    return total

print(my_function(7))
print(my_function(7,9,12,30))
print(my_function())
#Expected output
#7
#58
#0


def my_function_with_kw(*inputs,**kwinputs):
    for label,data in kwinputs.items():
        print(label, data)

my_function_with_kw(name='matt',language='Python')
print()
my_function_with_kw(shape='rectangle', color='blue')
#expected output
#name matt
#language Python
#
#shape rectangle
#color blue

#Grab just  certain keys
def my_function_only_print_name(**kwinputs):
    f_name = ""
    l_name = ""
    for key,value in kwinputs.items():
        if key == "first_name":
            f_name = value
        if key == "last_name":
            l_name = value
    return f"Hello {f_name} {l_name}! Have a nice day!"
print()
print(my_function_only_print_name(name="jacob", first_name="joe", gpa=2.36, language="python", sign="gemini", last_name="smith"))
#expected output
#Hello joe smith! Have a nice day!
