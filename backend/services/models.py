from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_start = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço inicial (A partir de)")
    icon_name = models.CharField(max_length=50, help_text="Nome do ícone (ex: format-paint)")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5, help_text="Nota de 1 a 5")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"
