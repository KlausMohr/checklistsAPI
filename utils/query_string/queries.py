#ALL PEOPLE RELATED QUERIES
GET_ALL_OWNER = "SELECT * FROM checklist_app.tb_owner;"


GET_OWNER_BY_ID = "SELECT * FROM checklist_app.tb_owner WHERE id = %s"

INSERT_OWNER = """INSERT INT checklist_app.tb_owner(
    name, 
    birthday, 
    telephone, 
    email,
    address,
    cpf)
    VALUES(
        %s, %s, %s, %s, %s, %s);"""
        
#DELET_OWNER =

#UPDATE_OWNER =

#ALL VEHICLES RELATED QUERIES
GET_ALL_VEHICLES = "SELECT * FROM checklist_app.tb_vehicle"


GET_VEHICLE_BY_ID = "SELECT * FROM checklist_app.tb_vehicle WHERE id = %s"


INSERT_VEHICLE = """INSERT INTO checklist_app.tb_vehicle(
    make, 
    model, 
    year, 
    color, 
    vin, 
    mileage, 
    licenseplt)
    VALUES(
        %s, %s, %s, %s, %s, %s, %s);"""
        
#DELETE_VEHICLE =

#UPDATE_VEHICLE =


#ALL OWNERSHIP RELATED QUERIES


#ALL CHECKLIST RELATED QUERIES
GET_ALL_CHECKLISTS = "SELECT * FROM checklist_app.tb_checklist"

GET_CHECKLIST_BY_ID = "SELECT * FROM checklist_app.tb_checklist WHERE id = %s"

INSERT_CHECKLIST = """INSERT INTO checklist_app.tb_checklist(
    diagnostic,
    underhood,
    underbody,
    exterior,
    interior,
    hybrid,
    road)
    VALUES(
        %s, %s, %s, %s, %s, %s, %s);"""

#DELETE_CHECKLIST = 

#UPDATE_CHECKLIST = 