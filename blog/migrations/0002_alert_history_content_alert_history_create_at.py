# Generated by Django 4.0.1 on 2022-01-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_history',
            name='content',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='alert_history',
            name='create_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]