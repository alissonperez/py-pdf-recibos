import fire

from pypdfrecibos.data import parse_csv_to_receipts

from icecream import ic


def generate(csvfilepath):
    items = parse_csv_to_receipts(csvfilepath)
    ic(items)

if __name__ == '__main__':
  fire.Fire(generate)
