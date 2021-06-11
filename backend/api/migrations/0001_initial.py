# Generated by Django 3.2.4 on 2021-06-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('github', models.URLField()),
                ('demo', models.URLField(blank=True)),
                ('image', models.FileField(blank=True, upload_to='photos/')),
                ('show', models.BooleanField(default=False)),
            ],
        ),
    ]
