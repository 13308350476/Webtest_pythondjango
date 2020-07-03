# Generated by Django 3.0.3 on 2020-07-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='u_Name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_Password',
            field=models.CharField(max_length=30),
        ),
    ]