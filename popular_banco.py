import pandas as pd
from pymongo import MongoClient
from typing import Dict, Any, List

def criar_dataframes() -> (pd.DataFrame, pd.DataFrame):
    dados_carros = {
        'Carro':['Onix','Polo','Sandero','Fiesta','City'],
        'Cor': ['Prata','Branco', 'Prata', 'Vermelho','Preto'],
        'Montadora': ['Chevrolet','Volkswagen', 'Renault', 'Ford', 'Honda']
    }
    df_carros = pd.DataFrame(dados_carros)
    print("DataFrame 'Carros' criado:")
    print(df_carros)
    print("-" * 30)

    dados_montadoras = {
        'Montadora': ['Chevrolet','Volkswagen', 'Renault', 'Ford', 'Honda'],
        'Pais': ['EUA','Alemanha','França','EUA','Japão']
    }

    df_montadoras = pd.DataFrame(dados_montadoras)
    print("Data 'Montadoras' criado:")
    print(df_montadoras)
    print("-" * 30)

    return df_carros, df_montadoras

def salvar_no_mongodb(df: pd.DataFrame, collection_name: str, db: Any):
    collection = db[collection_name]
    collection.delete_many({})
    records = df.to_dict('records')
    collection.insert_many(records)
    print(f"{len(records)} documentos inseridos na collection '{collection_name}'")

def main():
    MONGO_URI= "mongodb://localhost:27017/"
    DATABASE_NAME = "avaliacao_dataops" 

    try:
        df_carros, df_montadoras = criar_dataframes()

        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]

        print(f"Conectado ao MongoDB no banco '{DATABASE_NAME}'.")

        salvar_no_mongodb(df_carros, "Carros", db)
        salvar_no_mongodb(df_montadoras, "Montadoras", db)

        print("\nProcesso concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if 'client' in locals() and client:
            client.close()
            print("Conexão com o MongoDB fechada.")

if __name__ == "__main__":
    main()