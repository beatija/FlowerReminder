# Generated by Django 2.0.6 on 2018-06-09 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_auto_20180609_0818'),
        ('waterreminder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='flower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flower.Flower'),
            preserve_default=False,
        ),
    ]
