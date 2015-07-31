from django.db import models
import blogging

# Create your models here.
class Reference(models.Model):
    URL = 1
    BOOK = 2
    PAPER = 3
    PUBLICATION = 4
    TYPES_OF_REFS = (
                    (URL, 'URL'),
                    (BOOK, 'Book'),
                    (PAPER, 'Research Paper'), 
                    (PUBLICATION, 'Online Publication'))
    #Reference URL (can be blank)
    url = models.URLField(null=True, blank=True)
    #Reference title
    content = models.CharField(max_length=500)
    #Reference type: It could be a many-to-many field later.
    type = models.PositiveSmallIntegerField(choices=TYPES_OF_REFS, default=URL)
    #Parent Article
    parent = models.ForeignKey(blogging.models.BlogContent, related_name="reference") 
    
    