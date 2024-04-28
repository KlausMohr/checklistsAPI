from flask import request
from api.entities.checklist.hybrid_entity import Hybrid
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class HybridRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Hybrid).filter(Hybrid.id == id)
            try:
                if data:
                    for hybrid in data:
                        response = {"hybrid": hybrid.to_json()}
                return response_gen(200, "Hybrid", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Hybrid", response)

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    hybrid = Hybrid(
                        hybrid_cooling_system=body["hybrid_cooling_system"],
                        switchable_powertrain_mount=body["switchable_powertrain_mount"],
                        hybrid_entertainment_information_display=body[
                            "hybrid_entertainment_information_display"
                        ],
                        power_outlet_low_voltage=body["power_outlet_low_voltage"],
                    )
                    db.session.add(hybrid)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Hybrid",
                        hybrid.to_json(),
                        "Hybrid checklist inspection successfully inserted",
                    )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(
                    400,
                    "Hybrid",
                    {},
                    "Error while inserting a new Hybrid checklist inspection",
                )

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Hybrid).filter(Hybrid.id == id).first()

            body = request.get_json()

            try:
                hybrid = Hybrid(
                    hybrid_cooling_system=body["hybrid_cooling_system"],
                    switchable_powertrain_mount=body["switchable_powertrain_mount"],
                    hybrid_entertainment_information_display=body[
                        "hybrid_entertainment_information_display"
                    ],
                    power_outlet_low_voltage=body["power_outlet_low_voltage"],
                )

                data.hybrid_cooling_system = hybrid.hybrid_cooling_system
                data.switchable_powertrain_mount = hybrid.switchable_powertrain_mount
                data.hybrid_entertainment_information_display = (
                    hybrid.hybrid_entertainment_information_display
                )
                data.power_outlet_low_voltage = hybrid.power_outlet_low_voltage

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Hybrid",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )
