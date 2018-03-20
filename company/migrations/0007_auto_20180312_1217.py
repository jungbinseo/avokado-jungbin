# Generated by Django 2.0.2 on 2018-03-12 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date out'),
            preserve_default=False,
        ),
    ]