# Generated by Django 4.0.4 on 2022-05-24 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PMApp', '0002_alter_task_time_estimate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PMApp.project'),
        ),
    ]
