# Generated by Django 3.2 on 2021-06-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(default='Dinosaurs', max_length=200),
        ),
    ]
