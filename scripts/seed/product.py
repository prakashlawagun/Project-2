import csv
import random
from pathlib import Path

from yaspin import yaspin

from menu.models import MenuItem, MealCategory

PRODUCT_CSV_PATH = Path(__file__).parent.parent.parent / 'products.csv'

CATEGORIES = [
    'Burgers',
    'Pizzas',
    'Drinks',
    'Desserts',
    'Sides',
    'Salads',
]


def create_categories():
    with yaspin(text='Create categories', color='cyan') as spinner:
        for category in CATEGORIES:
            MealCategory.objects.get_or_create(name=category)
        spinner.ok()


def get_random_category():
    categories = MealCategory.objects.values_list('id', flat=True)
    category_id = random.choice(categories)
    return MealCategory.objects.get(id=category_id)


def create_products():
    with yaspin(text='Create products', color='cyan') as spinner:
        if not MenuItem.objects.exists():
            with open(PRODUCT_CSV_PATH, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    category = get_random_category()
                    name = row['name']
                    price = row['price']
                    description = row['description']
                    calories = row['calories']
                    MenuItem.objects.create(
                        name=name,
                        price=price,
                        description=description,
                        calories=calories,
                        category=category,
                    )
            spinner.ok()
        else:
            spinner.fail()
