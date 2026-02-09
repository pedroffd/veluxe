from services.models import Service

services_data = [
    {
        "name": "Polimento Técnico",
        "description": "Correção de pintura em múltiplos estágios para atingir o brilho máximo e remover microrriscos.",
        "price_start": 800.00,
        "icon_name": "✨",
        "is_featured": True
    },
    {
        "name": "Vitrificação Cerâmica",
        "description": "Proteção de alta durabilidade (até 3 anos) contra riscos, raios UV e sujeira. Hidrofobia extrema.",
        "price_start": 1200.00,
        "icon_name": "🛡️",
        "is_featured": True
    },
    {
        "name": "Higienização Interna Detalhada",
        "description": "Limpeza profunda de estofados, carpetes e teto, com hidratação de couro e eliminação de odores.",
        "price_start": 450.00,
        "icon_name": "couch",  # FontAwesome equivalent or emoji
        "is_featured": False
    },
    {
        "name": "Lavagem Detalhada",
        "description": "Lavagem técnica com produtos de pH neutro, descontaminação ferrosa e proteção em cera.",
        "price_start": 150.00,
        "icon_name": "droplet",
        "is_featured": False
    }
]

for item in services_data:
    Service.objects.get_or_create(name=item["name"], defaults=item)

print("Database seeded successfully!")
