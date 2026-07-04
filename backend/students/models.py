from django.db import models

from accounts.models import User
from django.utils import timezone

class Student(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("graduated", "Graduated"),
        ("suspended", "Suspended"),
    )

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    PARENTAL_EDUCATION_CHOICES = (
        ("primary", "Primary School"),
        ("secondary", "Secondary School"),
        ("bachelor", "Bachelor"),
        ("master", "Master"),
        ("doctorate", "Doctorate"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )

    student_id = models.AutoField(primary_key=True)

    age = models.PositiveSmallIntegerField()

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )

    class_name = models.CharField(max_length=30)

    study_hours_per_day = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
    )

    attendance_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    parental_education = models.CharField(
        max_length=20,
        choices=PARENTAL_EDUCATION_CHOICES,
    )

    internet_access = models.BooleanField(default=True)

    extracurricular_activities = models.BooleanField(default=False)

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

    math_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    science_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    english_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    previous_year_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    final_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    performance_level = models.CharField(
        max_length=20,
        default="Unknown",
    )
    passed = models.BooleanField()

    def __str__(self):
        return f"{self.student} Academic Record"


class Prediction(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="predictions",
    )

    predicted_final_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    predicted_performance_level = models.CharField(
        max_length=20,
        default="Unknown",
    )

    predicted_pass = models.BooleanField()

    confidence = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} Prediction ({self.created_at.date()})"