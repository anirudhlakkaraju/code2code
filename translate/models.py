from unittest import TestCase
from django.db import models
from django.conf import settings
from django.utils import timezone

LANGUAGE_CHOICES = (
    ('c++', 'C++'),
    ('python','Python'),
)


class Input(models.Model):

    source_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='c++')
    source_code = models.TextField()
    source_testcase = models.TextField()
    source_output = models.TextField()
    
    target_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='c++')
    target_code = models.TextField()
    target_testcase = models.TextField()
    target_output = models.TextField()



