from django.db import models


class School(models.Model):

    SCHOOL_TYPES = [
        ('University', 'University'),
        ('Polythecnic', 'Polythecnic'),
        ('College', 'College'),
        ('Academy', 'Academy'),
        ('Institute', 'Institute'),
        ('Senior Secondary', 'Senior Secondary'),
        ('Junior Secondary', 'Junior Secondary'),
        ('Primary', 'Primary'),
        ('Nursery', 'Nursery'),
    ]

    school_name = models.CharField(max_length=255)
    school_motto = models.CharField(max_length=255)
    school_logo = models.ImageField()
    school_phone = models.CharField(max_length=15, blank=True, null=True)
    school_address = models.TextField()
    school_website = models.CharField(max_length=50)
    school_type = models.CharField(choices=SCHOOL_TYPES)

    def __str__(self) -> str:
        return self.school_name