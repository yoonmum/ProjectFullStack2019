from django.db import models
from django.contrib.auth.models import User

# Create your models here.   
class Binding(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Publisher(models.Model): 
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn_10 = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    binding = models.ForeignKey(Binding, on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL,null=True)
    status = models.BooleanField(default=True) 
    def __str__(self):
        return self.title+self.status

class Borrow(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    def __str__(self):
        return self.book.title + " : "+self.borrower.first_name
    
class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    actor = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Name: {} Book: {} {}".format(self.actor.fisrt_name, self.book.title,str(self.created))
        # return "Name: "+str(self.actor)+"Book: "+self.book.name +": "+ str(self.created)


    
