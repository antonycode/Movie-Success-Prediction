# Generated by Django 2.1.7 on 2019-04-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movies_ph_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='d_img',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
