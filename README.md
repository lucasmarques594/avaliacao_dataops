# Desafio DataOps - Processo Seletivo

Este repositório contém a resolução do teste prático para a vaga de DataOps. O projeto consiste em popular um banco de dados MongoDB com dados de veículos e, em seguida, executar uma agregação para agrupar os dados por país de origem da montadora.

## Ferramentas Utilizadas

*   Python 3
*   Pandas
*   PyMongo
*   MongoDB

## Estrutura do Repositório

*   `Avaliacao_DataOps_Respondida.docx`: Documento com a autoavaliação e respostas sobre o desafio.
*   `popular_banco.py`: Script Python para criar os DataFrames e popular as collections `Carros` e `Montadoras` no MongoDB.
*   `agregacao.js`: Script contendo o pipeline de agregação do MongoDB para relacionar e agrupar os dados.
*   `export/`: Pasta contendo os arquivos de dados.
    *   `Carros.json`: Exportação da collection `Carros`.
    *   `Montadoras.json`: Exportação da collection `Montadoras`.
    *   `resultado_agregacao.json`: Arquivo JSON com o output final da agregação.

## Como Executar

**Pré-requisitos:** Ter o MongoDB e o Python 3 instalados.

1.  **Instalar dependências:**
    ```bash
    pip install pandas pymongo
    ```

2.  **Popular o Banco de Dados:**
    Execute o script Python para inserir os dados no MongoDB.
    ```bash
    python popular_banco.py
    ```

3.  **Executar a Agregação:**
    Abra o `mongosh`, conecte-se ao banco `avaliacao_dataops` e cole o conteúdo do arquivo `agregacao.js` para ver o resultado.

---
Obrigado pela oportunidade!