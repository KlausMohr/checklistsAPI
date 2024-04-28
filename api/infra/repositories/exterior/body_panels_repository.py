from flask import request
from api.entities.checklist.exterior.body_bumpers import BodyPanelsBumper
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class BodyPanelsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(BodyPanelsBumper)
                .filter(BodyPanelsBumper.id == id)
            )
            try:
                if data:
                    for body_p_bumper in data:
                        response = {"body_panels_bumper": body_p_bumper.to_json()}
                return response_gen(
                    200, "Body, Panels and Bumpers inspection", response
                )
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Body, Panels and Bumper", response
                )

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    bodyPBumper = BodyPanelsBumper(
                        flood_damage=body["flood_damage"],
                        fire_damage=body["fire_damage"],
                        major_damage=body["major_damage"],
                        body_panel=body["body_panel"],
                        bumper=body["bumper"],
                    )
                    db.session.add(bodyPBumper)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Body, Panels and Bumper",
                        bodyPBumper.to_json(),
                        "Body, Panels and Bumper successfully inserted",
                    )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400,
                    "Body, Panels and Bumper",
                    {},
                    "Um erro ocorreu ao tentar inserir um novo proprietário",
                )

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(BodyPanelsBumper)
                .filter(BodyPanelsBumper.id == id)
                .first()
            )

            body = request.get_json()

            try:
                bodyPBumper = BodyPanelsBumper(
                    flood_damage=body["flood_damage"],
                    fire_damage=body["fire_damage"],
                    major_damage=body["major_damage"],
                    body_panel=body["body_panel"],
                    bumper=body["bumper"],
                )
                data.flood_damage = bodyPBumper.flood_damage
                data.fire_damage = bodyPBumper.fire_damage
                data.major_damage = bodyPBumper.major_damage
                data.body_panel = bodyPBumper.body_panel
                data.bumper = bodyPBumper.bumper

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Body, Panels and Bumper",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )
