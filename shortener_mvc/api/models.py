from django.db import models
import hashlib
import random

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
        url_hash = hashlib.sha256(self.original_url.encode()).hexdigest()
        start_index = random.randint(0, len(url_hash) - 8)
        short_code = url_hash[start_index:start_index + 8]
        return short_code

    def generate_admin_token(self):
        salt = "my-salt-text"
        url_hash = hashlib.sha256(salt.encode() + self.original_url.encode()).hexdigest()
        return url_hash[:16]
