# Student Learning Portal

## Project Overview
A Python Object-Oriented Programming demonstration for an education-focused Student Learning Portal. It manages student records, courses, course enrolments and assessment results.

## Objectives
- Demonstrate classes, objects, attributes and methods.
- Store multiple student objects in a dictionary using unique student IDs.
- Demonstrate instance, class and static methods.
- Enrol students in courses and record validated assessment scores.
- Apply Digital Public Goods (DPG) principles.

## Technologies
Python 3, Visual Studio Code, Python `unittest`, Git and GitHub.

## Main Classes
- `Student`: stores student identity and programme information.
- `Course`: stores course details and enrolled student objects.
- `LearningPortal`: manages student and course records, enrolment and results.

## Features
- View registered students and courses.
- Enrol students in courses.
- Record scores from 0 to 100.
- Validate duplicate student/course IDs and missing records.

## Run
```bash
python3 main.py
```

## Run tests
```bash
python3 -m unittest -v test_main
```

## Sample records
- STU-101 — Aminata Koroma — Software Engineering
- STU-102 — Daniel Bangura — Information Technology
- CRS-201 — Introduction to Python
- CRS-202 — Database Fundamentals

## DPG Alignment
- **Open source:** source code can be reviewed and reused through GitHub.
- **Inclusive and accessible:** simple text-based interface and standard Python runtime.
- **Privacy-respecting:** demonstration records are fictional; no real sensitive student data should be committed.
- **Modular and reusable:** separate classes represent students, courses and portal operations.

## Limitations and Future Improvements
This is an educational console prototype. Future versions could add a database, secure authentication, a web/mobile interface, learning materials, attendance, assignment submission, and role-based access.

## Project Structure
```text
Student_Learning_Portal/
├── main.py
├── test_main.py
├── README.md
