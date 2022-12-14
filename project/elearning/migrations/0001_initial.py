# Generated by Django 4.0.4 on 2022-06-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('ects', models.IntegerField()),
                ('sem_reg', models.IntegerField()),
                ('sem_ext', models.IntegerField()),
                ('elective', models.CharField(choices=[('DA', 'da'), ('NE', 'ne')], max_length=50)),
            ],
        ),
    ]
