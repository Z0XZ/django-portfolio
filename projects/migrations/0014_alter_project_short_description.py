# Generated by Django 4.1.7 on 2023-03-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_project_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(max_length=200),
        ),
    ]
