# Generated by Django 4.2.3 on 2023-07-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_prop_alter_aquired_options_alter_aquired_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='crystal',
            name='props',
            field=models.ManyToManyField(to='main_app.prop'),
        ),
    ]
