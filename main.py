from api.infra.repositories.address_repository import AddressRepository
from api.infra.repositories.checklist_invoice_repository import (
    ChecklistInvoiceRepository,
)
from api.infra.repositories.checklist_repository import ChecklistRepository
from api.infra.repositories.exterior.body_panels_repository import BodyPanelsRepository
from api.infra.repositories.exterior.doors_hood_tailgate_repository import (
    DoorsHoodTailgateRepository,
)
from api.infra.repositories.exterior.exterior_lights import ExteriorLightsRepository
from api.infra.repositories.exterior.exterior_repository import ExteriorRepository
from api.infra.repositories.exterior.glass_outside_mirrors_repository import (
    GlassOutsideMirrorsRepository,
)
from api.infra.repositories.exterior.grille_trim_roof_rack_repository import (
    GrilleTrimRoofRackRepository,
)
from api.infra.repositories.owner_repository import OwnerRepository
from api.infra.repositories.vehicle_repository import VehicleRepository
from api import create_app


app = create_app()

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


#################################################

"""Rotas para endereço"""
@app.get("/owners/address")
def get_all():
    return AddressRepository.get_all()

@app.get("/owners/address/<int:id>")
def get_by_id(id):
    return AddressRepository.get_by_id(id)

@app.post("/owners/address/insert")
def insert_new_address():
    return AddressRepository.insert()

@app.put("/owners/address/<int:id>")
def update_address(id):
    return AddressRepository.update(id)

################################################

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



##############################################

"""Checklist routes"""


@app.get("/checklists/invoice")
def get_checklists_invoice():
    return ChecklistInvoiceRepository.get_all()


@app.get("/checklist/invoice/<int:id>")
def get_checklist_invoice_by_id(id):
    return ChecklistInvoiceRepository.get_by_id(id)


@app.get("/checklist/<int:id>")
def get_checklists(id):
    return ChecklistRepository.get_by_id(id)


"""Exterior checklist routes"""


@app.get("/checklist/exterior/<int:id>")
def get_checklist_exterior(id):
    return ExteriorRepository.get_by_id(id)


@app.get("/checklist/exterior/bodypanel/<int:id>")
def get_checklist_bodyPBumper(id):
    return BodyPanelsRepository.get_by_id(id)


@app.put("/checklist/exterior/bodypanel/<int:id>")
def update_checklist_bodyPBumper(id):
    return BodyPanelsRepository.update(id)


@app.get("/checklist/exterior/doorshoodtailgate/<int:id>")
def get_checklist_doorsHTailgate(id):
    return DoorsHoodTailgateRepository.get_by_id(id)


@app.put("/checklist/exterior/doorshoodtailgate/<int:id>")
def update_checklist_doorsHTailgate(id):
    return DoorsHoodTailgateRepository.update(id)


@app.get("/checklist/exterior/exterior-lights/<int:id>")
def get_checklist_exterior_lights(id):
    return ExteriorLightsRepository.get_by_id(id)


@app.put("/checklist/exterior/exterior-lights/<int:id>")
def update_checklist_exterior_lights(id):
    return ExteriorLightsRepository.update(id)


@app.get("/checklist/exterior/glass-outmirrors/<int:id>")
def get_checklist_glass_ouside_mirrors(id):
    return GlassOutsideMirrorsRepository.get_by_id(id)


@app.put("/checklist/exterior/glass-outmirrors/<int:id>")
def update_checklist_glass_ouside_mirrors(id):
    return GlassOutsideMirrorsRepository.update(id)


@app.get("/checklist/exterior/grille-trim-roof-rack/<int:id>")
def get_checklist_grille_trim_roof_rack(id):
    return GrilleTrimRoofRackRepository.get_by_id(id)


@app.put("/checklist/exterior/grille-trim-roof-rack/<int:id>")
def update_checklist_grille_trim_roof_rack(id):
    return GrilleTrimRoofRackRepository.update(id)


app.run(port=18080)
