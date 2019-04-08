"""DJANGO HONEYWORDS MODELS
honeywords/models.py

"""
from django.db import models

class Sweetwords(models.Model):
    """Sweetwords

    Model containing user-specific salt as key, along with the user's
    associated sweetwords.
    
    """
    salt = models.CharField(
        max_length=128,
        help_text="Salt associated with user's account",
        )
    sweetwords = models.CharField(
        max_length=65536,
        help_text="Sweetwords associated with user's account",
        )

    class Meta:
        verbose_name_plural = 'sweetwords'

    def __str__(self):
        return self.salt
