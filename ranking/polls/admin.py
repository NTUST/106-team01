from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Store, Drink, Cate

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('drink_name', 'price', 'category','store')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Store)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Cate)