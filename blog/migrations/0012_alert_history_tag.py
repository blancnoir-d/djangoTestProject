# Generated by Django 4.0.1 on 2022-01-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_history',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
