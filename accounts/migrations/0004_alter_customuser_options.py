# Generated by Django 3.2.7 on 2021-09-20 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210920_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
    ]