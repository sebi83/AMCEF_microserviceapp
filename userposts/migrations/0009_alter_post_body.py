# Generated by Django 4.0.4 on 2022-05-31 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0008_alter_post_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
