# Generated by Django 3.0.5 on 2020-04-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200418_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='project_type',
            field=models.CharField(choices=[('web app', 'Web Appsss'), ('web site', 'Web site'), ('Ios app', 'Ios App')], max_length=20, verbose_name='Type de projet'),
        ),
    ]
