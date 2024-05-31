class Owner:
    def __init__(self, name):
        self.name=name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self            
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)    

class Pet:
    def __init__(self, name, pet_type, owner=None):
        all=[]
        PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
        self.name=name
        self.pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)
            