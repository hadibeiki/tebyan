# Generated by Django 4.2.9 on 2024-01-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='سطح تحصیلات')),
            ],
            options={
                'verbose_name': 'تحصیلات',
                'verbose_name_plural': 'تحصیلات',
            },
        ),
    ]
