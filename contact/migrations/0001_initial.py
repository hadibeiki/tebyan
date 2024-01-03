# Generated by Django 4.2.9 on 2024-01-03 19:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
        ('sex', '0001_initial'),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mcontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('family', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('dad', models.CharField(max_length=50, verbose_name='نام پدر')),
                ('mobile', models.CharField(max_length=11, verbose_name='شماره موبایل')),
                ('melicode', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('age', models.IntegerField(verbose_name='سن')),
                ('price', models.IntegerField(default=0, verbose_name='هزینه پرداختی')),
                ('marital', models.CharField(choices=[('مجرد', 'مجرد'), ('متاهل', 'متاهل')], max_length=50, verbose_name='وضعیت تاهل')),
                ('otp', models.CharField(max_length=10, verbose_name='کد احراز هویت')),
                ('otpcreatedtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد کد احراز هویت')),
                ('testimonial', models.FileField(blank=True, null=True, upload_to='media/testimonial', verbose_name='رضایت نامه')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='city.mcity', verbose_name='شهرستان')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education.meducation', verbose_name='تحصیلات')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sex.msex', verbose_name='جنسیت')),
            ],
            options={
                'verbose_name': 'فرد',
                'verbose_name_plural': 'افراد',
            },
        ),
    ]
