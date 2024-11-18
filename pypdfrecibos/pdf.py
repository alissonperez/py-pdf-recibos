from fpdf import FPDF


class PDFReceipt(FPDF):

    def __init__(self, add_page_number):
        super().__init__(format='A4', orientation='P')

        self._add_page_number = add_page_number

        self._first_item_in_page = True

        # Dimensions for A4 in points (mm)
        self._page_width = 210  # Width in mm
        self._page_height = 297  # Height in mm

    def add_receipt(self, receipt):
        if self._first_item_in_page:
            self.set_xy(10, 10)
            self._first_item_in_page = False
        else:
            self.set_xy(10, (self._page_height / 2))
            self._first_item_in_page = True

        self.set_font('Arial', 'B', 12)
        self.cell(0, 0, 'RECIBO DE SERVIÇO', 0, 1, 'C')
        self.ln(10)

        # Line 1
        self._write_item('Recebido de: ', receipt.client, 50, 70)
        self._write_item('CPF: ', receipt.document, 30, ln=True)

        # Line 2
        self._write_item('Endereço: ', receipt.address, ln=True)

        # Line 3
        self._write_item('Valor: ', f'R$ {receipt.value:,.2f}', val_width=70)
        self._write_item('Na data: ', receipt.payment_date.strftime('%d/%m/%Y'), 30, ln=True)

        # Line 4 and 5 (description)
        self._field('Descrição do Serviço:', 0, align='L', ln=True)
        self._value(receipt.service_description, 0, ln=True, multi=True)
        self.set_y(self.get_y() + 7)

        if receipt.observations != '':
            self._field('Observações:', 0, align='L', ln=True)
            self._value(receipt.observations, 0, ln=True, multi=True)
            self.set_y(self.get_y() + 7)

        self._write_item('Assinatura: ', '__________________________________________________', ln=True)
        self._write_item('Nome completo: ', receipt.receiver_name, ln=True)
        self._write_item('Data: ', receipt.issue_date.strftime('%d/%m/%Y'))

    def _write_item(self, field, value, field_width=50, val_width=0, ln=False):
        self._field(field, field_width)
        self._value(value, val_width, ln=ln)

    def _field(self, field, width, align='R', ln=False):
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(220, 220, 220)
        self.cell(width, 6, field, border=0, align=align, fill=True)

        if ln:
            self.ln(7)

    def _value(self, value, width, ln=False, multi=False):
        self.set_fill_color(255, 255, 255)
        self.set_font('Arial', '', 10)

        if not multi:
            self.cell(width, 7, value)
        else:
            self.multi_cell(width, 7, value)

        if ln:
            self.ln(7)
