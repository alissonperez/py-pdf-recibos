import csv
from typing import List
from decimal import Decimal
from datetime import datetime

from pypdfrecibos.entities import ServiceReceipt

def parse_csv_to_receipts(file_path: str) -> List[ServiceReceipt]:
    receipts = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            receipt = ServiceReceipt(
                num=int(row.get('Número', '0')),
                client=row["Cliente"],
                document=row["CPF_CNPJ"],
                address=row["Endereço"],
                value=Decimal(row["Valor"].replace(",", ".")),  # Convert string to Decimal
                payment_date=datetime.strptime(row["Data do Pagamento"], "%d/%m/%Y").date(),
                receiver_name=row["Recebedor"],
                service_description=row["Descrição do Serviço"],
                issue_date=datetime.strptime(row["Data de Emissão"], "%d/%m/%Y").date(),
                observations=row.get("Observações", '') or ''
            )

            receipts.append(receipt)

    return receipts
