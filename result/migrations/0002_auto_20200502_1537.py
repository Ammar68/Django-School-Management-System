# Generated by Django 3.0.5 on 2020-05-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='exam_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='test_score',
            field=models.IntegerField(default=0),
        ),
    ]
