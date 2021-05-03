from main.models import Company, Product
from main import db

"""
    Inicialização da database SQLAlchemy
    Estrutura:
        {
            "company_id": "claro_11",
            "products": [
                {"id": "claro_10", "value": 10.0},
                {"id": "claro_20", "value": 20.0}
            ]
        }

"""

C1 = Company(company_id='vivo_11')
C2 = Company(company_id='claro_11')
C3 = Company(company_id='tim_11')

P1 = Product(company=C1, id='vivo_10', value='10.0')
P2 = Product(company=C1, id='vivo_20', value='20.0')
P3 = Product(company=C2, id='claro_10', value='10.0')
P4 = Product(company=C2, id='claro_20', value='20.0')
P5 = Product(company=C3, id='tim_10', value='10.0')
P6 = Product(company=C3, id='tim_20', value='20.0')

db.session.add_all([C1, C2, C3, P1, P2, P3, P4, P5, P6])
db.session.commit()

print("Database criada com sucesso!")
