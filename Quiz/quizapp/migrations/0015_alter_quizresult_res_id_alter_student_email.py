# Generated by Django 4.1.7 on 2023-05-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0014_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='res_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
