from django.core.management.base import BaseCommand
from content.models import PageContent


class Command(BaseCommand):
    help = 'Populate page content sections'

    def handle(self, *args, **kwargs):
        # Home page quote
        quote_obj, created = PageContent.objects.get_or_create(
            page='home',
            section_key='quote',
            defaults={
                'title': 'Quote',
                'content': '''༺  ༻
A way to root ourselves deep into the ground.
A way to experience a deep connection to the people around us.
A way of finding our inner voice and expressing it with all our heart, mind and soul!
A way to become more playful and joyful by means of connecting to our inner child.
A way to release blocked emotions and receive therapeutic benefits.
A way to connect to an ancient and sacred part within ourselves.
༺  ༻''',
                'order': 1
            }
        )
        if not created:
            quote_obj.content = '''༺  ༻
A way to root ourselves deep into the ground.
A way to experience a deep connection to the people around us.
A way of finding our inner voice and expressing it with all our heart, mind and soul!
A way to become more playful and joyful by means of connecting to our inner child.
A way to release blocked emotions and receive therapeutic benefits.
A way to connect to an ancient and sacred part within ourselves.
༺  ༻'''
            quote_obj.save()
        
        # Book page - Atma Bhavaka description
        PageContent.objects.get_or_create(
            page='book',
            section_key='atma_bhavaka_intro',
            defaults={
                'title': 'Atma Bhavaka',
                'content': 'Ātmā Bhāvaka is a practice that blends the insights of ancient spiritual traditions with modern psychological principles...',
                'order': 1
            }
        )
        
        # Book page - Stemexpressie description
        PageContent.objects.get_or_create(
            page='book',
            section_key='stemexpressie_intro',
            defaults={
                'title': 'Stemexpressie',
                'content': 'What is Stemexpressie? Stemexpressie (voice-expression) is a playful and liberating way...',
                'order': 2
            }
        )
        
        # Learn page sections
        learn_sections = [
            {
                'section_key': 'what_is_atma_bhavaka',
                'title': 'What is Ātmā Bhāvaka?',
                'content': 'Editable content for this section',
                'order': 1
            },
            {
                'section_key': 'roots_of_atma_bhavaka',
                'title': 'Roots of Ātmā Bhāvaka',
                'content': 'Editable content for this section',
                'order': 2
            },
            {
                'section_key': 'spirituality_meets_science',
                'title': 'Spirituality Meets Science',
                'content': 'Editable content for this section',
                'order': 3
            },
            {
                'section_key': 'science_of_atma_bhavaka',
                'title': 'Science of Ātmā Bhāvaka',
                'content': 'Editable content for this section',
                'order': 4
            },
        ]
        
        for section in learn_sections:
            PageContent.objects.get_or_create(
                page='learn',
                section_key=section['section_key'],
                defaults=section
            )
        
        # About page content
        PageContent.objects.get_or_create(
            page='about',
            section_key='about_content',
            defaults={
                'title': 'About',
                'content': 'Editable about page content',
                'order': 1
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Page content sections created!'))
