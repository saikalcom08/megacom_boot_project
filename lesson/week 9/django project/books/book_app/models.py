from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    inn = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    publish_date = models.DateField()

    def __str__(self):
        return f'{self.name}-->{self.inn}'

class ImageBook(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_book')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image.url}'