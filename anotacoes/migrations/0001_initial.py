# Generated by Django 3.1.7 on 2021-04-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
