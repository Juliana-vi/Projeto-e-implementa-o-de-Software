from typing import List
import streamlit as st 

from models import Item
import ItemDAO as db

class ItemController:

    @staticmethod
    @st.cache_data
    def get_all_itens() -> List[Item]:
        return db.fetch_all_itens()

    @staticmethod
    def create_item(nome: str, descricao: str, quantidade: int):

        # 1. Cria um objeto do modelo
        new_item = Item(nome=nome, descricao=descricao, quantidade=quantidade)
        
        # 2. Passa o objeto para a camada de acesso a dados
        db.create_item(new_item)
        
        # 3. Limpa o cache para que a lista seja atualizada na próxima leitura
        st.cache_data.clear()