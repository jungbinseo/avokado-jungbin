# Generated by Django 2.0.2 on 2018-03-12 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_pallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classified', models.CharField(choices=[('계약처', '계약처')], max_length=5)),
                ('type', models.CharField(choices=[('납품(직송포함)', '납품')], max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('pallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Pallet')),
            ],
        ),
    ]