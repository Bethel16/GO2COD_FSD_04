# Generated by Django 5.0.6 on 2024-10-02 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio_app', '0008_specificskill_general_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalskill',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
