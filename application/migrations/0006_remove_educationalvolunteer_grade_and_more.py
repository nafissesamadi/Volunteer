# Generated by Django 4.2.9 on 2024-01-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_educationalvolunteer_edu_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalvolunteer',
            name='grade',
        ),
        migrations.AddField(
            model_name='educationalvolunteer',
            name='grade',
            field=models.ManyToManyField(blank=True, null=True, to='application.grade', verbose_name='Preffered Grade'),
        ),
    ]