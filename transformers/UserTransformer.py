def transform(items):
    array = []

    for item in items:
        array.append(singleTransformUser(item))
    return array


def singleTransformUser(values):
    return {
        "customer_id": values.customer_id,
        "name": values.name,
        "city": values.city,
        "state": values.state,
        "postal": values.postal
    }
    
def singleTransformUserLogin(values):
    return {
        "customer_id": values.customer_id,
        "password": values.password
    }

def singleTransformSignJWT(values):
    return {
        "access_token": f'{values["access_token"]}'
    }

def transformUserAndContact(values):    
    if len(values) > 0:
        for row in values:
            return {
                "customer_id": row.Users.customer_id,
                "name": row.Users.name,
                "city": row.Users.city,
                "state": row.Users.state,
                "postal": row.Users.postal,
                "contact_name": row.Contacts.contact_name,
                "phone": row.Contacts.phone,
                "email": row.Contacts.email
            }