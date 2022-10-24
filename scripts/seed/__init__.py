from . import user, product


def run():
    user.create_superuser()
    user.create_default_user()
    product.create_categories()
    product.create_products()
