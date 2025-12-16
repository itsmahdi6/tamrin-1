students =[
    {"name" : "ali" ,"id" :"100" ,"grades" :[15,18,16]},
    {"name" :"mahdi" ,"id" :"110", "grades":[19,17,14]},
    {"name" :"hasan" ,"id" :"120", "grades":[14,16,11]}
]
def calculate_student_avg(student):
    grades=student["grades"]
    if len(grades) == 0 :
        return 0
    avg = sum(grades)/len(grades)
    return avg
for student in students :
    avg = calculate_student_avg(student)
    print(f"{student['name']} (ID: {student['id']}) average grade is {avg:.2f}")
