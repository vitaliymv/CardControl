# Generated by Django 4.0.6 on 2022-07-14 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=3)),
                ('number', models.PositiveBigIntegerField()),
                ('release_date', models.DateTimeField()),
                ('activity_end_date', models.DateTimeField()),
                ('cvv', models.IntegerField(max_length=3)),
                ('funds', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
            ],
        ),
    ]
