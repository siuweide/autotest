# Generated by Django 3.1.3 on 2020-11-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201128_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=100, verbose_name='模块名称'),
        ),
    ]