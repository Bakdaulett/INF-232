# Generated by Django 4.2.1 on 2023-05-13 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_alter_quiz_creator_id_alter_variant_qa_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='qa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.question'),
        ),
    ]