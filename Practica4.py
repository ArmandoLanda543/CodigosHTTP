from fastapi import FastAPI, HTTPException, status
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

def my_schema():
   openapi_schema = get_openapi(
       title="Practica 4",
       version="1.0",
       description="HTTP Methods",
       routes=app.routes,
   )
   app.openapi_schema = openapi_schema
   return app.openapi_schema

app=FastAPI()

class User(BaseModel): ##ENTIDAD
    PassengerId:int
    Survived:int
    Pclass:int
    Name:str   
    Sex:str
    Age:int

users_list=[User(PassengerId=1, Survived=0, Pclass=3, Name='Braund, Mr. Owen Harris', Sex='male', Age=22),
            User(PassengerId=2, Survived=1, Pclass=1, Name='Cumings, Mrs. John Bradley (Florence Briggs Thayer)', Sex='female',Age=38),
            User(PassengerId=3, Survived=1, Pclass=3, Name= 'Heikkinen, Miss. Laina', Sex='female', Age=26),
            User(PassengerId=4, Survived=1, Pclass=1, Name='Futrelle, Mrs. Jacques Heath (Lily May Peel)', Sex='female', Age=35),
            User(PassengerId=5, Survived=0, Pclass=3, Name='Allen, Mr. William Henry', Sex='male', Age=35),
            User(PassengerId=6, Survived=0, Pclass=3, Name='Moran, Mr. James', Sex='male', Age=0),
            User(PassengerId=7, Survived=0, Pclass=1, Name='McCarthy, Mr. Timothy J', Sex='male', Age=54),
            User(PassengerId=8, Survived=0, Pclass=3, Name='Palsson, Master. Gosta Leonard', Sex='male', Age=2),
            User(PassengerId=9, Survived=1, Pclass=3, Name='Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)', Sex='female', Age=27),
            User(PassengerId=10, Survived=1, Pclass=2, Name='Nasser, Mrs. Nicholas (Adele Achem)', Sex='female', Age=14),
            User(PassengerId=11, Survived=1, Pclass=3, Name='Sandstrom, Miss. Marguerite Rut', Sex='female', Age=4),
            User(PassengerId=12, Survived=1, Pclass=1, Name='Bonnell, Miss. Elizabeth', Sex='female', Age=58),
            User(PassengerId=13, Survived=0, Pclass=3, Name='Saundercock, Mr. William Henry', Sex='male', Age=20),
            User(PassengerId=14, Survived=0, Pclass=3, Name='Andersson, Mr. Anders Johan', Sex='male', Age=39),
            User(PassengerId=15, Survived=0, Pclass=3, Name='Vestrom, Miss. Hulda Amanda Adolfina', Sex='female', Age=14),
            User(PassengerId=16, Survived=1, Pclass=2, Name='Hewlett, Mrs. (Mary D Kingcome)', Sex='male', Age=22),
            User(PassengerId=17, Survived=0, Pclass=3, Name='Rice, Master. Eugene', Sex='male', Age=2),
            User(PassengerId=18, Survived=1, Pclass=2, Name='Williams, Mr. Charles Eugene', Sex='male', Age=0),
            User(PassengerId=19, Survived=0, Pclass=3, Name='Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)', Sex='female', Age=31),
            User(PassengerId=20, Survived=1, Pclass=3, Name='Masselmani, Mrs. Fatima', Sex='female', Age=0),
            User(PassengerId=21, Survived=0, Pclass=2, Name='Fynney, Mr. Joseph J', Sex='male', Age=35),
            User(PassengerId=22, Survived=1, Pclass=2, Name='Beesley, Mr. Lawrence', Sex='male', Age=34),
            User(PassengerId=23, Survived=1, Pclass=3, Name='McGowan, Miss. Anna ""Annie""', Sex='female', Age=15),
            User(PassengerId=24, Survived=1, Pclass=1, Name='Sloper, Mr. William Thompson', Sex='male', Age=28),
            User(PassengerId=25, Survived=0, Pclass=3, Name='Palsson, Miss. Torborg Danira', Sex='female', Age=8)]

####################################################    GET     ######################################################
@app.get("/UsuariosPractica4/{user_id}", status_code=status.HTTP_202_ACCEPTED) #PATH
async def get_user(user_id:int):
    for user in users_list:
        if user.PassengerId==user_id:
            return user
    raise HTTPException(status_code = 204, detail= "Usuario no encontrado")


@app.get("/UsuariosPractica4", status_code=status.HTTP_200_OK) #QUERY
async def get_users():
    return users_list

####################################################    POST    ######################################################

@app.post("/UsuariosPractica4", status_code=status.HTTP_201_CREATED) #QUERY
async def userclass(user:User):
    found=False

    for index, save_user in enumerate(users_list):
        if save_user.PassengerId == user.PassengerId:
            raise HTTPException(status_code = 424, detail= "El usuario ya existe" )
    else:
        users_list.append(user)
        return {"message": "Usuario creado exitosamente"}
        return user

###########################put############################################
@app.put("/UsuariosPractica4/", status_code=status.HTTP_426_UPGRADE_REQUIRED)
async def userclass(user:User):

    found=False #Usamos bandera found para verificar si hemos encontrado el usuario o no

    for index, save_user in enumerate(users_list):      ##TOMA LA POSICION DE DONDE ESTA EL USUARIO
        if save_user.PassengerId == user.PassengerId:     #Si el Id del usuario guardado es igual al Id del usuario nuevo
            users_list[index]=user      #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
            found=True
    if not found:
        raise HTTPException(status_code = 404, detail= "El usuario no existe" )
    else:
        return user
        return {"message": "Usuario actualizado exitosamente"}

###########################DELETE############################################
@app.delete("/UsuariosPractica4/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerId ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code = 410, detail= "El registro se ha eliminado" )
           return "El registro se ha eliminado"
       
    if not found:
        raise HTTPException(status_code = 404, detail= "El registro no se ha encontrado" )


