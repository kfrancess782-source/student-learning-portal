"""Student Learning Portal - education."""

class Student:
    def __init__(self, student_id, name, programme):
        self.student_id = student_id
        self.name = name
        self.programme = programme

    def display_info(self):
        return f"{self.student_id}: {self.name} - {self.programme}"

    @classmethod
    def from_record(cls, record):
        return cls(record["student_id"], record["name"], record["programme"])


class Course:
    def __init__(self, course_id, title, lecturer):
        self.course_id = course_id
        self.title = title
        self.lecturer = lecturer
        self.enrolled_students = []

    def enrol(self, student):
        if any(s.student_id == student.student_id for s in self.enrolled_students):
            raise ValueError("Student is already enrolled in this course.")
        self.enrolled_students.append(student)
        return f"{student.name} enrolled in {self.title}."

    def course_summary(self):
        return f"{self.course_id} | {self.title} | Lecturer: {self.lecturer} | Enrolled: {len(self.enrolled_students)}"


class LearningPortal:
    def __init__(self, portal_name):
        self.portal_name = portal_name
        # One required collection: dictionary keyed by unique student ID.
        self.students = {}
        self.courses = {}
        self.results = {}

    @staticmethod
    def valid_score(score):
        return isinstance(score, (int, float)) and 0 <= score <= 100

    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student.student_id] = student

    def add_course(self, course):
        if course.course_id in self.courses:
            raise ValueError("Course ID already exists.")
        self.courses[course.course_id] = course

    def enrol_student(self, student_id, course_id):
        if student_id not in self.students:
            raise KeyError("Student was not found.")
        if course_id not in self.courses:
            raise KeyError("Course was not found.")
        return self.courses[course_id].enrol(self.students[student_id])

    def display_students(self):
        if not self.students:
            return "No students registered."
        return "\n".join(s.display_info() for s in self.students.values())

    def record_result(self, student_id, course_id, score):
        if not self.valid_score(score):
            raise ValueError("Score must be between 0 and 100.")
        if student_id not in self.students or course_id not in self.courses:
            raise KeyError("Student or course was not found.")
        self.results[(student_id, course_id)] = score


    @classmethod
    def create_demo_portal(cls):
        portal = cls("Open Learning Portal")
        portal.add_student(Student("STU-101", "Aminata Koroma", "Software Engineering"))
        portal.add_student(Student("STU-102", "Daniel Bangura", "Information Technology"))
        portal.add_course(Course("CRS-201", "Introduction to Python", "Mr. Kamara"))
        portal.add_course(Course("CRS-202", "Database Fundamentals", "Ms. Conteh"))
        portal.enrol_student("STU-101", "CRS-201")
        portal.enrol_student("STU-102", "CRS-202")
        return portal


def main():
    portal = LearningPortal.create_demo_portal()
    while True:
        print(f"\n=== {portal.portal_name} ===")
        print("1. View students")
        print("2. View courses")
        print("3. Enrol student")
        print("4. Record result")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print(portal.display_students())
            elif choice == "2":
                for course in portal.courses.values():
                    print(course.course_summary())
            elif choice == "3":
                sid = input("Student ID: ").strip()
                cid = input("Course ID: ").strip()
                print(portal.enrol_student(sid, cid))
            elif choice == "4":
                sid = input("Student ID: ").strip()
                cid = input("Course ID: ").strip()
                score = float(input("Score (0-100): "))
                portal.record_result(sid, cid, score)
                print("Result recorded.")
            elif choice == "5":
                print("Thank you for using the Student Learning Portal.")
                break
            else:
                print("Invalid option. Please choose 1 to 5.")
        except (ValueError, KeyError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
