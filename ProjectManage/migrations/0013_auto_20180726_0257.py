# Generated by Django 2.0.7 on 2018-07-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0012_company_file_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_file',
            name='ef_path',
            field=models.CharField(max_length=1000),
        ),
    ]
