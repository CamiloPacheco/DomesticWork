# Generated by Django 2.1.3 on 2018-11-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findWork', '0009_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Phone',
            field=models.IntegerField(max_length=30),
        ),
    ]