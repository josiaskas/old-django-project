# Generated by Django 3.0.5 on 2020-04-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('author', models.CharField(max_length=100, verbose_name='source')),
                ('content', models.TextField(max_length=500, verbose_name='contenu')),
                ('link', models.URLField(verbose_name="lien vers l'article")),
                ('pub_date', models.DateField(auto_now=True, verbose_name='Date de publication')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Email adress')),
                ('project_type', models.CharField(choices=[('web_app', 'Web App'), ('web_site', 'Web site'), ('ios_app', 'Ios App')], max_length=10, verbose_name='Type de projet')),
                ('amount', models.FloatField(default=300, verbose_name='Montant')),
                ('details', models.TextField(max_length=2000, verbose_name='Détails additionel')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('source', models.CharField(max_length=100, verbose_name='source')),
                ('embed_code', models.TextField(max_length=500, verbose_name='embed code')),
                ('pub_date', models.DateField(verbose_name='Date de publication')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nom')),
                ('picture', models.CharField(max_length=200, verbose_name='image')),
                ('logo_picture', models.URLField(blank=True, null=True, verbose_name='logo image')),
                ('excerpt', models.CharField(default='A simple project', max_length=300, verbose_name='extrait')),
                ('content', models.TextField(verbose_name='contenue')),
                ('url', models.URLField(verbose_name='Url vers le projet')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='slug')),
                ('featured', models.BooleanField(default=False, verbose_name='en vedette')),
                ('published', models.BooleanField(default=False, verbose_name='publié')),
                ('realease_date', models.DateField(verbose_name='Date de livraison')),
                ('tags', models.ManyToManyField(related_name='projects', to='projects.Tag')),
            ],
        ),
    ]
