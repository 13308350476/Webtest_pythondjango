# Generated by Django 3.0.3 on 2020-07-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0006_movie_m_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=100)),
                ('m_grade', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='m_grade',
        ),
    ]
