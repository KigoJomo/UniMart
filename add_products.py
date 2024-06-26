import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Unimart.settings")
django.setup()

from shop.models import Category, Product

# Define product lists for each category
electronics_products = [
    "Smartphone",
    "Laptop",
    "Smartwatch",
    "Headphones",
    "Tablet",
    "Camera",
    "TV",
    "Printer",
    "Gaming Console",
    "Router",
    "External Hard Drive",
    "Wireless Earbuds",
    "Microphone",
    "Portable Speaker",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Graphics Card",
    "Power Bank",
    "Charging Cable",
    "Camera Lens",
    "Drone",
    "Fitness Tracker",
    "LED Light Strip",
    "Home Assistant",
    "Action Camera",
    "Projector",
    "VR Headset",
    "Wireless Charger"
]

clothing_products = [
    "T-Shirt",
    "Jeans",
    "Dress",
    "Sweater",
    "Jacket",
    "Shoes",
    "Skirt",
    "Socks",
    "Hat",
    "Shorts",
    "Coat",
    "Scarf",
    "Gloves",
    "Blouse",
    "Boots",
    "Sandals",
    "Pants",
    "Belt",
    "Cardigan",
    "Polo Shirt",
    "Tie",
    "Leggings",
    "Hoodie",
    "Suit",
    "Underwear",
    "Pajamas",
    "Swimsuit",
    "Raincoat",
    "Vest"
]

home_and_kitchen_products = [
    "Coffee Maker",
    "Blender",
    "Toaster",
    "Microwave",
    "Food Processor",
    "Electric Kettle",
    "Air Fryer",
    "Slow Cooker",
    "Stand Mixer",
    "Rice Cooker",
    "Juicer",
    "Pressure Cooker",
    "Waffle Maker",
    "Hand Blender",
    "Grill",
    "Espresso Machine",
    "Water Filter",
    "Dishwasher",
    "Food Scale",
    "Can Opener",
    "Kitchen Utensil Set",
    "Cutlery Set",
    "Knife Block",
    "Mixing Bowls",
    "Bakeware Set",
    "Cookware Set",
    "Dining Set",
    "Kitchen Towels",
    "Apron",
    "Placemats"
]

books_products = [
    "Fiction Book",
    "Non-Fiction Book",
    "Textbook",
    "Children's Book",
    "Cookbook",
    "Biography",
    "Self-Help Book",
    "Mystery Book",
    "Romance Novel",
    "Science Fiction Book",
    "Fantasy Book",
    "Thriller Book",
    "Poetry Book",
    "History Book",
    "Art Book",
    "Travel Book",
    "Health Book",
    "Business Book",
    "Graphic Novel",
    "Comic Book",
    "Horror Book",
    "Classic Literature",
    "Religious Book",
    "Philosophy Book",
    "Political Book",
    "Humor Book",
    "Young Adult Book",
    "Memoir",
    "Essay Collection",
    "Drama Book"
]

health_and_beauty_products = [
    "Shampoo",
    "Conditioner",
    "Body Wash",
    "Face Wash",
    "Moisturizer",
    "Sunscreen",
    "Deodorant",
    "Perfume",
    "Cologne",
    "Hair Gel",
    "Hair Spray",
    "Hair Mask",
    "Hair Oil",
    "Hair Serum",
    "Lip Balm",
    "Hand Cream",
    "Body Lotion",
    "Face Mask",
    "Facial Cleanser",
    "Eye Cream",
    "Serum",
    "Body Scrub",
    "Essential Oil",
    "Toner",
    "Makeup Remover",
    "Foundation",
    "Concealer",
    "Mascara",
    "Eyeliner",
    "Lipstick"
]

