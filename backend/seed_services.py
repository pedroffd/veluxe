import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from services.models import Service, ServiceFeature

def seed():
    print("Seeding detailed services...")
    
    # 1. Sequência Diamante (Combo)
    Service.objects.filter(name="Sequência Diamante").delete()
    diamante = Service.objects.create(
        name="Sequência Diamante",
        category='combo',
        description="O tratamento mais completo para quem exige perfeição absoluta.",
        price_start=4590.00,
        price_cash=4360.50,
        installment_max=4,
        warranty_time="9 meses",
        delivery_time="4 dias",
        is_featured=True
    )
    
    features = [
        "Tratamento Interno Completo",
        "Tratamento do Motor",
        "Tratamento dos Vidros",
        "Tratamento da Pintura",
        "Revestimento Nano Cerâmico (3 anos)"
    ]
    
    for i, f in enumerate(features):
        ServiceFeature.objects.create(service=diamante, description=f, order=i)

    # 2. Limpeza Preventiva
    Service.objects.filter(name="Limpeza Preventiva").delete()
    preventiva = Service.objects.create(
        name="Limpeza Preventiva",
        category='individual',
        description="Ideal para manutenção e proteção rápida.",
        price_start=350.00,
        price_cash=332.50,
        installment_max=2,
        warranty_time="7 dias",
        delivery_time="4 horas",
        icon_name="🧼"
    )
    
    features_prev = ["Limpeza germicida", "Lavagem técnica", "Proteção de carnaúba e sílica"]
    for i, f in enumerate(features_prev):
        ServiceFeature.objects.create(service=preventiva, description=f, order=i)

    # 3. Tratamento do Interior
    Service.objects.filter(name="Tratamento do Interior").delete()
    interior = Service.objects.create(
        name="Tratamento do Interior",
        category='individual',
        description="Renovação completa da cabine.",
        price_start=990.00,
        price_cash=940.50,
        installment_max=3,
        warranty_time="1 mês",
        delivery_time="1 dia",
        icon_name="💺"
    )
    
    features_int = ["Limpeza do interior", "Esterilização", "Oxi-Sanitização", "Proteção de plásticos e couros"]
    for i, f in enumerate(features_int):
        ServiceFeature.objects.create(service=interior, description=f, order=i)

    print("Database re-seeded with premium content!")

if __name__ == "__main__":
    seed()
