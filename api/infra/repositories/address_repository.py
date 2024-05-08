from flask import request
from api.entities.address_entity import Address
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from .irepository import Repository


class AddressRepository(Repository):
    def get_all():
        with DBConnection() as db:
            data = db.session.query(Address).all()
            response = [bairro.to_json() for bairro in data]
            return response_gen(
                200,
                "Endereço",
                response,
                "Lista de endereços cadastrados",
            )

    def get_by_id(id):
        with DBConnection() as db:
            data = db.session.query(Address).filter(Address.id == id)
            response = [bairro.to_json() for bairro in data]
            return response_gen(200, "Address", response)

    def update(id):
        with DBConnection() as db:
            address_obj = db.session.query(Address).filter(Address.id == id).first()
            body = request.get_json()

            try:
                if "cep" in body:
                    address_obj.cep = body["cep"]
                if "logradouro" in body:
                    address_obj.logradouro = body["logradouro"]
                if "complemento" in body:
                    address_obj.complemento = body["complemento"]
                if "bairro" in body:
                    address_obj.bairro = body["bairro"]
                if "localidade" in body:
                    address_obj.localidade = body["localidade"]
                if "uf" in body:
                    address_obj.uf = body["uf"]
                if "country" in body:
                    address_obj.country = body["country"]
                    
                db.session.add(address_obj)
                db.session.commit()
                return response_gen(
                    200,
                    "Endereço",
                    address_obj.to_json(),
                    "Dados do endereço atualizados com sucesso",
                )
            except ImportError as e:
                print("Error", e)
                return response_gen(
                    400, "Endereço", {}, "Erro ao atualizar dados do endereço"
                )

    def delete(id):
        with DBConnection() as db:
            try:
                data = db.session.query(Address).filter(Address.id == id).delete()
                db.session.commit()
                return response_gen(
                    200, "Endereço", data, "Endereço removido com sucesso"
                )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400, "Endereço", {}, "Falha ao remover proprietário"
                )

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:

                obj = Address(
                    cep=body["cep"],
                    logradouro=body["logradouro"],
                    complemento=body["complemento"],
                    bairro=body["bairro"],
                    localidade=body["localidade"],
                    uf=body["uf"],
                    country=body["country"],
                    
                )
                db.session.add(obj)
                db.session.commit()
                return response_gen(
                    200,
                    "Endereço",
                    obj.to_json(),
                    "Novo proprietário inserido com sucesso",
                )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400,
                    "Endereço",
                    {},
                    "Um erro ocorreu ao tentar inserir um novo proprietário",
                )
