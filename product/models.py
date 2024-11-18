from django.db import models

# Create your models here.


class foto (models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "fotos"

    def __str__(self):
        return self.title
    