toys_and_games_products = [
    "Board Game",
    "Puzzle",
    "LEGO Set",
    "Action Figure",
    "Doll",
    "Toy Car",
    "Remote Control Car",
    "Train Set",
    "Model Kit",
    "Building Blocks",
    "Dollhouse",
    "Stuffed Animal",
    "Teddy Bear",
    "Play-Doh Set",
    "Art Kit",
    "Craft Kit",
    "Science Kit",
    "Educational Toy",
    "Musical Instrument",
    "Outdoor Game",
    "Kite",
    "Bicycle",
    "Scooter",
    "Skateboard",
    "Trampoline",
    "Jump Rope",
    "Yo-Yo",
    "Frisbee",
    "Basketball",
    "Soccer Ball"
]

sports_and_outdoors_products = [
    "Tent",
    "Sleeping Bag",
    "Backpack",
    "Hiking Boots",
    "Water Bottle",
    "Camping Stove",
    "Headlamp",
    "Flashlight",
    "Binoculars",
    "Pocket Knife",
    "Fishing Rod",
    "Cycling Helmet",
    "Running Shoes",
    "Yoga Mat",
    "Exercise Ball",
    "Resistance Bands",
    "Gym Bag",
    "Jump Rope",
    "Fitness Tracker",
    "Swim Goggles",
    "Dumbbell Set",
    "Tennis Racket",
    "Golf Club Set",
    "Basketball Hoop",
    "Soccer Goal",
    "Football",
    "Baseball Bat",
    "Volleyball",
    "Surfboard",
    "Skateboard"
]

automotive_products = [
    "Car Wax",
    "Car Wash Soap",
    "Car Shampoo",
    "Microfiber Towels",
    "Wheel Brush",
    "Tire Shine",
    "Car Polish",
    "Car Wax Applicator",
    "Car Detailing Kit",
    "Car Vacuum",
    "Car Air Freshener",
    "Car Seat Covers",
    "Steering Wheel Cover",
    "Car Floor Mats",
    "Car Sunshade",
    "Car Organizer",
    "Car Charger",
    "Car Phone Mount",
    "Car Jump Starter",
    "Car Battery Charger",
    "Car Emergency Kit",
    "Car Jack",
    "Jumper Cables",
    "Tire Pressure Gauge",
    "Engine Oil",
    "Car Coolant",
    "Windshield Wipers",
    "Antifreeze",
    "Fuel Additive",
    "Brake Fluid"
]

grocery_products = [
    "Bread",
    "Milk",
    "Eggs",
    "Butter",
    "Cheese",
    "Yogurt",
    "Fresh Fruit",
    "Fresh Vegetables",
    "Cereal",
    "Pasta",
    "Rice",
    "Canned Soup",
    "Canned Vegetables",
    "Canned Beans",
    "Frozen Pizza",
    "Frozen Vegetables",
    "Frozen Meals",
    "Ice Cream",
    "Snack Bars",
    "Chips",
    "Soda",
    "Juice",
    "Coffee",
    "Tea",
    "Water",
    "Cookies",
    "Chocolate",
    "Candy",
    "Condiments",
    "Spices"
]

office_supplies_products = [
    "Notebook",
    "Pen",
    "Pencil",
    "Highlighter",
    "Stapler",
    "Staples",
    "Scissors",
    "Tape",
    "Glue Stick",
    "Whiteboard",
    "Dry Erase Markers",
    "Desk Organizer",
    "Paper Clips",
    "Binder Clips",
    "Push Pins",
    "Rubber Bands",
    "Calculator",
    "Ruler",
    "Folders",
    "Binders",
    "Printer Paper",
    "Ink Cartridges",
    "USB Flash Drive",
    "External Hard Drive",
    "Desk Lamp",
    "Mouse Pad",
    "Monitor Stand",
    "Headphones",
    "Laptop Stand",
    "Desk Calendar"
]

# Define a function to add products to the database


def add_products():
    categories = Category.objects.all()

    for category in categories:
        products_list = globals(
        )[f"{category.name.lower().replace(' ', '_')}_products"]
        print(category.name)
        for product_name in products_list:
            Product.objects.create(
                name=product_name,
                category=category,
                # Random price between 10 and 1000
                price=random.randint(10, 1000)
            )
            print(product_name)
        print("")


if __name__ == "__main__":
    add_products()
