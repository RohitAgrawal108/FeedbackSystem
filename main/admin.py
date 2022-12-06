from django.contrib import admin
from .models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','description','category', 'date')
    search_fields = ('description', 'category', 'date',)

    list_per_page = 5

admin.site.register(Feedback, FeedbackAdmin)