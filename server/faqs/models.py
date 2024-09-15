from django.db import models

class FruitFAQ(models.Model):
    fruit_name = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fruit_name
