# Generated by Django 5.0.6 on 2024-05-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduling',
            name='notes',
        ),
        migrations.AddField(
            model_name='scheduling',
            name='item',
            field=models.TextField(default='ITEM', help_text='Item booked', max_length=32, verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='scheduling',
            name='person',
            field=models.TextField(default='USER', help_text='User booking the item', max_length=32, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='day',
            field=models.DateField(help_text='Day required', verbose_name='Day required'),
        ),
    ]