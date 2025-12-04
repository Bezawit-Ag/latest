from django.core.management.base import BaseCommand
from restaurant.models import Menu


class Command(BaseCommand):
    help = 'Populates the database with traditional Ethiopian dishes'

    def handle(self, *args, **options):
        ethiopian_dishes = [
            {
                'name': 'Doro Wat',
                'Price': 350,
                'description': 'Ethiopia\'s national dish—spicy chicken stew slow-simmered with berbere, onions, garlic, and hard-boiled eggs. Served with fresh injera.'
            },
            {
                'name': 'Kitfo',
                'Price': 420,
                'description': 'Premium minced raw beef seasoned with mitmita (chili powder) and niter kibbeh (clarified butter). Served with ayib (cheese) and gomen (collard greens).'
            },
            {
                'name': 'Tibs',
                'Price': 380,
                'description': 'Sautéed beef or lamb cubes with onions, peppers, rosemary, and berbere. Available mild or spicy. Served with injera or bread.'
            },
            {
                'name': 'Shiro Wat',
                'Price': 180,
                'description': 'Creamy chickpea flour stew spiced with berbere, garlic, and ginger. A beloved vegetarian dish served with injera.'
            },
            {
                'name': 'Misir Wat',
                'Price': 160,
                'description': 'Red lentil stew cooked with berbere, onions, and garlic. A staple vegetarian option rich in flavor and protein.'
            },
            {
                'name': 'Gomen',
                'Price': 140,
                'description': 'Tender collard greens sautéed with garlic, ginger, and turmeric. A healthy, flavorful side dish.'
            },
            {
                'name': 'Fasolia',
                'Price': 150,
                'description': 'Green beans and carrots cooked in a light tomato sauce with onions and spices. A fresh, colorful vegetarian option.'
            },
            {
                'name': 'Atkilt Wat',
                'Price': 145,
                'description': 'Cabbage, carrots, and potatoes braised with turmeric and spices. A comforting, mild vegetable dish.'
            },
            {
                'name': 'Doro Tibs',
                'Price': 360,
                'description': 'Chicken pieces sautéed with onions, peppers, and berbere. Crispy on the outside, tender inside.'
            },
            {
                'name': 'Beyaynetu',
                'Price': 280,
                'description': 'A colorful platter of vegetarian dishes including shiro, misir wat, gomen, fasolia, and atkilt. Perfect for sharing.'
            },
            {
                'name': 'Dulet',
                'Price': 320,
                'description': 'Spiced mixture of minced tripe, liver, and lean meat sautéed with onions, peppers, and mitmita. A bold, flavorful dish.'
            },
            {
                'name': 'Firfir',
                'Price': 200,
                'description': 'Shredded injera sautéed with spicy berbere sauce, onions, and peppers. A traditional breakfast or comfort food.'
            },
            {
                'name': 'Tere Siga',
                'Price': 450,
                'description': 'Raw beef cubes served with mitmita and awaze (spicy dipping sauce). For the adventurous eater.'
            },
            {
                'name': 'Yebeg Wat',
                'Price': 400,
                'description': 'Tender lamb stew slow-cooked with berbere, onions, and spices. Rich, aromatic, and deeply satisfying.'
            },
            {
                'name': 'Kik Alicha',
                'Price': 155,
                'description': 'Mild yellow split pea stew cooked with turmeric, onions, and garlic. A gentle, comforting vegetarian option.'
            }
        ]

        # Clear existing menu items
        Menu.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing menu items.'))

        # Create new Ethiopian dishes
        created_count = 0
        for dish in ethiopian_dishes:
            Menu.objects.create(
                name=dish['name'],
                Price=dish['Price'],
                description=dish['description']
            )
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} Ethiopian dishes!')
        )

