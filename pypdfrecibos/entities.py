from datetime import date
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class ServiceReceipt:
    client: str
    document: str  # CPF/CNPJ
    address: str
    value: Decimal
    payment_date: date
    receiver_name: str
    service_description: str
    issue_date: date
    observations: str = ''
