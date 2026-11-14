names = [input("Name: ") 
for _ in range(int(input("Count: ")))]

print("Students:",",".join(names))
print("Total:", len(names))
def average(scores):
    return sum(scores) / len(scores)
    
scores = [float(input("Score: "))

for scores in range(int(input("Count: ")))]

print("Average:", average(scores))
print("Max:", max(scores))
print("Min:", min(scores))
