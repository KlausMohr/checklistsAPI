from api.entities.checklist.exterior_entity import Exterior
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class ExteriorRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Exterior).filter(Exterior.id == id)

            try:
                if data:
                    for exterior in data:
                        response = {"exterior": exterior.to_json()}

                return response_gen(200, "Exterior items", response)
            except Exception as exception:
                print(exception)
                db.session.rollback()
                return response_gen(204, "Exterior items no content!", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError
        # with DBConnection() as db:
        #     try:
        #         db.session.query().with_entities(Exterior).filter(
        #             Exterior.id == id
        #         ).delete()
        #         db.session.commit()
        #         return response_gen(200, "Checklist successfully deleted")
        #     except:
        #         db.session.rollback()
        #         return response_gen(400, "Delete process not possible")

    def update(id):
        raise NotImplementedError
