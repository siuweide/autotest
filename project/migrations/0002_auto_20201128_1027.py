# Generated by Django 3.1.3 on 2020-11-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': '模块管理', 'verbose_name_plural': '模块管理'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目管理', 'verbose_name_plural': '项目管理'},
        ),
        migrations.AddField(
            model_name='module',
            name='describe',
            field=models.TextField(default='', verbose_name='描述'),
        ),
    ]
