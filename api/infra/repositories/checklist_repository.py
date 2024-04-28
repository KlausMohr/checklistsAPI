from flask import request
from api.entities.checklist.diagnosis_entity import Diagnosis
from api.entities.checklist.exterior_entity import Exterior
from api.entities.checklist.hybrid_entity import Hybrid
from api.entities.checklist.interior_entity import Interior
from api.entities.checklist.roadtest_enitity import RoadTest
from api.entities.checklist.underbody_entity import Underbody
from api.entities.checklist.underhood_entity import Underhood
from api.entities.checklist_entity import Checklist
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from .irepository import Repository


class ChecklistRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            try:
                data = (
                    db.session.query()
                    .with_entities(
                        Checklist,
                        Diagnosis,
                        Exterior,
                        Hybrid,
                        Interior,
                        RoadTest,
                        Underbody,
                        Underhood,
                    )
                    .select_from(Checklist)
                    .join(Diagnosis)
                    .join(Exterior)
                    .join(Hybrid)
                    .join(Interior)
                    .join(RoadTest)
                    .join(Underbody)
                    .join(Underhood)
                    .where(Checklist.id == id)
                )

                for (
                    checklist,
                    diagnosis,
                    exterior,
                    hybrid,
                    interior,
                    roadtest,
                    underbody,
                    underhood,
                ) in data:
                    response = {
                        "checklist": checklist.to_json(),
                        "items": {
                            "diagnosis": diagnosis.to_json(),
                            "exterior": exterior.to_json(),
                            "hybrid": hybrid.to_json(),
                            "interior": interior.to_json(),
                            "roadtest": roadtest.to_json(),
                            "underbody": underbody.to_json(),
                            "underhood": underhood.to_json(),
                        },
                    }
                return response_gen(200, "Checklist", response)

            except Exception as exception:
                print(exception)
                return response_gen(204, "No content for Checklist", {})

    def insert():
        with DBConnection() as db:
            try:
                body = request.get_json()

                if body:
                    checklist = Checklist(
                        diagnostic_id=body["diagnostic_id"],
                        underhood_id=body["underhood_id"],
                        underbody=body["underbody"],
                        exterior_id=body["exterior_id"],
                        interior_id=body["interior_id"],
                        hybrid_id=body["hybrid_id"],
                        roadtest_id=body["roadtest_id"],
                    )
                db.session.add(checklist)
                db.session.commit()
                return response_gen(
                    200, "Checklist inserted successfully", checklist.to_json()
                )
            except Exception as exception:
                db.session.rollback()
                print(exception)
                return response_gen(400, "Error while inserting new checklist", {})

    def delete(id):
        with DBConnection() as db:
            try:
                data = db.session.query(Checklist).filter(Checklist.id == id).delete()
                db.session.commit()
                return response_gen(
                    200, f"Checklist: {Checklist.id}", data, "Removido com sucesso"
                )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(400, "Checklist", {}, "Falha ao remover checklist")

    def update(id):
        raise NotImplementedError
