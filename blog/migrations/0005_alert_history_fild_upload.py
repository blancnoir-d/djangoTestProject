# Generated by Django 4.0.1 on 2022-01-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alert_history_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_history',
            name='fild_upload',
            field=models.FileField(blank=True, upload_to='blog/images/%Y/%m/%d'),
        ),
    ]