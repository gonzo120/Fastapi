from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, userEntity
from models.user import User

user = APIRouter()

@user.get('/users')
def find_all_user(): 
    return userEntity(conn.local.user.find())

@user.post('/users')
def create_user(user: User): 
    new_user = dict(user)
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)

@user.get('/users/{id}')
def find_user(): 
    return ' Hello world'

@user.put('/users/{id}')
def update_user(): 
    return ' Hello world'

@user.delete('/users/{id}')
def delete_user(): 
    return ' Hello world'