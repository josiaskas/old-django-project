# Generated by Django 3.0.5 on 2020-04-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=200, verbose_name='message'),
        ),
    ]
