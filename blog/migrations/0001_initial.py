# Generated by Django 3.0.5 on 2020-04-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=200)),
                ('long_text', models.TextField()),
            ],
        ),
    ]