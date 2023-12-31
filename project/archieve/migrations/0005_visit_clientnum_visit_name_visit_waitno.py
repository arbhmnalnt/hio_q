# Generated by Django 4.2.2 on 2023-07-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archieve', '0004_alter_visit_created_at_alter_visit_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='clientNum',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الحاسب'),
        ),
        migrations.AddField(
            model_name='visit',
            name='name',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='اسم المنتفع'),
        ),
        migrations.AddField(
            model_name='visit',
            name='waitNo',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
