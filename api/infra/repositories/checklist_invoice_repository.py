from flask import request
from api.entities.checklist_entity import Checklist
from api.entities.checklist_invoice import ChecklistInvoice
from api.entities.owner_entity import Owner
from api.entities.vehicle_entity import Vehicle
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from .irepository import Repository


class ChecklistInvoiceRepository(Repository):
    def get_all():
        with DBConnection() as db:
            data = (
                db.session.query()
                .with_entities(ChecklistInvoice, Vehicle, Owner)
                .select_from(ChecklistInvoice)
                .join(Checklist)
                .join(Vehicle)
                .join(Owner)
                .all()
            )
            try:
                response = []
                for checklist, vehicle, owner in data:
                    obj = {
                        "checklist": checklist.to_json(),
                        "vehicle": {
                            "model": vehicle.model,
                            "licenseplt": vehicle.licenseplt,
                        },
                        "owner": owner.name,
                    }
                    response.append(obj)

                return response_gen(
                    200, "Checklist Invoice", response, "Lista de checklists realizados"
                )
            except:
                response = {}
                return response_gen(
                    204, "No content found for Checklists Invoice", response
                )

    def get_by_id(id):
        with DBConnection() as db:
            data = (
                db.session.query(ChecklistInvoice, Vehicle, Owner)
                .select_from(ChecklistInvoice)
                .join(Vehicle)
                .join(Owner)
                .filter(ChecklistInvoice.id == id)
            )

            try:
                for checklist, vehicle, owner in data:
                    response = {
                        "checklist": checklist.to_json(),
                        "vehicle": vehicle.to_json(),
                        "owner": owner.to_json(),
                    }
                return response_gen(200, "Checklist", response)
            except:
                response = {}
                return response_gen(
                    204, "No content found for Checklists Invoice", response
                )

    def insert():
        pass

    def delete(id):
        with DBConnection() as db:
            try:
                db.session.query(ChecklistInvoice).filter(
                    ChecklistInvoice.id == id
                ).delete()
                db.session.commit()
                return response_gen(200, "Invoice successfully deleted")
            except:
                db.session.rollback()
                return response_gen(400, "Delete process not possible")

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(ChecklistInvoice)
                .filter(ChecklistInvoice.id == id)
                .first()
            )
            body = request.get_json()
            try:
                if "vehicle_id" in body:
                    data.vehicle_id = body["vehicle_id"]
                if "owner_id" in body:
                    data.owner_id = body["owner_id"]

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200, "Checklist Invoice successfully updated", data.to_json()
                )
            except Exception as exception:
                print(exception)
                return response_gen(400, "Error while updating checklist invoice", {})
