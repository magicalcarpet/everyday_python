class Parent:
    def __init__(self, fingers):
        self.fingers = fingers


    def get_fingers(self):
        return self.fingers


class Child(Parent):
    def __init__(self, eye_colour, gender, skin_colour, favourite_sport, fingers):
        Parent.__init__(self, fingers)
        self.eye_colour = eye_colour
        self.gender = gender
        self.skin_colour = skin_colour
        self.favourite_sport = favourite_sport

    
    def get_skin_colour(self):
        return f'The skin colour is {self.skin_colour}'


    def get_eye_colour(self):
        return f'The eye colour is {self.eye_colour}'


    def get_gender(self):
        return f'The gender is {self.gender}'


    def get_favourite_sport(self):
        return f'My favourite sport is {self.favourite_sport}'


    def set_favourite_sport(self, favourite_sport):
        self.favourite_sport = favourite_sport


    
parent = Parent(5)
print(parent.fingers)
print(parent.get_fingers())

tom = Child('blue', 'male', 'yellow', 'archery', 5)
steve = Child('green', 'uncertain', 'pink', 'skiing', 4)
print(tom.get_fingers())
# print(tom.eye_colour)
# print(tom.skin_colour)
# print(tom.gender)
# print(tom.get_skin_colour())
# print(tom.get_gender())
# print(tom.get_eye_colour())
# print(tom.get_favourite_sport())
# tom.set_favourite_sport('rowing')
# print(tom.get_favourite_sport())
# print('-'*30)

# print(steve.eye_colour)
# print(steve.skin_colour)
# print(steve.gender)
# print(steve.get_skin_colour())
# print(steve.get_gender())
# print(steve.get_eye_colour())
# print(steve.get_favourite_sport())
# steve.set_favourite_sport('wrestling')
# print(steve.get_favourite_sport())
# steve.set_favourite_sport('rally cross')
# print(steve.get_favourite_sport())
