# Generated by Django 2.1 on 2018-10-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-update']},
        ),
        migrations.AddField(
            model_name='thread',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
