from django.db import models

JOB = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
)
"""JOB_CATEGORY = (
    ('programming', 'programming'),
    ('freelancing', 'freelancing'),
    ('designing', 'designing'),
    ('front end', 'front end'),
)
"""


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    JobType = models.CharField(max_length=15, choices=JOB)
    description = models.TextField(max_length=2000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiences = models.IntegerField(default=1)
    # category = models.CharField(max_length=30, choices=JOB_CATEGORY)
    # location

    def __str__(self):
        return self.title, ' in ', self.published_at