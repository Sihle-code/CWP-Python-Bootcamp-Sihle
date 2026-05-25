students = {
    "John": {"math": 70, "english": 85, "science": 90},
    "Mary": {"math": 95, "english": 88, "science": 76},
    "Peter": {"math": 60, "english": 72, "science": 65},
    "Jane": {"math": 88, "english": 91, "science": 89}
}

# 1. Finds the student with the highest average score   
def highest_average(students):

    highest_student = ""
    highest_avg = 0

    for student, marks in students.items():

        average = sum(marks.values()) / len(marks)

        if average > highest_avg:
            highest_avg = average
            highest_student = student

    return highest_student
print(highest_average(students))


# 2. Finds the student with the lowest science score

lowest_science_marks = ""
lowest_score = 100

for student, marks in students.items():

    if marks["science"] < lowest_score:
        lowest_science_marks = marks["science"]
        lowest_science_marks = student

print(lowest_science_marks) 

# 3. Counts how many students scored above 80 in at least 2 subjects

def count_above_80(students):
    count = 0
    for score in students.values():
        if sum(marks > 80 for marks in marks.values()) >= 2:
            count += 1
    return count

print(count_above_80(students))

#4. Creates a new dictionary that stores each student’s average score rounded to 2 decimal places
def create_average_dict(students):
    average_dict = {}
    for student, marks in students.items():
        average_score = sum(marks.values()) / len(marks)
        average_dict[student] = round(average_score, 2)
    return average_dict
print(create_average_dict(students))