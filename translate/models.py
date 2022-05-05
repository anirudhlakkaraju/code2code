from django.db import models

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
    translated_code = models.TextField(blank=True)
    target_testcase = models.TextField()
    target_output = models.TextField()



