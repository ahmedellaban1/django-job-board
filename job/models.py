from django.db import models

JOB = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
)


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    JobType = models.CharField(max_length=100, choices=JOB)
    # location



