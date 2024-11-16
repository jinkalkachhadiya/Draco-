# web/views.py
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Manga
from django.template import loader
from .models import Chapter
from DRApps.user.views import *


def manga_list(request):
    # Fetch all manga from the database
    mangas = Manga.objects.all()
    return render(request, 'user/web_home.html', {'mangas': mangas})
def manga_detail(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    chapters = manga.chapters.all()  # Get all chapters related to the manga
    total_chapters = chapters.count()  # Count total chapters
    return render(request, 'user/manga_detail.html', {
        'manga': manga,
        'chapters': chapters,
        'total_chapters': total_chapters
    })
def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, 'chapter_detail.html', {'chapter': chapter})

def chapter_pdf(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    pdf_file = chapter.pdf_file

    # Open the PDF file and return it as a response
    with open(pdf_file.path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={pdf_file.name}'
        return response