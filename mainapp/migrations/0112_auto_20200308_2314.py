# Generated by Django 2.2.11 on 2020-03-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0111_auto_20190818_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsjob',
            name='sms_type',
            field=models.CharField(choices=[('consent', 'Consent'), ('info', 'Information'), ('survey', 'Survey')], max_length=10),
        ),
    ]