# Generated by Django 3.2.13 on 2023-02-12 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chart1',
            old_name='release_date',
            new_name='release_date1',
        ),
        migrations.RenameField(
            model_name='chart2',
            old_name='release_date',
            new_name='release_date2',
        ),
    ]
