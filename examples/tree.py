# we want to create a function which takes a single integer input and creates a tree
# with a base as wide as the input and progessively gets smaller until it reaches one

# for example, if we have an input of five then: 
# 
# *
# **
# ***
# ****
# *****

# if the input is not an integer, raise an exception and inform the user


def tree(number):
    # check if input belong to int class
    if type(number) == int:
        # take the valid integer and multiply by the star * 
        for i in range(1, number):
            print(i, i * '*')
    else:
        raise Exception("Sorry, only numbers are accepted.")


tree(7)
tree("food")


