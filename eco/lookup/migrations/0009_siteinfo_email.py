# Generated by Django 3.0.7 on 2020-06-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0008_auto_20200620_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]