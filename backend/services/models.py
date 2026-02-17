from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('combo', 'Combo (Sequência)'),
        ('individual', 'Tratamento Individual'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='individual')
    description = models.TextField()
    price_start = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço inicial (A partir de)")
    price_cash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Preço à vista (com desconto)")
    installment_max = models.IntegerField(default=1, help_text="Número máximo de parcelas")
    
    warranty_time = models.CharField(max_length=50, blank=True, help_text="Ex: 9 meses, 3 anos")
    delivery_time = models.CharField(max_length=50, blank=True, help_text="Ex: 4 dias, 4 horas")
    
    icon_name = models.CharField(max_length=50, blank=True, help_text="Nome do ícone ou Emoji")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.name}"

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.service.name} - {self.description}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5, help_text="Nota de 1 a 5")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"
