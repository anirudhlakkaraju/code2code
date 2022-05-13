# Generated by Django 4.0.4 on 2022-05-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0008_alter_input_source_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='source_language',
            field=models.CharField(choices=[('C++', 'C++'), ('Python', 'Python')], default='C++', max_length=10),
        ),
        migrations.AlterField(
            model_name='input',
            name='target_language',
            field=models.CharField(choices=[('C++', 'C++'), ('Python', 'Python')], default='Python', max_length=10),
        ),
    ]
