from flask import request
from api.entities.checklist.exterior.grille_trim_roof_rack import GrilleTrimRoofRack
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class GrilleTrimRoofRackRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            data = db.session.query(GrilleTrimRoofRack).filter(
                GrilleTrimRoofRack.id == id
            )

            try:
                if data:
                    for grille_trim_roof_rack in data:
                        response = {
                            "grille_trim_roof_rack": grille_trim_roof_rack.to_json()
                        }
                    return response_gen(
                        200,
                        "Grille, Trim, Roof and Rack checklist inspection",
                        response,
                    )
            except Exception as exception:
                print(exception)
                return response_gen(
                    204, "No content for Grille, Trim, Roof and Rack inspection", {}
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(GrilleTrimRoofRack)
                .filter(GrilleTrimRoofRack.id == id)
                .first()
            )
            body = request.get_json()

            try:
                obj = GrilleTrimRoofRack(
                    grille_inspection=body["grille_inspection"],
                    trim_inspection=body["trim_inspection"],
                    roof_rack_inspection=body["roof_rack_inspection"],
                )

                data.grille_inspection = obj.grille_inspection
                data.trim_inspection = obj.trim_inspection
                data.roof_rack_inspection = obj.roof_rack_inspection
                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Grille, Trim, Roof and Rack inspection successfully updated",
                    data.to_json(),
                )
            except Exception as exception:
                print(exception)
                return response_gen(
                    400,
                    "Error while trying to update the group Grille, Trim, Roof and Rack",
                    {},
                )
