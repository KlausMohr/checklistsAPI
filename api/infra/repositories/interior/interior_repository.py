from flask import request
from api.entities.checklist.interior_entity import Interior
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class InteriorRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Interior).filter(Interior.id == id)

            try:
                if data:
                    for interior in data:
                        response = {"Interior": interior.to_json()}

                return response_gen(200, "Interior items", response)
            except Exception as exception:
                print(exception)
                db.session.rollback()
                return response_gen(204, "No content for Interior items", response)

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    interior = Interior(
                        
                    )
                    db.session.add(interior)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Interior",
                        interior.to_json(),
                        "Interior checklist inspection successfully inserted",
                    )
            except Exception as exception:
                print("Error: ", exception)
                return response_gen(
                    400,
                    "Interior",
                    {},
                    "Error while inserting a new Interior checklist inspection",
                )

    def delete(id):
        raise NotImplementedError
        # with DBConnection() as db:
        #     try:
        #         db.session.query().with_entities(Interior).filter(
        #             Interior.id == id
        #         ).delete()
        #         db.session.commit()
        #         return response_gen(200, "Checklist successfully deleted")
        #     except:
        #         db.session.rollback()
        #         return response_gen(400, "Delete process not possible")

    def update(id):
        raise NotImplementedError
