# Generated by Django 2.0.7 on 2018-07-26 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0008_auto_20180726_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='superior_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectManage.Department'),
        ),
    ]