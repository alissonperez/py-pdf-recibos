from fpdf import FPDF


class PDFRecibo(FPDF):
    def __init__(self, *args, **kwargs):
        self._add_page_number = kwargs.pop('add_page_number', True)
        print('add_page_number:', self._add_page_number)

        super().__init__(*args, **kwargs)

    def header(self):
        # Adiciona o título
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "RECIBO DE SERVIÇO", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)

        # Rodapé com número da página
        if self._add_page_number:
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def add_recipt(self, receipt):
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Recebido de: {receipt.client}", 0, 1)
        self.cell(0, 10, f"CPF/CNPJ: {receipt.document}", 0, 1)
        self.cell(0, 10, f"Endereço: {receipt.address}", 0, 1)
        self.ln(5)

        # Valor e data de pagamento
        self.cell(0, 10, f"Valor: R$ {receipt.value}", 0, 1)
        self.cell(0, 10, f"Data do Pagamento: {receipt.payment_date}", 0, 1)
        self.ln(5)

        # Descrição do serviço
        self.cell(0, 10, "Descrição do Serviço:", 0, 1)
        self.multi_cell(0, 10, receipt.service_description)
        self.ln(10)

        # Assinatura e data de emissão
        self.cell(0, 10, "Assinatura: _________________________", 0, 1)
        self.cell(0, 10, f"Nome completo: {receipt.receiver_name}", 0, 1)
        self.cell(0, 10, f"Data: {receipt.issue_date}", 0, 1)
        self.ln(10)

        # # Observações
        # self.cell(0, 10, "Observações:", 0, 1)
        # self.multi_cell(0, 10, "[Qualquer observação adicional, se necessário]")

    def add_recibo(self, cliente, cpf_cnpj, endereco, valor, data_pagamento, descricao, data_emissao):
        # Informações do cliente
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Recebido de: {cliente}", 0, 1)
        self.cell(0, 10, f"CPF/CNPJ: {cpf_cnpj}", 0, 1)
        self.cell(0, 10, f"Endereço: {endereco}", 0, 1)
        self.ln(5)

        # Valor e data de pagamento
        self.cell(0, 10, f"Valor: R$ {valor}", 0, 1)
        self.cell(0, 10, f"Data do Pagamento: {data_pagamento}", 0, 1)
        self.ln(5)

        # Descrição do serviço
        self.cell(0, 10, "Descrição do Serviço:", 0, 1)
        self.multi_cell(0, 10, descricao)
        self.ln(10)

        # Assinatura e data de emissão
        self.cell(0, 10, "Assinatura: _________________________", 0, 1)
        self.cell(0, 10, f"Data: {data_emissao}", 0, 1)
        self.ln(10)

        # Observações
        self.cell(0, 10, "Observações:", 0, 1)
        self.multi_cell(0, 10, "[Qualquer observação adicional, se necessário]")
