def calculate_average(scores):
    n=0
    for i in scores:
       n=i+n
    n=n/len(scores)
    print('Average score: '+str(n))

def get_highest_score(scores):
    print("Highest score: "+str(max(scores)))

def get_lowest_score(scores):
    print("Lowest score: "+str(min(scores)))

def process_students(students):
    n=0
    for i in range(4):
        print(students[n])
        n=n+1
    print("Total students: "+str(len(students)))

def register_students(*students):
    print("Registered Students:")
    for student in students:
        print(student)
    print(f"Total: {len(students)}")
