# Generated by Django 4.1.7 on 2023-04-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_task_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='statusname',
        ),
        migrations.AddField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Inprogress', 'Inprogress'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
