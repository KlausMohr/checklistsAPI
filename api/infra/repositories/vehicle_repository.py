from flask import request
from api.entities.vehicle_entity import Vehicle
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from .irepository import Repository


class VehicleRepository(Repository):
    def get_all():
        with DBConnection() as db:
            data = db.session.query(Vehicle).all()
            response = [vehicle.to_json() for vehicle in data]
            return response_gen(
                200, "Veículo", response, "Lista de veículos cadastrados"
            )

    def get_by_id(id):
        with DBConnection() as db:
            data = db.session.query(Vehicle).filter(Vehicle.id == id)
            response = [vehicle.to_json() for vehicle in data]
            return response_gen(200, "Veículo", response)

    def update(id):
        with DBConnection() as db:
            vehicle_obj = db.session.query(Vehicle).filter(Vehicle.id == id).first()
            body = request.get_json()

            try:
                if "make" in body:
                    vehicle_obj.make = body["make"]
                if "model" in body:
                    vehicle_obj.model = body["model"]
                if "year" in body:
                    vehicle_obj.year = body["year"]
                if "color" in body:
                    vehicle_obj.color = body["color"]
                if "vin" in body:
                    vehicle_obj.vin = body["vin"]
                if "mileage" in body:
                    vehicle_obj.mileage = body["mileage"]
                if "licenseplt" in body:
                    vehicle_obj.licenseplt = body["licenseplt"]

                db.session.add(vehicle_obj)
                db.session.commit()
                return response_gen(
                    200, "Veículo", vehicle_obj.to_json(), "Veículo atualizado com sucesso"
                )
            except ImportError as e:
                print("Erro", e)
                return response_gen(
                    400, "Veículo", {}, "Erro ao atualizar dados do veículo"
                )

    def delete(id):
        with DBConnection() as db:
            try:
                data = db.session.query(Vehicle).filter(Vehicle.id == id).delete()
                db.session.commit()
                return response_gen(
                    200, f"Veículo: {Vehicle.id}", data, "Removido com sucesso"
                )
            except ImportError as e:
                print("Error: ", e)
                return response_gen(400, "Veículo", {}, "Falha ao remover veículo")

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                vehicle = Vehicle(
                    make=body["make"],
                    model=body["model"],
                    year=body["year"],
                    color=body["color"],
                    vin=body["vin"],
                    mileage=body["mileage"],
                    licenseplt=body["licenseplt"],
                )
                db.session.add(vehicle)
                db.session.commit()
                return response_gen(
                    200,
                    "Veículo",
                    vehicle.to_json(),
                    "Novo veículo cadastrado com sucesso",
                )
            except ImportError as e:
                print()
