import json
import os
import itertools


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]

class Student:
    def __init__(self, id, grade, math, science, history, english, geography):
        self.id = id
        self.grade = grade
        self.math = math
        self.science = science
        self.history = history
        self.english = english
        self.geography = geography
        
    def __getitem__(self, key):
        return getattr(self, key)
        
    
    def average_mark(self):
        return float(self.math + self.science + self.history + self.english + self.geography) / 5
    
    def hardest_subject(self):
        return min([self.math, self.science, self.history, self.english, self.geography])

    def easiest_subject(self):
        return max([self.math, self.science, self.history, self.english, self.geography])
        

def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = Student(**json.load(file))
    except FileNotFoundError:
        return {}

    return report_card

def load_all_student_report_cards():
    students = []
    
    for i in range(1000):
        students.append(load_report_card("students", i))

    return students
    
def calculate_average_student_mark():
    students = load_all_student_report_cards()
    return sum([s.average_mark() for s in students]) / len(students)

def find_easiest_subject():
    students = load_all_student_report_cards()
    scores = []
    
    for subject in SUBJECTS:
       scores.append({"subject": subject, "average_mark": sum(map(lambda x: x[subject], students)) / len(students)})
    
    return max(scores, key=lambda x: x["average_mark"])["subject"]
    

def find_hardest_subject():
    students = load_all_student_report_cards()
    scores = []
    
    for subject in SUBJECTS:
       scores.append({"subject": subject, "average_mark": sum(map(lambda x: x[subject], students)) / len(students)})
    
    return min(scores, key=lambda x: x["average_mark"])["subject"]

def find_best_grade():
    students = load_all_student_report_cards()
    grade_marks = []
    
    for k, v in itertools.groupby(students, lambda x: x.grade):
        groupLength = len(list(v))
        grade_marks.append({"grade": k, "average_mark": sum(map(lambda x: x.average_mark(), v)) / groupLength })
        
    return max(grade_marks, key=lambda x: x['average_mark'])["grade"]    

def find_worst_grade():
    students = load_all_student_report_cards()
    grade_marks = []
    
    for k, v in itertools.groupby(students, lambda x: x.grade):
        groupLength = len(list(v))
        grade_marks.append({"grade": k, "average_mark": sum(map(lambda x: x.average_mark(), v)) / groupLength  })
        
    return min(grade_marks, key=lambda x: x['average_mark'])["grade"]    
        

def find_best_student_id():
    students = load_all_student_report_cards()
    best_student = None
    
    for s in students:
        if best_student is None:
            best_student = s
        elif best_student.average_mark() < s.average_mark():
            best_student = s
    
    return best_student.id    

def find_worst_student_id():
    students = load_all_student_report_cards()
    worst_student = None
    
    for s in students:
        if worst_student is None:
            worst_student = s
        elif worst_student.average_mark() > s.average_mark():
            worst_student = s
    
    return worst_student.id    

def main():
    print(f"Average Student Grade: {calculate_average_student_mark()}")
    print(f"Best Performing Grade: {find_best_grade()}")
    print(f"Easiest Subject: {find_easiest_subject()}")
    print(f"Hardest Subject: {find_hardest_subject()}")
    print(f"Works Performing Grade: {find_worst_grade()}")
    print(f"Best Student ID: {find_best_student_id()}")
    print(f"Worst Student ID: {find_worst_student_id()}")
    
if __name__ == "__main__":
        main()
