# Generated by Django 4.2.3 on 2023-07-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crystal',
            name='color',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crystal',
            name='transparency',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
    ]