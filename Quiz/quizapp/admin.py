from django.contrib import admin
from .models import *

# Register your models here.



class MemberAdmin(admin.ModelAdmin):
    list_display = ("creator_id", "email", "username")

class MemberAdmin2(admin.ModelAdmin):
    list_display = ("user_id", "username", "email")

class MemberAdmin3(admin.ModelAdmin):
    list_display = ("quiz_id", "topic", "creator_id")

class MemberAdmin4(admin.ModelAdmin):
    list_display = ("qa_id", "question", "answer", "quiz_id")

class MemberAdmin5(admin.ModelAdmin):
    list_display = ("v_id", "variant", "qa_id")

class MemberAdmin6(admin.ModelAdmin):
    list_display = ("res_id", "quiz_id", "student_id", "score")



admin.site.register(Creator, MemberAdmin)
admin.site.register(Student, MemberAdmin2)
admin.site.register(Quiz, MemberAdmin3)
admin.site.register(Question, MemberAdmin4)
admin.site.register(Variant, MemberAdmin5)
admin.site.register(QuizResult, MemberAdmin6)
