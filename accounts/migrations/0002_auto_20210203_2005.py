# Generated by Django 3.1.5 on 2021-02-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='userId',
            new_name='user',
        ),
    ]
