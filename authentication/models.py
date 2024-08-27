from django.db import models

# Create your models here.

class SıgnUpToken(models.Model):
    token = models.CharField(max_length=10)
    expiration_date = models.DateTimeField()
    
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    
    def __str__(self) -> str:
        return self.token