# Generated by Django 3.2.5 on 2021-07-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]