# Generated by Django 4.2.9 on 2024-01-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mosque', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mregistereatekaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(blank=True, choices=[('بله', 'بله'), ('خیر', 'خیر')], max_length=50, null=True, verbose_name='وضعیت پرداخت')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.mcontact', verbose_name='فرد')),
                ('mosque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mosque.mmosque', verbose_name='مسجد')),
            ],
            options={
                'verbose_name': 'ثبت نام',
                'verbose_name_plural': 'ثبت نام های اعتکاف',
            },
        ),
    ]
