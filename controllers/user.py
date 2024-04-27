from starlette.requests import Request
from starlette.responses import JSONResponse
from models.user import Users
from dto.dto import ok
from dto.dto import badRequest
from transformers.UserTransformer import singleTransformUser
from transformers.UserTransformer import singleTransformUserLogin
from transformers.UserTransformer import singleTransformSignJWT
from database.config import SessionLocal
from utils.hash_password import get_password_hash
from utils.verify_password import verify_password
from middleware.auth_handler import signJWT
from middleware.auth_handler import get_current_user
from models.contact import Contacts
from transformers.UserTransformer import transformUserAndContact

db=SessionLocal()

class UserController:
    @staticmethod
    async def store(request: Request) -> JSONResponse:
        try:
            body = await request.json()
            name = body['name']
            city = body['city']
            state = body['state']
            postal = body['postal']
            password = body['password']
            
            if name == "":
                raise Exception("name couldn't be empty!")
            elif len(password) < 8:
                raise Exception("password must be at least 8 characters!")
            
            hashPassword = get_password_hash(password)
            
            usersData = db.query(Users).all()
            
            if len(usersData) == 0:
                user = Users(name=name, city=city, state=state, postal=postal, password=hashPassword)
                db.add(user)
                db.commit()
                transformer = singleTransformUser(user)
                return ok(transformer, "Success Create User!")
            
            customerId = len(usersData) + 1
            user = Users(customer_id=customerId, name=name, city=city, state=state, postal=postal, password=hashPassword)
            db.add(user)
            db.commit()
            transformer = singleTransformUser(user)
            return ok(transformer, "Success Create User!")
        except Exception as e:
            db.rollback()
            return badRequest('', f'{e}')
    
    @staticmethod
    async def update(id: int, request: Request) -> JSONResponse:
        try:
            auth_token = request.headers.get('Authorization')
            token = auth_token.split('Bearer')[1].strip()
            userId = get_current_user(token)
            
            body = await request.json()
            name = body['name']
            city = body['city']
            state = body['state']
            postal = body['postal']
            password = body['password']

            if name == "":
                raise Exception("name couldn't be empty!")
            elif len(password) < 8:
                raise Exception("password must be at least 8 characters!")


            userUpdate = db.query(Users).filter(Users.customer_id==id).first()
            if userUpdate is None:
                raise Exception('user not found!')

            hashPassword = get_password_hash(password)
            userUpdate.name = name
            userUpdate.city = city
            userUpdate.state = state
            userUpdate.postal = postal
            userUpdate.password = hashPassword

            transformer = singleTransformUser(userUpdate)
            if transformer["customer_id"] != userId:
                raise Exception('You are not Owner!')
            
            db.commit()
            return ok(transformer, "Success Update User!")
        except Exception as e:
            db.rollback()
            return badRequest('', f'{e}')
    
    @staticmethod
    async def login(request: Request) -> JSONResponse:
        try:
            body = await request.json()
            name = body['name']
            password = body['password']
            
            if name == "":
                raise Exception("name couldn't be empty!")
            elif len(password) < 8:
                raise Exception("password must be at least 8 characters!")
            
            user = db.query(Users).filter(Users.name == name).first()
            if user is None:
                raise Exception('user not found!')
                        
            transformerUserLoginUser = singleTransformUserLogin(user)
            
            verifyPasword = verify_password(password, transformerUserLoginUser['password'])
            if verifyPasword == False:
                raise Exception('Password not matched!')
            
            sign_jwt = signJWT(transformerUserLoginUser['customer_id'])
            transformSignJWT = singleTransformSignJWT(sign_jwt)
            
            strObj = transformSignJWT["access_token"]
            start = 0
            stop = 1
            # Remove charactes from index 5 to 10
            if len(strObj) > stop :
                strObj = strObj[0: start:] + strObj[stop + 1::]
            
            transformSignJWT["access_token"] = strObj[:-1]
            return ok(transformSignJWT, "Success Login!")
        except Exception as e:
            return badRequest('', f'{e}')
    
    @staticmethod
    async def profile(id: int, request: Request) -> JSONResponse:
        try:
            auth_token = request.headers.get('Authorization')
            token = auth_token.split('Bearer')[1].strip()
            userId = get_current_user(token)

            profile = db.query(Users, Contacts).join(Contacts).filter(Contacts.customer_id == id).all()
            
            if len(profile) == 0:
                raise Exception('Please input or create Contact data first!')

            if profile is None:
                raise Exception('Contact not Found!')
                        
            transformer = transformUserAndContact(profile)

            if transformer["customer_id"] != userId:
                raise Exception('You are not Owner!')
            
            return ok(transformer, "Success Get Contact!")
        except Exception as e:
            return badRequest('', f'{e}')