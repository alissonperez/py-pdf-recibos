import fire
from icecream import ic

from pypdfrecibos.data import parse_csv_to_receipts
from pypdfrecibos.pdf import PDFRecibo


def generate(csvfilepath, outputfilepath, add_page_number='false'):
    items = parse_csv_to_receipts(csvfilepath)

    ic(add_page_number)

    pdf = PDFRecibo(add_page_number=add_page_number.lower().strip() == 'true')

    for item in items:
        print(f'Creating receipt for {item.client} - {item.value}')
        pdf.add_page()
        pdf.add_recipt(item)

    # Salva o arquivo
    pdf.output(outputfilepath)


if __name__ == '__main__':
  fire.Fire(generate)
