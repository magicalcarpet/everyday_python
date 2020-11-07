def eye_colour():
    return 'brown'


def gender():
    return 'male'


def number_of_arms():
    return 2


def name(name):
    return name


print(eye_colour())
print(gender())
print(number_of_arms())
print(name('Kenny'))


def outer(input):
    print(input)
    inner(input)


def inner(input):
    print('I have been called from outer', input)


outer('Romney')
