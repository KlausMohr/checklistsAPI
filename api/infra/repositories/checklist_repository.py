from flask import json
from api.entities.checklist_entity import Checklist
from api.entities.checklist_invoice import ChecklistInvoice
from api.entities.owner_entity import Owner
from api.entities.vehicle_entity import Vehicle
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from .irepository import Repository


class ChecklistRepository (Repository):
    def get_all():
        with DBConnection() as db:
            data = db.session.query().with_entities(ChecklistInvoice, Vehicle, Owner).select_from(
                ChecklistInvoice).join(Checklist).join(Vehicle).join(Owner).all()
            response = []
            for checklist, vehicle, owner in data:
                obj = {"checklist": checklist.to_json(),
                           "vehicle": vehicle.to_json(),
                           "owner": owner.to_json()}
                response.append(obj)
  
            return response_gen(200, "Checklists", response, "Lista de checklists realizados")

    def get_by_id(id):
        with DBConnection() as db:
            data = db.session.query(ChecklistInvoice, Vehicle, Owner).select_from(ChecklistInvoice).join(
                Vehicle).join(Owner).filter(ChecklistInvoice.id == id)
            for checklist, vehicle, owner in data:
                response = {"checklist": checklist.to_json(),
                            "vehicle": vehicle.to_json(),
                            "owner": owner.to_json()}

            # response = [checklist.to_json() for checklist in data]

            return response_gen(200, "Checklist", response)

    def insert():
        pass

    def delete(id):
        return super().delete()

    def update(id):
        return super().update()
