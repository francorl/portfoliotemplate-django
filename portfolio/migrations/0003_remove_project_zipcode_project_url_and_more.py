# Generated by Django 4.2.9 on 2024-01-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_project_zipcode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
    ]
