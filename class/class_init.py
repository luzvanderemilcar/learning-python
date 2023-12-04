class Human:
    def __init__(self, name, age, gender, human_id):
        self.id = human_id
        self.name = name
        [self.firstname, self.lastname] = name.split(" ")
        self.age = age
        self.gender = gender
        
    def get_id(self):
        return self.id
        
    def set_id(self,no):
        self.id = no
      
    def introduce(self):
        print(f"My name is {self.name}. I'm {self.age} years old")

luzvander = Human("Luzvander EMILCAR", 27, "male", 23)
# calling method on object
luzvander.set_id(1)
print(luzvander.get_id())