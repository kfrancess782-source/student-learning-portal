import unittest
from main import Student, Course, LearningPortal

class TestStudentLearningPortal(unittest.TestCase):
    def setUp(self):
        self.portal = LearningPortal.create_demo_portal()

    def test_student_object_creation(self):
        student = Student("STU-999", "Test Student", "Computing")
        self.assertEqual(student.name, "Test Student")

    def test_dictionary_stores_students(self):
        self.assertIn("STU-101", self.portal.students)
        self.assertEqual(len(self.portal.students), 2)

    def test_course_enrolment(self):
        student = Student("STU-103", "Mariama Sesay", "Software Engineering")
        self.portal.add_student(student)
        self.portal.enrol_student("STU-103", "CRS-201")
        self.assertEqual(len(self.portal.courses["CRS-201"].enrolled_students), 2)

    def test_duplicate_student_rejected(self):
        with self.assertRaises(ValueError):
            self.portal.add_student(Student("STU-101", "Duplicate", "Computing"))

    def test_result_validation(self):
        self.portal.record_result("STU-101", "CRS-201", 85)
        self.assertEqual(self.portal.results[("STU-101", "CRS-201")], 85)
        with self.assertRaises(ValueError):
            self.portal.record_result("STU-101", "CRS-201", 120)

    def test_missing_student_rejected(self):
        with self.assertRaises(KeyError):
            self.portal.enrol_student("STU-404", "CRS-201")

if __name__ == "__main__":
    unittest.main()
