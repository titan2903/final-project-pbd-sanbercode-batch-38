from starlette.responses import JSONResponse
from starlette.requests import Request
from dto.dto import ok
from dto.dto import badRequest
from models.contact import Contacts
from database.config import SessionLocal
from entity.ContactTransformer import singleTransformContact
from utils.validate_email import validateEmail
from middleware.auth_handler import get_current_user

db=SessionLocal()

class ContactController:
    @staticmethod
    async def store(request: Request) -> JSONResponse:
        try:
            auth_token = request.headers.get('Authorization')
            token = auth_token.split('Bearer')[1].strip()
            userId = get_current_user(token)
            
            body = await request.json()
            contact_name = body['contact_name']
            phone = body['phone']
            email = body['email']
            
            if contact_name == "":
                raise Exception("contact name couldn't be empty!")
            elif email == "":
                raise Exception("email can't be empty!")
            elif phone == "":
                raise Exception("phone can't be empty!")
            
            isEmailValid = validateEmail(email)
            
            if isEmailValid == False:
                raise Exception("Invalid Email!")
            
            contact = Contacts(customer_id=userId, contact_name=contact_name, phone=phone, email=email.lower())
            db.add(contact)
            db.commit()
            transformer = singleTransformContact(contact)
            return ok(transformer, "Success Create Contact!")
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
            contact_name = body['contact_name']
            phone = body['phone']
            email = body['email']

            if contact_name == "":
                raise Exception("contact name couldn't be empty!")
            elif email == "":
                raise Exception("email can't be empty!")
            elif phone == "":
                raise Exception("phone can't be empty!")


            isEmailValid = validateEmail(email)
            
            if isEmailValid == False:
                raise Exception("Invalid Email!")
            
            contactUpdate = db.query(Contacts).filter(Contacts.contact_id==id).first()
            if contactUpdate is None:
                raise Exception('contact not found!')

            contactUpdate.contact_name = contact_name
            contactUpdate.phone = phone
            contactUpdate.email = email.lower()
        

            transformer = singleTransformContact(contactUpdate)
            if transformer["customer_id"] != userId:
                raise Exception('You are not Owner!')
            
            db.commit()
            return ok(transformer, "Success Update Contact!")
        except Exception as e:
            db.rollback()
            return badRequest('', f'{e}')

    @staticmethod
    async def getById(id:int, request: Request) -> JSONResponse:
        try:
            auth_token = request.headers.get('Authorization')
            token = auth_token.split('Bearer')[1].strip()
            userId = get_current_user(token)

            contact = db.query(Contacts).filter(Contacts.contact_id==id).first()
            

            if contact is None:
                raise Exception('Contact not Found!')

            transformer = singleTransformContact(contact)

            if transformer["customer_id"] != userId:
                raise Exception('You are not Owner!')
            
            return ok(transformer, "Success Get Contact!")
        except Exception as e:
            return badRequest('', f'{e}')