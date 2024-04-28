from flask import request
from api.entities.checklist.interior.luggage_compartment import LuggageCompartment
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class LuggageCompartmentRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(LuggageCompartment)
                .filter(LuggageCompartment.id == id)
            )
            try:
                if data:
                    for luggage_compartment in data:
                        response = {
                            "luggage_compartment": luggage_compartment.to_json()
                        }
                return response_gen(200, "Luggage comparment", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Luggage comparment", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(LuggageCompartment)
                .filter(LuggageCompartment.id == id)
                .first()
            )

            body = request.get_json()

            try:
                luggage_compartment = LuggageCompartment(
                    luggage_carpet=body["luggage_carpet"],
                    luggage_trim=body["luggage_trim"],
                    luggage_light=body["luggage_light"],
                    jack_tool_kit=body["jack_tool_kit"],
                    spare_tire_inspection=body["spare_tire_inspection"],
                    spare_tire_airpressure=body["spare_tire_airpressure"],
                    tire_inflator_kit=body["tire_inflator_kit"],
                    emergency_trunk_lid=body["emergency_trunk_lid"],
                )

                data.luggage_carpet = luggage_compartment.luggage_carpet
                data.luggage_trim = luggage_compartment.luggage_trim
                data.luggage_light = luggage_compartment.luggage_light
                data.jack_tool_kit = luggage_compartment.jack_tool_kit
                data.spare_tire_inspection = luggage_compartment.spare_tire_inspection
                data.spare_tire_airpressure = luggage_compartment.luggage_light
                data.tire_inflator_kit = luggage_compartment.tire_inflator_kit
                data.emergency_trunk_lid = luggage_compartment.emergency_trunk_lid

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Luggage comparment",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )
