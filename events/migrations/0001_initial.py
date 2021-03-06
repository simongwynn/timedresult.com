# Generated by Django 3.0.8 on 2020-08-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='events/images/')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('discipline', models.CharField(choices=[('RD', 'Road'), ('TR', 'Track'), ('CX', 'Cyclo-Cross'), ('MTB', 'Mountain-Bike'), ('GR', 'Gravel Bike')], default='RD', max_length=3)),
            ],
        ),
    ]
