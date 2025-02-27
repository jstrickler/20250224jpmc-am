from collections import defaultdict
from functools import wraps


def doit(func):  # <- decorator
    @wraps(func)
    def ham():  # <- "wrapper"
        print("Hello from ham()")
        return_val = func() # <- decorated function
        return return_val
    return ham
    #return func

functions = defaultdict(list)

def register_function(category): # <- decorator takes decorator params
    def _factory(func):
        functions[category].append(func)
        return func
    return _factory

@register_function("foo")
@doit
def spam():
    print("Hello from spam()")
# spam = doit(spam)
# spam = register_function(spam)
# function_list.append(spam)

@register_function("bar")
@doit
def barf():
    return 999

#spam = doit(spam)

spam()  # calling wrapper function
spam()
x = barf()
print(f"{x = }")
print()

@register_function("foo")
def toast():
    print("TOAST")

for category, function_list in functions.items():
    print(category)
    for function in function_list:
        function()


