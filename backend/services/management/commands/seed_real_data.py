from django.core.management.base import BaseCommand
from services.models import Service, ServiceFeature
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds real service data from AoRaboni'

    def handle(self, *args, **options):
        self.stdout.write("Cleaning existing services...")
        Service.objects.all().delete()

        services_data = [
            {
                "name": "Sequência Rubi",
                "category": "combo",
                "description": "Proteção de até 5 anos com correção total dos defeitos da pintura. O pináculo do detalhamento automotivo.",
                "price_start": Decimal("6290.00"),
                "price_cash": Decimal("5975.50"),
                "installment_max": 5,
                "warranty_time": "12 meses",
                "delivery_time": "5 dias",
                "is_featured": True,
                "features": [
                    "Tratamento dos Faróis",
                    "Vitrificação de plásticos",
                    "Tratamento das Rodas e Caixas de Rodas",
                    "Correção total de pintura",
                    "Proteção de até 5 anos (Graphene Coating)"
                ]
            },
            {
                "name": "Sequência Diamante",
                "category": "combo",
                "description": "Proteção de até 3 anos com correção de pintura avançada.",
                "price_start": Decimal("4590.00"),
                "price_cash": Decimal("4360.50"),
                "installment_max": 4,
                "warranty_time": "9 meses",
                "delivery_time": "4 dias",
                "is_featured": True,
                "features": [
                    "Tratamento dos Vidros",
                    "Tratamento da Pintura",
                    "Revestimento Nano Cerâmico (3 anos)"
                ]
            },
            {
                "name": "Sequência Bronze",
                "category": "combo",
                "description": "Proteção de até 1 ano com brilho intenso e proteção cerâmica básica.",
                "price_start": Decimal("3590.00"),
                "price_cash": Decimal("3410.50"),
                "installment_max": 3,
                "warranty_time": "8 meses",
                "delivery_time": "3 dias",
                "features": [
                    "Tratamento da Pintura",
                    "Revestimento Nano Cerâmico (1 ano)"
                ]
            },
            {
                "name": "Limpeza Preventiva (Sem Proteção)",
                "category": "individual",
                "description": "Limpeza detalhada para veículos que não possuem proteção prévia.",
                "price_start": Decimal("350.00"),
                "installment_max": 1,
                "warranty_time": "7 dias",
                "delivery_time": "4 horas",
                "features": [
                    "Limpeza germicida",
                    "Lavagem técnica",
                    "Proteção de carnauba e sílica"
                ]
            },
            {
                "name": "Tratamento do Interior",
                "category": "individual",
                "description": "Limpeza profunda, esterilização e proteção de todas as superfícies internas.",
                "price_start": Decimal("990.00"),
                "installment_max": 1,
                "warranty_time": "1 mês",
                "delivery_time": "1 dia",
                "features": [
                    "Limpeza do interior",
                    "Esterilização",
                    "Oxi-Sanitização",
                    "Proteção de plásticos e borrachas",
                    "Proteção de couro e tecidos"
                ]
            },
            {
                "name": "Tratamento de Pintura (Ceramic 5 anos)",
                "category": "individual",
                "description": "Correção de pintura personalizada com vitrificação de longa duração.",
                "price_start": Decimal("3690.00"),
                "installment_max": 1,
                "warranty_time": "5 anos",
                "delivery_time": "4 dias",
                "features": [
                    "Aumento de brilho e correção",
                    "Projeto personalizado",
                    "Limpeza germicida",
                    "Vitrificação de 5 anos"
                ]
            }
        ]

        for s_data in services_data:
            features = s_data.pop('features', [])
            service = Service.objects.create(**s_data)
            for idx, feature_desc in enumerate(features):
                ServiceFeature.objects.create(
                    service=service,
                    description=feature_desc,
                    order=idx
                )
            self.stdout.write(self.style.SUCCESS(f'Created service: {service.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded REAL services!'))
