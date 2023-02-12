# Generated by Django 4.1.2 on 2023-01-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('C', 'Complicated')], max_length=20)),
                ('residential_address', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=50, null=True)),
                ('favourite_food', models.CharField(blank=True, max_length=100, null=True)),
                ('team', models.CharField(choices=[('Team A', 'A'), ('Team B', 'B')], max_length=10)),
            ],
            options={
                'ordering': ['first_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('C', 'Complicated')], max_length=20)),
                ('residential_address', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=50, null=True)),
                ('favourite_food', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['first_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('C', 'Complicated')], max_length=20)),
                ('residential_address', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=50, null=True)),
                ('favourite_food', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(choices=[('J', 'Janitors'), ('S', 'Security'), ('AP', 'Armed Personnel')], max_length=50)),
            ],
            options={
                'ordering': ['first_name'],
                'abstract': False,
            },
        ),
    ]
