# Generated by Django 3.0.4 on 2020-03-28 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batches', '0003_remove_batch_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='students',
        ),
    ]
