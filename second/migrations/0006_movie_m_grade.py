# Generated by Django 3.0.3 on 2020-07-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0005_auto_20200702_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='m_grade',
            field=models.CharField(max_length=10, null=True),
        ),
    ]