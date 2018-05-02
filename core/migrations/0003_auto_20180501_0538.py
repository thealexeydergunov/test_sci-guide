# Generated by Django 2.0.4 on 2018-05-01 05:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180501_0448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlforprocessing',
            name='created_at',
        ),
        migrations.AddField(
            model_name='resultfromparsing',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urlforprocessing',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'wait'), (2, 'process'), (3, 'success'), (4, 'error')], default=1, verbose_name='Operation status'),
        ),
    ]
