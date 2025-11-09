from django.core.management.base import BaseCommand
from content.models import ContactInfo, PackagePrice


class Command(BaseCommand):
    help = 'Populate initial content data'

    def handle(self, *args, **kwargs):
        # Create ContactInfo
        if not ContactInfo.objects.exists():
            ContactInfo.objects.create(
                phone='+4917610716264',
                email='jarin.z@hotmail.de',
                instagram_handle='atma_bhavaka',
                instagram_url='https://www.instagram.com/instagram_profile',
                facebook_name='Atma Bhavaka',
                facebook_url='https://www.facebook.com/profile.php?id=61568685404582',
                workshop_address_line1='FB Deurvoorstraat 10',
                workshop_address_line2='7071BH Ulft',
                company_name='Van Emmichoven',
                company_address_line1='FB Deurvoorstraat 10',
                company_address_line2='7071BH Ulft',
                company_kvk='87915138'
            )
            self.stdout.write(self.style.SUCCESS('Created ContactInfo'))
        else:
            self.stdout.write(self.style.WARNING('ContactInfo already exists'))

        # Create PackagePrices
        packages = [
            {
                'name': 'First Lesson Special',
                'price': 18.00,
                'description': 'Offer: €9 off the first lesson',
                'details': 'Price: €18 for a single 3-hour session\nDetails: Get started with a discounted rate on your first session.',
                'payment_url': 'https://tikkie.me/pay/VanEmmichov/3w1pwfyQUkuXMRGDfGD3vC',
                'qr_code_image': 'QR-first.png',
                'order': 1
            },
            {
                'name': 'Single Session',
                'price': 27.00,
                'description': 'One 3-hour session',
                'details': 'Price: €27\nDetails: One 3-hour session with no commitment, ideal for a single drop-in experience.',
                'payment_url': 'https://tikkie.me/pay/VanEmmichov/5w4Za7bHhnx5GXLWDpNfdH',
                'qr_code_image': 'QR-single.png',
                'order': 2
            },
            {
                'name': '3-Day Pass',
                'price': 78.00,
                'description': '€26 per session',
                'details': 'Price: €78 (€26 per session)\nValidity: Use within 3 months\nDetails: Access any 3 sessions with a small discount to encourage consistency.\nSavings: €3 discount',
                'payment_url': 'https://tikkie.me/pay/VanEmmichov/jhWdr1fiz33YHziz4CwXCu',
                'qr_code_image': 'QR-3day.png',
                'order': 3
            },
            {
                'name': '5-Day Pass',
                'price': 126.00,
                'description': '€25.20 per session',
                'details': 'Price: €126 (€25.20 per session)\nValidity: Use within 5 months\nDetails: Enjoy five sessions with a moderate discount for regular practice.\nSavings: €9 discount',
                'payment_url': 'https://tikkie.me/pay/VanEmmichov/tHJ2ekc9sBni5bhP3rXGZt',
                'qr_code_image': 'QR-5day.png',
                'order': 4
            },
            {
                'name': '7-Day Pass',
                'price': 171.00,
                'description': '€24.43 per session',
                'details': 'Price: €171 (€24.43 per session)\nValidity: Use within 6 months\nDetails: A 7-session option with a larger discount, ideal for deeper engagement.\nSavings: €18 discount',
                'payment_url': 'https://tikkie.me/pay/VanEmmichov/xcGKdorUj7XRCkJp6Q6LAn',
                'qr_code_image': 'QR-7day.png',
                'order': 5
            },
            {
                'name': 'Stemexpressie Basic Course',
                'price': 127.00,
                'description': '12 hours (three hours per evening)',
                'details': 'The cost of the basic course is €127\nThe basic course lasts 12 hours (three hours per evening)',
                'payment_url': 'https://tikkie.me/pay/VanEmmichov/tQFjmpdmysN9fxVVM2AHcs',
                'qr_code_image': 'QR-Stemexpressie .png',
                'order': 6
            },
        ]

        for pkg_data in packages:
            pkg, created = PackagePrice.objects.get_or_create(
                name=pkg_data['name'],
                defaults=pkg_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created package: {pkg.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Package already exists: {pkg.name}'))

        self.stdout.write(self.style.SUCCESS('Initial content population complete!'))
