from django.db import models

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Schedule(models.Model):
    DAY_CHOICES = [
        ('Пн', 'Понеділок'),
        ('Вт', 'Вівторок'),
        ('Ср', 'Середа'),
        ('Чт', 'Четвер'),
        ('Пт', 'Пʼятниця'),
    ]
    day_of_week = models.CharField(max_length=2, choices=DAY_CHOICES)
    start_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField()


