# Generated by Django 4.0.6 on 2022-07-09 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]