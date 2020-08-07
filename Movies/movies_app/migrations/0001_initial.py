# Generated by Django 3.0.5 on 2020-08-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=50, unique=True)),
                ('t_ype', models.CharField(max_length=30)),
                ('rank', models.IntegerField()),
                ('casting', models.CharField(max_length=50)),
                ('release', models.IntegerField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
