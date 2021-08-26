# Generated by Django 3.1.2 on 2021-08-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usingCode', models.CharField(max_length=10)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userIncentive', models.IntegerField(default=0)),
                ('referalEmail', models.EmailField(max_length=254)),
                ('referalIncentive', models.IntegerField(default=0)),
            ],
        ),
    ]
