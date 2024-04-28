from flask import request
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
                return response_gen(204, "No contents for Exterior items", response)

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    exterior = Exterior(
                        body_panels_bumper_id=body["body_panels_bumper_id"],
                        door_hood_tailgate_id=body["door_hood_tailgate_id"],
                        grille_trim_roof_rack_id=body["grille_trim_roof_rack_id"],
                        glass_outside_mirrors_id=body["glass_outside_mirrors_id"],
                        exterior_lights_id=body["exterior_lights_id"],
                    )
                    db.session.add(exterior)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Exterior",
                        exterior.to_json(),
                        "Exterior checklist inspection successfully inserted",
                    )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400,
                    "Exterior",
                    {},
                    "Error while inserting a new Exterior checklist inspection",
                )

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
