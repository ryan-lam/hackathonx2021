# Generated by Django 3.2.4 on 2021-06-26 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_course_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequence',
            old_name='order',
            new_name='index',
        ),
    ]
