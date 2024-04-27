from flask import request
from api.entities.checklist.exterior.glass_outside_mirrors import GlassOutsideMirrors
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class GlassOutsideMirrorsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query(GlassOutsideMirrors).filter(
                GlassOutsideMirrors.id == id
            )

            try:
                if data:
                    for glass_outside_mirrors in data:
                        response = {
                            "glass_outside_mirrors": glass_outside_mirrors.to_json()
                        }
                    return response_gen(200, "Glass and Ouside Mirrors", response)
            except Exception as exception:
                print(exception)
                return response_gen(204, "No content for Glass and Outside Mirrors", {})

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            body = request.get_json()
            data = (
                db.session.query(GlassOutsideMirrors)
                .filter(GlassOutsideMirrors.id == id)
                .first()
            )
            try:
                obj = GlassOutsideMirrors(
                    windshield=body["windshield"],
                    side_glass=body["side_glass"],
                    rear_window_tail_gate=body["rear_window_tail_gate"],
                    wiper_blade_replacement=body["wiper_blade_replacement"],
                    outside_mirror=body["outside_mirror"],
                    outside_mirror_folding=body["outside_mirror_folding"],
                )
                data.windshield = obj.windshield
                data.side_glass = obj.side_glass
                data.rear_window_tail_gate = obj.rear_window_tail_gate
                data.wiper_blade_replacement = obj.wiper_blade_replacement
                data.outside_mirror = obj.outside_mirror
                data.outside_mirror_folding = obj.outside_mirror_folding

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Glass and Outside Mirrors inspection successfully updated",
                    data.to_json(),
                )
            except Exception as exception:
                print(exception)
                return response_gen(
                    400,
                    "Error while trying to update the group Glass and Outside Mirrors",
                    {},
                )
