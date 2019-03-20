from django.contrib import admin
from .models import Quiz  # Import Quiz module


# Register Quiz module on the admin interface
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['name', 'published']

    class Meta:
        model = Quiz
        # All fields of Quiz
        fields = '__all__'
