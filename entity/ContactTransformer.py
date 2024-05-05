def transform(items):
    array = []

    for item in items:
        array.append(singleTransformContact(item))
    return array


def singleTransformContact(values):
    return {
        "contact_id": values.contact_id,
        "customer_id": values.customer_id,
        "contact_name": values.contact_name,
        "phone": values.phone,
        "email": values.email,
    }
