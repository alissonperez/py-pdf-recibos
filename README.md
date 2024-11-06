# Gerador de Recibos em PDF

Este projeto é um gerador de recibos em PDF a partir de um arquivo CSV. Ele lê dados de um arquivo CSV de exemplo e gera recibos em formato PDF automaticamente.

## Exemplo do CSV

Abaixo está um exemplo do formato do arquivo CSV que deve ser usado como entrada para o gerador de recibos.

```csv
Cliente,CPF_CNPJ,Endereço,Valor,Data do Pagamento,Descrição do Serviço,Data de Emissão,Recebedor
João da Silva,123.456.789-00,Rua Exemplo, 123 - Cidade, Estado,500,00,05/11/2024,Serviço de consultoria em desenvolvimento de software.,05/11/2024,Fulano de Tal
Maria Oliveira,987.654.321-00,Av. Central, 456 - Cidade, Estado,750,00,06/11/2024,Serviço de design gráfico para criação de logotipo.,06/11/2024,Fulano de Tal
Pedro Santos,456.789.123-00,Travessa das Flores, 789 - Cidade, Estado,300,00,07/11/2024,Serviço de manutenção em sistema de gestão.,07/11/2024,Fulano de Tal
Ana Costa,321.654.987-00,Praça das Árvores, 101 - Cidade, Estado,450,00,08/11/2024,Serviço de instalação e configuração de rede.,08/11/2024,Fulano de Tal
Carlos Pereira,789.123.456-00,Alameda das Palmeiras, 202 - Cidade, Estado,600,00,09/11/2024,Serviço de revisão e auditoria de processos.,09/11/2024,Fulano de Tal
```

## Dependências

- Python 3.12
- Poetry (para gerenciamento de dependências e ambiente virtual)

## Instalação

Para instalar as dependências e configurar o ambiente, utilize o comando abaixo:

```bash
poetry install
```

## Executando o Gerador de Recibos

Para rodar o gerador e criar o arquivo PDF com os recibos, execute o seguinte comando:

```bash
poetry run python main.py ./recibos_servicos.csv recibos.pdf
```

- `./recibos_servicos.csv`: caminho para o arquivo CSV de entrada com os dados dos recibos.
- `recibos.pdf`: nome do arquivo PDF de saída que conterá os recibos gerados.

### Exemplo de PDF (em A4)

<img width="561" alt="image" src="https://github.com/user-attachments/assets/0db0f73b-0b9d-410b-91bc-655cc2f56ce0">

## Sobre o Projeto

Este projeto foi desenvolvido para facilitar a criação de recibos em PDF a partir de dados estruturados em um arquivo CSV. Cada linha do CSV representa um recibo com informações detalhadas sobre o cliente, o valor, a data de pagamento, a descrição do serviço, a data de emissão e o nome do recebedor.
