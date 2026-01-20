from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Register Question Inline and Choice Inline classes here

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register Question Admin and Lesson Admin classes here

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['text', 'lesson_id', 'grade']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

# Register Course Admin and Instructor Admin classes here

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
