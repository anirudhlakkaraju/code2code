from django.db import models

LANGUAGE_CHOICES = (
    ('C++', 'C++'),
    ('Python','Python'),
)


class Input(models.Model):

    source_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='C++')
    source_code = models.TextField()

    # In case test cases is implemented. UNUSED FOR NOW
    source_testcase = models.TextField()
    source_output = models.TextField()
    
    target_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='Python')
    translated_code = models.TextField(blank=True)
    
    # In case test cases is implemented. UNUSED FOR NOW
    target_testcase = models.TextField()
    target_output = models.TextField()



