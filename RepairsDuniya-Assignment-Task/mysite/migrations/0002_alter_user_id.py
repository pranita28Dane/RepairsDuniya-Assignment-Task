# Generated by Django 4.2.5 on 2023-10-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
