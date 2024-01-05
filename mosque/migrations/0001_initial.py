# Generated by Django 4.2.9 on 2024-01-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sex', '__first__'),
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mmosque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام مسجد')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('latitude', models.FloatField(verbose_name='عرض جغرافیایی')),
                ('longtude', models.FloatField(verbose_name='طول جغرافیایی')),
                ('price', models.IntegerField(verbose_name='هزینه اعتکاف')),
                ('velocity', models.IntegerField(verbose_name='ظرفیت')),
                ('startage', models.IntegerField(verbose_name='سن شروع')),
                ('endage', models.IntegerField(verbose_name='سن پایان')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='city.mcity', verbose_name='شهرستان')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sex.msex', verbose_name='جنسیت')),
            ],
            options={
                'verbose_name': 'مسجد',
                'verbose_name_plural': 'مساجد',
            },
        ),
    ]
