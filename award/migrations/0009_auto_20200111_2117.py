# Generated by Django 2.2.8 on 2020-01-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0008_auto_20200111_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_photo',
            field=models.ImageField(blank=True, default='person.png', upload_to='images/'),
        ),
    ]