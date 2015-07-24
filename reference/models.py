from django.db import models

# Create your models here.
class Reference(models.Model):
    URL = 1
    BOOK = 2
    PAPER = 3
    TYPES_OF_REFS = (
                    (URL, 'URL'),
                    (BOOK, 'Book'),
                    (PAPER, 'Research Paper'), 
                    )
    #Reference URL (can be blank)
    url = models.URLField(null=True, blank=True)
    #Reference title
    title = models.CharField(max_length=255)
    #Reference type: It could be a many-to-many field later.
    type = models.PositiveSmallIntegerField(choices=TYPES_OF_REFS, default=URL)
    #Page Number (Relevant only for books)
    page = models.PositiveIntegerField(null=True,blank=True)
    