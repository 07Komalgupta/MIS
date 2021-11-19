# Generated by Django 3.2.7 on 2021-11-18 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210928_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('05', 'Uttam Nagar'), ('06', 'East Azad Nagar'), ('07', 'Pitampura'), ('08', 'Kalka Ji'), ('09', 'Badarpur'), ('10', 'Dilshad Garden')], max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('time', models.TimeField()),
                ('days', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('remarks', models.CharField(max_length=155)),
                ('is_active', models.BooleanField()),
                ('examid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=120, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('fee', models.IntegerField()),
                ('duration', models.CharField(max_length=120)),
                ('hours', models.IntegerField()),
                ('class_mode', models.CharField(choices=[('online', 'online'), ('offline', 'offline'), ('weekend', 'weekend')], max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('course_exam', models.CharField(max_length=120)),
                ('main_content', models.CharField(max_length=120)),
                ('upgradation', models.CharField(max_length=120)),
                ('prerequisites', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('seats', models.IntegerField()),
                ('is_active', models.CharField(max_length=120)),
                ('is_composite', models.CharField(max_length=120)),
                ('no_of_exam', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('counselor', 'Counselor'), ('centerhead', 'Centerhead'), ('trainer', 'Trainer')], max_length=20),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=30, unique=True)),
                ('branch', models.CharField(choices=[('05', 'Uttam Nagar'), ('06', 'East Azad Nagar'), ('07', 'Pitampura'), ('08', 'Kalka Ji'), ('09', 'Badarpur'), ('10', 'Dilshad Garden')], max_length=20)),
                ('fname', models.CharField(max_length=120)),
                ('lname', models.CharField(max_length=120)),
                ('fathername', models.CharField(max_length=120)),
                ('mothername', models.CharField(max_length=120)),
                ('fatherocc', models.CharField(max_length=120)),
                ('add1', models.CharField(max_length=150)),
                ('add2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('pincode', models.IntegerField()),
                ('contact1', models.IntegerField()),
                ('contact2', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('stream', models.CharField(choices=[('arts', 'Arts'), ('commerce', 'Commerce'), ('science', 'Science'), ('humanities', 'Humanities')], max_length=10)),
                ('sch_location', models.CharField(max_length=120)),
                ('school', models.CharField(max_length=120)),
                ('adm_date', models.DateField()),
                ('totalfee', models.IntegerField()),
                ('adm_fee', models.IntegerField()),
                ('inst', models.IntegerField()),
                ('inst_amt', models.IntegerField()),
                ('inst_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.batch')),
                ('counselor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.loginuser')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.course')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleid', models.CharField(max_length=120, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('duration', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
        migrations.AddField(
            model_name='batch',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.loginuser'),
        ),
        migrations.AddField(
            model_name='batch',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.module'),
        ),
    ]
