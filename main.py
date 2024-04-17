from flask import Flask
from infra.repositories.owner_repository import OwnerRepository
from infra.repositories.vehicle_repository import VehicleRepository

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


"""Rotas para Proprietários"""


@app.get("/owners")
def get_all_owner():
    return OwnerRepository.get_all()


@app.get("/owners/<int:id>")
def get_owner_byid(id):
    return OwnerRepository.get_by_id(id)


@app.post("/owners/insert")
def insert_new_owner():
    return OwnerRepository.insert()


@app.put("/owners/<int:id>")
def update_owner(id):
    return OwnerRepository.update(id)


@app.delete("/owners/<int:id>")
def delete_owner(id):
    return OwnerRepository.delete(id)


"""Rotas para veículos"""


@app.get("/vehicles")
def get_all_vehicle():
    return VehicleRepository.get_all()


@app.get("/vehicles/<int:id>")
def get_vehicle_byid(id):
    return VehicleRepository.get_by_id(id)


@app.post("/vehicles/insert")
def insert_vehicle():
    return VehicleRepository.insert()


@app.put("/vehicles/<int:id>")
def update_vehicle(id):
    return VehicleRepository.update(id)


@app.delete("/vehicles/<int:id>")
def delete_vehicle(id):
    return VehicleRepository.delete(id)


app.run(port=18080)
