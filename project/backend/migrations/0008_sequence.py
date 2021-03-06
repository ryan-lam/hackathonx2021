# Generated by Django 3.2.4 on 2021-06-26 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_item_course_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.course')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.item')),
            ],
        ),
    ]
