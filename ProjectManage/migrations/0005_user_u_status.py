# Generated by Django 2.0.7 on 2018-07-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0004_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_status',
            field=models.IntegerField(default=1),
        ),
    ]