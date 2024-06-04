# Generated by Django 5.0.6 on 2024-05-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_alter_scheduling_day_alter_scheduling_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='item',
            field=models.CharField(choices=[('is a laptop', 'Laptop'), ('like a non portable laptop', 'Desktop'), ('like a very portable laptop', 'Mobile'), ('for taking photos', 'Camera')], default='Camera', max_length=32, verbose_name='Item'),
        ),
    ]