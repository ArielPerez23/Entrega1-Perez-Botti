# Generated by Django 4.0.5 on 2022-07-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_merge_20220720_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Curiosity', 'Curiosity')], max_length=30),
        ),
    ]
