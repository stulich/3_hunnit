# Generated by Django 2.1.2 on 2018-11-01 22:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UMassApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveypost',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this post', primary_key=True, serialize=False),
        ),
    ]