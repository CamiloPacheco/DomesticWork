# Generated by Django 2.1.3 on 2018-11-12 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findWork', '0004_auto_20181112_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=30)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findWork.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='administrator',
            name='User',
        ),
        migrations.AddField(
            model_name='administrator',
            name='Password',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administrator',
            name='Username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
