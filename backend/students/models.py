from django.db import models
from accounts.models import User

class Student(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("graduated", "Graduated"),
        ("suspended", "Suspended"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    student_id = models.AutoField(primary_key=True)

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=1,
        choices=(
            ("M", "Male"),
            ("F", "Female"),
        ),
    )

    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default = 0)

    study_hours_per_week = models.DecimalField(max_digits=4, decimal_places=1, default=0)

    previous_gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    current_grade = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="active",
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class AcademicRecord(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="academic_records",
    )

    semester = models.PositiveSmallIntegerField()

    homework_average = models.DecimalField(max_digits=5, decimal_places=2)

    quiz_average = models.DecimalField(max_digits=5, decimal_places=2)

    midterm_score = models.DecimalField(max_digits=5, decimal_places=2)

    final_exam_score = models.DecimalField(max_digits=5, decimal_places=2)

    final_grade = models.DecimalField(max_digits=5, decimal_places=2)

    passed = models.BooleanField()

    def __str__(self):
        return f"{self.student} - Semester {self.semester}"

class Prediction(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="predictions",
    )

    predicted_grade = models.DecimalField(max_digits=5, decimal_places=2)

    predicted_pass = models.BooleanField()

    confidence = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.created_at.date()}"