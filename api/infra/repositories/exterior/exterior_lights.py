from flask import request
from api.entities.checklist.exterior.exterior_lights import ExteriorLights
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class ExteriorLightsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            data = db.session.query(ExteriorLights).filter(ExteriorLights.id == id)

            try:
                if data:
                    for exterior_lights in data:
                        response = {"exterior_lights": exterior_lights.to_json()}
                    return response_gen(
                        200, "Exterior lights checklist inspection", response
                    )
            except Exception as exception:
                print(exception)
                return response_gen(204, "No content for Exterior Lights", {})

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            body = request.get_json()
            data = (
                db.session.query(ExteriorLights).filter(ExteriorLights.id == id).first()
            )

            try:
                exterior_lights = ExteriorLights(
                    front_end_lights=body["front_end_lights"],
                    back_end_lights=body["back_end_lights"],
                    side_exterior_lights=body["side_exterior_lights"],
                    hazard_lights=body["hazard_lights"],
                    auto_on_off_lightning=body["auto_on_off_lightning"],
                    trailer_lamp_connector=body["trailer_lamp_connector"],
                )
                data.front_end_lights = exterior_lights.front_end_lights
                data.back_end_lights = exterior_lights.back_end_lights
                data.side_exterior_lights = exterior_lights.side_exterior_lights
                data.hazard_lights = exterior_lights.hazard_lights
                data.auto_on_off_lightning = exterior_lights.auto_on_off_lightning
                data.trailer_lamp_connector = exterior_lights.trailer_lamp_connector
                
                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Exterior Lights inspection successfully updated",
                    data.to_json(),
                )

            except Exception as exception:
                print(exception)
                return response_gen(
                    400, "Error while trying to update the group Exterior Lights", {}
                )
