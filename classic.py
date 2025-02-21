class registration:
    no_of_reg = 0
    def __init__(self, name: str):
        self.name = name
        registration.no_of_reg += 1
   
    members = []
    @classmethod
    def reg_members(cls):
        
        print(f"{cls.no_of_reg} had registered")
    @staticmethod
    def print_reg(self):
        members.append(self.name)
new = registration("muhammad")
registration.reg_members()