# Generated by Django 3.2.5 on 2021-07-25 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=0, max_length=5),
        ),
    ]
