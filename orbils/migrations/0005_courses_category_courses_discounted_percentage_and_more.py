# Generated by Django 5.0 on 2024-03-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbils', '0004_alter_courses_coursename_alter_courses_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='courses',
            name='discounted_percentage',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='courses',
            name='discounted_price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='courses',
            name='original_price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='courses',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
