# Generated by Django 4.0.1 on 2022-02-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_quiz_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='public',
            field=models.BooleanField(default=False, null=True),
        ),
    ]