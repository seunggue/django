# Generated by Django 2.2.4 on 2019-10-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('choice_1', models.CharField(max_length=100)),
                ('choice_2', models.CharField(max_length=100)),
            ],
        ),
    ]