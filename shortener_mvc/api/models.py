from django.db import models
import string
import random
from django.conf import settings

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=8, unique=True)
    admin_token = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        if not self.admin_token:
            self.admin_token = self.generate_admin_token()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        chars = string.ascii_letters + string.digits
        shortCode = ''.join(random.choice(chars) for _ in range(7))
        
        while URL.objects.filter(short_code=shortCode).exists():
            shortCode = ''.join(random.choice(chars) for _ in range(7))
        
        return shortCode

    def generate_admin_token(self):
        chars = string.ascii_letters + string.digits
        token = ''.join(random.choice(chars) for _ in range(16))
        
        while URL.objects.filter(admin_token=token).exists():
            token = ''.join(random.choice(chars) for _ in range(16))
        
        return token

    def get_absolute_url(self):
        return f"{settings.ALLOWED_HOSTS[0]}/{self.short_code}"