class Student:
    def __init__(self, course_id, course_title, credit_hours, cgpa):
        self.data = [{'Course Id': course_id, 'Course Title': course_title, 'Credit Hours': credit_hours, 'CGPA': cgpa}]
    
    def add_course(self, course_id="", course_title="", credit_hours=0.0, cgpa=0.0):
        self.data.append({'Course Id': course_id, 'Course Title': course_title, 'Credit Hours': credit_hours, 'CGPA': cgpa})
    
    def calculate_cgpa(self):
        total_credit_points = sum(course['Credit Hours'] * course['CGPA'] for course in self.data)
        total_credit_hours = sum(course['Credit Hours'] for course in self.data)
        if total_credit_hours == 0:
            return 0.0
        return total_credit_points / total_credit_hours
    
    def show(self):
        for idx, course in enumerate(self.data, start=1):
            print(f"Course {idx}:")
            print(f"  Course ID: {course['Course Id']}")
            print(f"  Course Title: {course['Course Title']}")
            print(f"  Credit Hours: {course['Credit Hours']}")
            print(f"  CGPA: {course['CGPA']}\n")

# Example usage:
s1 = Student('Math101', 'Fc', 3, 4)
s1.add_course('Physics101', 'Fc', 4, 3.5)
s1.add_course('Chemistry101', 'Fc', 3, 3.7)

print("Student Data:")
s1.show()
print(f"CGPA: {s1.calculate_cgpa()}")
