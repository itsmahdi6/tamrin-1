class Vehicle :
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def display_info(self) :
        print(f"___information of vehicle___")
        print(f"brand :{self.brand}")
        print(f"year :{self.year}")
class Car(Vehicle) :
    def __init__(self, brand, year ,doors):
        super().__init__(brand, year)
        self.doors=doors
    def display_info(self) :
      super().display_info()
      print(f"doors :{self.doors}\n")
class Motorcycle(Vehicle) :
    def __init__(self, brand, year , has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar=has_sidecar
    def display_info(self):
        super().display_info()
        print(f"has_sidecar : {self.has_sidecar}")    
Vehicle1=Vehicle("audi" , 2015)
car1=Car("benz" ,2022 ,2)
motorcycle1=Motorcycle("kawasaki",2020,"no")
print(f"first : vehicle information :")
Vehicle1.display_info()
print(f"second : car information :")
car1.display_info()
print(f"third :motorcycle information :")
motorcycle1.display_info()
        