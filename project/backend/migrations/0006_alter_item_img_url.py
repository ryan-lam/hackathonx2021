# Generated by Django 3.2 on 2021-06-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]