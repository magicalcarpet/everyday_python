def add(first_num, second_num):
    return first_num + second_num


print(add(76, 9023))
fn_add = add
print(fn_add(1, 8))

result = lambda x,y: x + y
print(result(3, 7))

value = lambda a, b: a * b
print(value(7, 7))
