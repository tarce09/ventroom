# Generated by Django 3.2.2 on 2021-05-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sentiment',
            field=models.CharField(default='pass', max_length=10),
        ),
    ]