# Generated by Django 3.1.4 on 2020-12-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201230_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alterado',
            field=models.DateTimeField(),
        ),
    ]
