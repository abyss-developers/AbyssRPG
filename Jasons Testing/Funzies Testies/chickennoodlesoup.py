class Bob:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def manage(self):
        print("hello my name is {} and i am {} years old. i am also {} feet tall.".format(self.name,self.age,self.height))
    
hello = Bob("jason", 12, 5)
hello.manage()