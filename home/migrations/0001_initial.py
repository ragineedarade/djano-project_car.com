# Generated by Django 5.0.6 on 2024-06-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120)),
                ('message', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
