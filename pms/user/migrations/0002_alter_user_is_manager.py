# Generated by Django 4.1.7 on 2023-03-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
