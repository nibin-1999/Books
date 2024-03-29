from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to="books/images")
    author = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    is_favourite = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book=models.ForeignKey("books.book",on_delete=models.CASCADE)
    user= models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date= models.DateTimeField()
    comment= models.TextField()
    
    class Meta:
        db_table = "books_comment"
    
    def __str__(self):
        return str(self.id)