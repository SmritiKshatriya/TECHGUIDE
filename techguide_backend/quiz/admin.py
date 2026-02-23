from django.contrib import admin

from .models import ChoiceDomainScore, Domain, QuizChoice, QuizQuestion


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ChoiceDomainScoreInline(admin.TabularInline):
    model = ChoiceDomainScore
    extra = 0


class QuizChoiceInline(admin.TabularInline):
    model = QuizChoice
    extra = 1
    show_change_link = True


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'order')
    list_filter = ('category',)
    list_editable = ('order',)
    ordering = ('category', 'order')
    inlines = [QuizChoiceInline]
    search_fields = ('question_text',)


@admin.register(QuizChoice)
class QuizChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'order')
    list_filter = ('question__category',)
    list_editable = ('order',)
    ordering = ('question', 'order')
    inlines = [ChoiceDomainScoreInline]
    search_fields = ('choice_text',)


@admin.register(ChoiceDomainScore)
class ChoiceDomainScoreAdmin(admin.ModelAdmin):
    list_display = ('choice', 'domain', 'score')
    list_filter = ('domain',)
    search_fields = ('choice__choice_text', 'domain__name')
