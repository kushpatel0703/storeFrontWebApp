# Generated by Django 2.1.3 on 2018-11-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=1000)),
                ('price', models.FloatField(max_length=50)),
                ('itemIcon', models.CharField(max_length=1000)),
            ],
        ),
    ]