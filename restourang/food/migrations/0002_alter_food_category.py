# Generated by Django 4.2.2 on 2023-06-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(choices=[('1', 'pizza'), ('2', 'burger'), ('3', 'pasta'), ('4', 'fries')], max_length=6),
        ),
    ]
