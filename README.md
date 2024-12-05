# Course Enrollment System API

This project is a Django REST Framework (DRF) API for managing course enrollment in a university system. It provides a secure and efficient way to handle authentication, manage data for teachers, students, courses, and sections, and enforce business rules for course and section enrollment.

## Features

1. **Authentication System**
   - Uses Secure Web Tokens (SWT) for authentication.
   - Access tokens are securely saved in cookies for enhanced security.

2. **CRUD Operations**
   - Perform create, read, update, and delete (CRUD) operations for:
     - Teachers
     - Students
     - Courses
     - Sections

3. **Course-Section System**
   - Prevents duplicate sections from being created within the same course.

4. **Teacher Enrollment**
   - Allows teachers to enroll in course sections.
   - Ensures each course section is assigned to only one teacher.

5. **Student Enrollment**
   - Students can enroll in courses and access their enrolled course details.

6. **Unified Data API**
   - Provides a single API endpoint to view all students, teachers, courses, and sections in one response.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abirc0928/Course-Enrolling-System-Django.git
   cd course_enroll
