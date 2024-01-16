# Generated by Django 4.2.9 on 2024-01-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_mcontact_marital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcontact',
            name='marital',
            field=models.CharField(choices=[('متاهل', 'متاهل'), ('مجرد', 'مجرد')], max_length=50, verbose_name='وضعیت تاهل'),
        ),
    ]