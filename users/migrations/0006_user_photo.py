# Generated by Django 4.1 on 2022-08-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/images/profile_pictures/'),
        ),
    ]