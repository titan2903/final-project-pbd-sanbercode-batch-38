def transform(items):
    array = []

    for item in items:
        array.append(singleTransformProduct(item))
    return array


def singleTransformProduct(values):
    return {
        "product_id": values.product_id,
        "product_name": values.product_name,
        "category": values.category,
        "sub_category": values.sub_category,
    }
