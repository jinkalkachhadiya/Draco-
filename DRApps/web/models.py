from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    chapter_number = models.IntegerField()
    pdf_file = models.FileField(upload_to='chapter_pdfs/')  # PDF field remains mandatory

    def __str__(self):
        return f"{self.manga.title} - Chapter {self.chapter_number}"

