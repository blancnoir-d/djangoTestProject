# Generated by Django 4.0.1 on 2022-01-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alert_history_content_alert_history_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_history',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='alert_history',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='alert_history',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
