from django.db import models


# Create your models here.

class Student(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user_id}: {self.username}"


class Creator(models.Model):
    creator_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    username = models.CharField(max_length=255)


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    creator_id = models.ForeignKey(Creator, on_delete=models.CASCADE)


class Question(models.Model):
    qa_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Variant(models.Model):
    v_id = models.AutoField(primary_key=True)
    variant = models.CharField(max_length=255)
    qa_id = models.ForeignKey(Question, on_delete=models.CASCADE)

class QuizResult(models.Model):
    res_id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    score = models.IntegerField()
