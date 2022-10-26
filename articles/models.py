from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)