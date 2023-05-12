class House():

    def __init__(self,bedroom,hall_size,kitchen):
        self.bedroom = bedroom
        self.hall = hall_size
        self.kitchen = kitchen

    def __repr__(self) -> str:
        return f"The House have {self.bedroom} bedroom and {self.kitchen} kitchen"

    def __len__(self):
        return self.hall
    
H = House(2,3000,1)
hall_size = len(H)
print(hall_size)
        
