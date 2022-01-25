# Generated by Django 4.0.1 on 2022-01-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'AUTHOR'), ('CONTRIBUTOR', 'CONTRIBUTOR')], default='CONTRIBUTOR', max_length=11),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], default='LOW', max_length=6),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('TODO', 'TODO'), ('IN PROGRESS', 'IN PROGRESS'), ('DONE', 'DONE')], default='TODO', max_length=11),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tag',
            field=models.CharField(choices=[('BUG', 'BUG'), ('TASK', 'TASK'), ('UPGRADE', 'UPGRADE')], max_length=7),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('BACKEND', 'BACKEND'), ('FRONTEND', 'FRONTEND'), ('iOS', 'iOS'), ('ANDROID', 'ANDROID')], max_length=8),
        ),
    ]