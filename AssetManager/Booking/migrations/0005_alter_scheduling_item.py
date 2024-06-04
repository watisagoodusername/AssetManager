# Generated by Django 5.0.6 on 2024-05-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_alter_scheduling_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='item',
            field=models.CharField(choices=[('laptop', 'Laptop'), ('desktop', 'Desktop'), ('mobile', 'Mobile'), ('camera', 'Camera')], default='Camera', max_length=32, verbose_name='Item'),
        ),
    ]