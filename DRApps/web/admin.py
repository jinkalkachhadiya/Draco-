from django.contrib import admin
from .models import Manga, Chapter

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('manga', 'chapter_number', 'title')
