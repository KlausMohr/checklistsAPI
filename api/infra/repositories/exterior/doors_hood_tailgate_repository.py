from flask import request
from api.entities.checklist.exterior.doors_hood_tailgate import DoorsHoodTailgate
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class DoorsHoodTailgateRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query(DoorsHoodTailgate).filter(
                DoorsHoodTailgate.id == id
            )
            try:
                if data:
                    for doors_hood_tailgate in data:
                        response = {
                            "doors_hood_tailgate": doors_hood_tailgate.to_json()
                        }
                return response_gen(200, "Doors, Hood and Tailgate", response)
            except Exception as exception:
                print(exception)
                return response_gen(
                    204,
                    "No content found for Doors, Hood and Tailgate inspection",
                    response,
                )

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    dht_obj = DoorsHoodTailgate(
                        doors_alignmet=body["doors_alignmet"],
                        doors_hinges=body["doors_hinges"],
                        roof_inspection=body["roof_inspection"],
                        hood_alignment=body["hood_alignment"],
                        hood_release=body["hood_release"],
                        hood_hinges=body["hood_hinges"],
                        hood_gass_struts=body["hood_gass_struts"],
                        tailgate_alignment=body["tailgate_alignment"],
                        trunk_gass_struts=body["trunk_gass_struts"],
                        power_lift_gate_operation=body["power_lift_gate_operation"],
                    )
                    db.session.add(dht_obj)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Doors, Hood and Tailgate",
                        dht_obj.to_json(),
                        "Doors, Hood and Tailgate inspection successfully inserted",
                    )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400,
                    "Proprietário",
                    {},
                    "Um erro ocorreu ao tentar inserir um novo proprietário",
                )

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(DoorsHoodTailgate)
                .filter(DoorsHoodTailgate.id == id)
                .first()
            )
            body = request.get_json()

            try:
                dht_obj = DoorsHoodTailgate(
                    doors_alignmet=body["doors_alignmet"],
                    doors_hinges=body["doors_hinges"],
                    roof_inspection=body["roof_inspection"],
                    hood_alignment=body["hood_alignment"],
                    hood_release=body["hood_release"],
                    hood_hinges=body["hood_hinges"],
                    hood_gass_struts=body["hood_gass_struts"],
                    tailgate_alignment=body["tailgate_alignment"],
                    trunk_gass_struts=body["trunk_gass_struts"],
                    power_lift_gate_operation=body["power_lift_gate_operation"],
                )
                data.doors_alignmet = dht_obj.doors_alignmet
                data.doors_hinges = dht_obj.doors_hinges
                data.roof_inspection = dht_obj.roof_inspection
                data.hood_alignment = dht_obj.hood_alignment
                data.hood_release = dht_obj.hood_release
                data.hood_hinges = dht_obj.hood_hinges
                data.hood_gass_struts = dht_obj.hood_gass_struts
                data.tailgate_alignment = dht_obj.tailgate_alignment
                data.trunk_gass_struts = dht_obj.trunk_gass_struts
                data.power_lift_gate_operation = dht_obj.power_lift_gate_operation

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Doors, Hood and Tailgate inspection successfully updated",
                    data.to_json(),
                )

            except Exception as exception:
                print(exception)
                return response_gen(
                    400,
                    "Error while trying to update the group Doors, Hood and Tailgate inspection",
                    {},
                )
