def calculate_average(scores):
    n=0
    for i in scores:
       n=i+n
    n=n/len(scores)
    print('Average score: '+str(n))
scores = [78, 91, 85, 67, 95, 88]
calculate_average(scores)
def get_highest_score(scores):
    print("Highest score: "+str(max(scores)))
    
scores = [78, 91, 85, 67, 95, 88]
get_highest_score(scores)
def get_lowest_score(scores):
    print("Lowest score: "+str(min(scores)))
    
scores = [78, 91, 85, 67, 95, 88]
get_lowest_score(scores)
def process_students(students):
    n=0
    for i in range(4):
        print(students[n])
        n=n+1
students = ["Ali", "Leyla", "Kamran", "Aysel"]

process_students(students)
print("Total students: "+str(len(students)))
def register_students(*students):
    print("Registered Students:")
    for student in students:
        print(student)
    print(f"Total: {len(students)}")

register_students("Ali", "Leyla", "Kamran")
