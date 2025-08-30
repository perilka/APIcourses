from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name if len(self.name) < 15 else f"{self.name[:15]}..."

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title if len(self.title) < 15 else f"{self.title[:15]}..."

class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='details')
    semester = models.CharField(max_length=20)
    duration_weeks = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['semester', 'course', 'university'], name='unique university course for semester')
        ]

    def __str__(self):
        return f'{self.course} from {self.university}'
