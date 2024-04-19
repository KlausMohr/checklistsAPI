from flask import request
from api.entities.owner_entity import Owner
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from .irepository import Repository


class OwnerRepository(Repository):
    def get_all():
        with DBConnection() as db:
            data = db.session.query(Owner).all()
            response = [owner.to_json() for owner in data]
            return response_gen(
                200,
                "Proprietários",
                response,
                "Lista de todos os proprietários cadastrados",
            )

    def get_by_id(id):
        with DBConnection() as db:
            data = db.session.query(Owner).filter(Owner.id == id)
            response = [owner.to_json() for owner in data]
            return response_gen(200, "Proprietário", response)

    def update(id):
        with DBConnection() as db:
            owner_obj = db.session.query(Owner).filter(Owner.id == id).first()
            body = request.get_json()

            try:
                if "name" in body:
                    owner_obj.name = body["name"]
                if "cpf" in body:
                    owner_obj.cpf = body["cpf"]
                if "birthday" in body:
                    owner_obj.birthday = body["birthday"]
                if "address" in body:
                    owner_obj.address = body["address"]
                if "email" in body:
                    owner_obj.email = body["email"]
                if "telephone" in body:
                    owner_obj.telephone = body["telephone"]

                db.session.add(owner_obj)
                db.session.commit()
                return response_gen(
                    200,
                    "Proprietário",
                    owner_obj.to_json(),
                    "Dados do proprietário atualizados com sucesso",
                )
            except ImportError as e:
                print("Error", e)
                return response_gen(
                    400, "Proprietário", {}, "Erro ao atualizar dados do proprietário"
                )

    def delete(id):
        with DBConnection() as db:
            try:
                data = db.session.query(Owner).filter(Owner.id == id).delete()
                db.session.commit()
                return response_gen(
                    200, "Proprietário", data, "Proprietário removido com sucesso"
                )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400, "Proprietário", {}, "Falha ao remover proprietário"
                )

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:

                owner = Owner(
                    name=body["name"],
                    cpf=body["cpf"],
                    birthday=body["birthday"],
                    address=body["address"],
                    email=body["email"],
                    telephone=body["telephone"],
                )
                db.session.add(owner)
                db.session.commit()
                return response_gen(
                    200,
                    "Proprietário",
                    owner.to_json(),
                    "Novo proprietário inserido com sucesso",
                )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400,
                    "Proprietário",
                    {},
                    "Um erro ocorreu ao tentar inserir um novo proprietário",
                )
