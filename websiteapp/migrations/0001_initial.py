# Generated by Django 4.0.6 on 2022-07-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('writer', models.CharField(blank=True, default='민지', max_length=20, null=True)),
                ('body', models.TextField()),
                ('feelings', models.TextField()),
            ],
        ),
    ]
