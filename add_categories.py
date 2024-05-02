import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Unimart.settings")
django.setup()

from shop.models import Category

product_categories = [
    "Electronics",
    "Clothing",
    "Home and Kitchen",
    "Books",
    "Health and Beauty",
    "Toys and Games",
    "Sports and Outdoors",
    "Automotive",
    "Grocery",
    "Office Supplies"
]

def add_categories():
    for category in product_categories:
        Category.objects.create(
            name = category
        )
        print(category)

if __name__ == "__main__":
    add_categories()
