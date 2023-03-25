from django.db import models
from datetime import date

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    last_updated = models.DateTimeField(auto_now=True)
    short_description = models.TextField(max_length=200)
    description = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)