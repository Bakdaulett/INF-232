# Generated by Django 4.1.7 on 2023-05-14 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0012_remove_quizresult_id_remove_quizresult_quiz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='creator_id',
        ),
    ]
