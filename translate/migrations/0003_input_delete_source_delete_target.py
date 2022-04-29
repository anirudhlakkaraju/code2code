# Generated by Django 4.0.4 on 2022-04-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0002_alter_source_language_alter_target_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_lang', models.CharField(choices=[('c++', 'C++'), ('python', 'Python')], default='c++', max_length=10)),
                ('source_code', models.TextField()),
                ('source_testcase', models.TextField()),
                ('source_output', models.TextField()),
                ('target_language', models.CharField(choices=[('c++', 'C++'), ('python', 'Python')], default='c++', max_length=10)),
                ('target_code', models.TextField()),
                ('target_testcase', models.TextField()),
                ('target_output', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='Target',
        ),
    ]
