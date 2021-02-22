from datetime import datetime

from django.db import models

from tinymce.models import HTMLField


class Categories(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class News(models.Model):
    pub_date = models.DateField(default=datetime.now, blank=True)
    title = models.CharField(max_length=120, verbose_name="News title", db_index=True)
    text = HTMLField()
    categories = models.ForeignKey(Categories,
                                   on_delete=models.CASCADE,
                                   verbose_name="News categories")
    sub_categories = models.ManyToManyField(Categories,
                                            verbose_name="List for sub categories",
                                            related_name='provider')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
