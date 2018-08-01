# Generated by Django 2.0.7 on 2018-07-26 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0014_project_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='p_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectManage.Project_source'),
        ),
        migrations.AddField(
            model_name='project',
            name='p_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectManage.Project_type'),
        ),
    ]
