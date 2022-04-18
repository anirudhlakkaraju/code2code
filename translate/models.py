from unittest import TestCase
from django.db import models
from django.conf import settings
from django.utils import timezone

LANGUAGE_CHOICES = (
    ('c++', 'C++'),
    ('python','Python'),
)


class Source(models.Model):

    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='c++')
    code = models.TextField()
    testcase = models.TextField()


class Target(models.Model):

    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='c++')
    code = models.TextField()
    testcase = models.TextField()

