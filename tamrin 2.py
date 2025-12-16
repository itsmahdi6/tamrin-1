def CalculateAverage(Grades) :
  return  sum(Grades) /len(Grades)
    
Count = int (input("please enter the number of unit : "))
if Count <= 0 :
    print("number of unit should be greater than zero")
    exit()
Grades = []
for i in range(Count):
    Grade = float(input(f"please enter the grades of your units"))
    Grades.append(Grade)
Average = CalculateAverage(Grades)
print(f"your average grade is :{Average}")
if Average >= 17 :
    print("nice grade !")
elif Average >= 12 :
    print("good grade ! ")
else :
    print("bad grade !")    
