class Arplaine:
    def __init__(self, id_airplane, model, capacity, owner):
        self._id_airplane = id_airplane
        self.model = model
        self.capacity = capacity
        self.owner = owner
        
    def get_id(self):
        return self._id_airplane
        

class Worker:
   # def __init__(self,id_worker):
      #  self.id_worker = id_worker
        
        
    def set_id_worker(self, new_id):
        self._id_worker = new_id
    
    
    def get_id_worker(self):
        return self._id_worker    

class Pilot(Worker):
    # Function that is call at the creation of each instance
    def __init__(self, id_worker, name, vehicle, employer):
        self._id_worker = id_worker
        self.name = name
        self.employer = employer
        self.vehicle = vehicle
   
    
    
albert = Pilot(15, "Johnson Smith", "airplane", "American Express")
albert._id_worker=23
print(albert._id_worker)