# Generated by Django 4.1.7 on 2023-03-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]