import fire
from icecream import ic

from pypdfrecibos.data import parse_csv_to_receipts
from pypdfrecibos.pdf import PDFReceipt


def generate(csvfilepath, outputfilepath, add_page_number='false'):
    items = parse_csv_to_receipts(csvfilepath)

    ic(add_page_number)

    pdf = PDFReceipt(add_page_number=add_page_number.lower().strip() == 'true')

    for i, item in enumerate(items):
        print(f'Creating receipt for {item.client} - {item.value}')
        if i % 2 == 0:
            pdf.add_page()

        pdf.add_receipt(item)

    # Salva o arquivo
    pdf.output(outputfilepath)

if __name__ == '__main__':
  fire.Fire(generate)
