# Generated by Django 4.2.9 on 2024-01-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mcity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام شهرستان')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تلفن پشتیبانی')),
                ('mobile', models.CharField(max_length=11, verbose_name='شماره موبایل پشتیبانی')),
                ('user', models.CharField(max_length=200, verbose_name='نام کاربر پشتیبانی')),
            ],
            options={
                'verbose_name': 'شهرستان',
                'verbose_name_plural': 'شهرستان ها',
            },
        ),
    ]
