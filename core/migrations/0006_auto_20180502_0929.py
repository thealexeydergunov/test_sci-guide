# Generated by Django 2.0.4 on 2018-05-02 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180501_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultfromparsing',
            name='url',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.URLForProcessing', verbose_name='URL'),
        ),
    ]
