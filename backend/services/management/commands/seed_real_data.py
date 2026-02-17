from django.core.management.base import BaseCommand
from services.models import Service, ServiceFeature
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds full real service data from AoRaboni (16+ services)'

    def handle(self, *args, **options):
        self.stdout.write("Cleaning existing services...")
        Service.objects.all().delete()

        services_data = [
            # COMBOS (SEQUÊNCIAS)
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
                "price_start": Decimal("3990.00"),
                "price_cash": Decimal("3790.50"),
                "installment_max": 4,
                "warranty_time": "9 meses",
                "delivery_time": "4 dias",
                "is_featured": True,
                "features": [
                    "Tratamento dos Vidros",
                    "Tratamento da Pintura",
                    "Revestimento Nano Cerâmico (3 anos)",
                    "Tratamento Interno Premium"
                ]
            },
            {
                "name": "Sequência Bronze",
                "category": "combo",
                "description": "Proteção de até 1 ano com brilho intenso e proteção cerâmica básica.",
                "price_start": Decimal("2990.00"),
                "price_cash": Decimal("2840.50"),
                "installment_max": 3,
                "warranty_time": "8 meses",
                "delivery_time": "3 dias",
                "features": [
                    "Tratamento da Pintura",
                    "Selagem Cerâmica (1 ano)",
                    "Remoção de 60% dos defeitos"
                ]
            },
            # INDIVIDUAIS - LIMPEZA E MANUTENÇÃO
            {
                "name": "Limpeza Preventiva (Carros com Proteção)",
                "category": "individual",
                "description": "Manutenção detalhada para veículos que já possuem vitrificação ou selagem.",
                "price_start": Decimal("350.00"),
                "installment_max": 2,
                "warranty_time": "7 dias",
                "delivery_time": "3 horas",
                "features": ["Lavagem técnica", "Descontaminação química", "Reforço da proteção existente"]
            },
            {
                "name": "Lavagem Técnica Detalhada",
                "category": "individual",
                "description": "Limpeza profunda de chassi, rodas e carroceria com pincéis e produtos pH neutro.",
                "price_start": Decimal("250.00"),
                "installment_max": 1,
                "delivery_time": "5 horas",
                "features": ["Limpeza de caixas de roda", "Pincelamento de emblemas", "Secagem com soprador"]
            },
            {
                "name": "Limpeza e Proteção de Motor",
                "category": "individual",
                "description": "Remoção de graxa e oxidação com proteção em verniz de motor de alta temperatura.",
                "price_start": Decimal("390.00"),
                "installment_max": 1,
                "delivery_time": "4 horas",
                "features": ["Limpeza técnica a seco/vapor", "Tratamento de plásticos e mangueiras", "Verniz protetor"]
            },
            # INDIVIDUAIS - INTERIOR
            {
                "name": "Tratamento do Interior (Higienização)",
                "category": "individual",
                "description": "Limpeza germicida de teto, bancos, carpetes e painel.",
                "price_start": Decimal("990.00"),
                "installment_max": 3,
                "warranty_time": "1 mês",
                "delivery_time": "1 dia",
                "features": ["Oxi-Sanitização", "Limpeza de extração", "Higienização de ar-condicionado"]
            },
            {
                "name": "Hidratação e Proteção de Couro",
                "category": "individual",
                "description": "Limpeza específica para couro com aplicação de condicionador ou coat cerâmico.",
                "price_start": Decimal("450.00"),
                "installment_max": 2,
                "delivery_time": "6 horas",
                "features": ["Toque seco original", "Proteção UV", "Prevenção de rachaduras"]
            },
            # INDIVIDUAIS - PROTEÇÕES ESPECÍFICAS
            {
                "name": "Tratamento de Vidros (Vitrificação)",
                "category": "individual",
                "description": "Repelência extrema de água e proteção contra chuva ácida.",
                "price_start": Decimal("290.00"),
                "installment_max": 1,
                "delivery_time": "3 horas",
                "features": ["Remoção de manchas", "Descontaminação", "Coat repelente"]
            },
            {
                "name": "Vitrificação de Rodas",
                "category": "individual",
                "description": "Proteção térmica para rodas, facilitando a limpeza de fuligem de freio.",
                "price_start": Decimal("490.00"),
                "installment_max": 2,
                "delivery_time": "6 horas",
                "features": ["Limpeza interna da roda", "Resistência a altas temperaturas", "Brilho metálico"]
            },
            {
                "name": "Revitalização de Plásticos Externos",
                "category": "individual",
                "description": "Restauração da cor original e proteção contra esbranquiçado de sol.",
                "price_start": Decimal("350.00"),
                "installment_max": 1,
                "delivery_time": "4 horas",
                "features": ["Limpeza profunda", "Vitrificador de plásticos", "Acabamento original"]
            },
            # INDIVIDUAIS - PINTURA
            {
                "name": "Polimento de Faróis",
                "category": "individual",
                "description": "Restauração da transparência e proteção contra amarelamento.",
                "price_start": Decimal("250.00"),
                "installment_max": 1,
                "delivery_time": "3 horas",
                "features": ["Lixamento técnico", "Polimento em etapas", "Verniz/Vitrificador UV"]
            },
            {
                "name": "Polimento Técnico de Brilho",
                "category": "individual",
                "description": "Remoção de micro-riscos e aumento extremo de reflexo.",
                "price_start": Decimal("1290.00"),
                "installment_max": 3,
                "delivery_time": "2 dias",
                "features": ["Etapa de corte leve", "Refino e Lustro", "Selante sintético"]
            },
            {
                "name": "Pintura de Pinças de Freio",
                "category": "individual",
                "description": "Personalização estética com tinta de alta temperatura e verniz cerâmico.",
                "price_start": Decimal("690.00"),
                "installment_max": 2,
                "delivery_time": "1 dia",
                "features": ["Limpeza mecânica", "Base primer", "Acabamento premium"]
            },
            {
                "name": "Remoção de Chuva Ácida",
                "category": "individual",
                "description": "Limpeza química de vidros para remover marcas d'água persistentes.",
                "price_start": Decimal("190.00"),
                "installment_max": 1,
                "delivery_time": "2 horas",
                "features": ["Polimento de vidros", "Limpeza ácida técnica"]
            },
            {
                "name": "Oxi-Sanitização",
                "category": "individual",
                "description": "Eliminação de fungos, bactérias e odores desagradáveis através do ozônio.",
                "price_start": Decimal("150.00"),
                "installment_max": 1,
                "delivery_time": "1 hora",
                "features": ["Higienização total do ar", "Remoção de cheiro de cigarro/animais"]
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

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(services_data)} REAL services!'))
