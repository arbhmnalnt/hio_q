# Generated by Django 4.2.2 on 2023-07-16 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archieve', '0005_visit_clientnum_visit_name_visit_waitno'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='lawOrentity',
            field=models.CharField(blank=True, max_length=175, null=True, verbose_name='جهة العمل / القانون'),
        ),
    ]
