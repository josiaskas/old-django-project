# Generated by Django 3.0.5 on 2020-04-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200420_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo_picture',
            field=models.ImageField(blank=True, null=True, upload_to='projects/', verbose_name='logo'),
        ),
    ]
