from django.test import TestCase
# Create your tests here.
from datetime import datetime
from django.urls import reverse, resolve
from .views import PessoaAPIView, RegiaoAPIView
from .models import (
    Pessoa,
    Name,
    Location,
    Coordinate,
    Timezone,
    Picture,
    Phone,
    Cell
)

class ApiTest(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            gender='M',
            email='test@email.com',
            regiao='Sul',
            birthday='1990-11-05T09:14:15Z',
            registered='1990-11-05T09:14:15Z'
        )

        self.name = Name.objects.create(
            title='mr',
            first='andy',
            last='kiaka',
            pessoa=self.pessoa
        )

        self.location = Location.objects.create(
            street='8614 avenida vinícius de morais',
            city='ponta grossa',
            state='rondônia',
            postcode=97701,
            pessoa=self.pessoa
        )

        self.coordinate = Coordinate.objects.create(
            latitude='-76.3253',
            longitude='137.9437',
            location=self.location
        )

        self.timezone = Timezone.objects.create(
            offset='-1:00',
            description='Azores, Cape Verde Islands',
            location=self.location
        )

        self.picture = Picture.objects.create(
            large='https://randomuser.me/api/portraits/women/46.jpg',
            medium='https://randomuser.me/api/portraits/med/women/46.jpg',
            thumbnail='https://randomuser.me/api/portraits/thumb/women/46.jpg',
            pessoa=self.pessoa
        )

        self.phone = Phone.objects.create(
            phone='+550154155648',
            pessoa=self.pessoa
        )

        self.cell = Cell.objects.create(
            cell='+551082645550',
            pessoa=self.pessoa
        )

    def test_pessoa(self):
        self.assertEqual(self.pessoa.gender, 'M')
        self.assertEqual(self.pessoa.email, 'test@email.com')
        self.assertEqual(self.pessoa.regiao, 'Sul')
        self.assertEqual(self.pessoa.birthday, '1990-11-05T09:14:15Z')
        self.assertEqual(self.pessoa.registered, '1990-11-05T09:14:15Z')
    
    def test_name(self):
        self.assertEqual(self.name.title, 'mr')
        self.assertEqual(self.name.first, 'andy')
        self.assertEqual(self.name.last, 'kiaka')
        self.assertIsInstance(self.name.pessoa, Pessoa)

    def test_location(self):
        self.assertEqual(self.location.street, '8614 avenida vinícius de morais')
        self.assertEqual(self.location.city, 'ponta grossa')
        self.assertEqual(self.location.state, 'rondônia')
        self.assertEqual(self.location.postcode, 97701)
        self.assertIsInstance(self.location.pessoa, Pessoa)

    def test_coordinate(self):
        self.assertEqual(self.coordinate.latitude, '-76.3253')
        self.assertEqual(self.coordinate.longitude, '137.9437')
        self.assertIsInstance(self.coordinate.location, Location)

    def test_timezone(self):
        self.assertEqual(self.timezone.offset, '-1:00')
        self.assertEqual(self.timezone.description, 'Azores, Cape Verde Islands')
        self.assertIsInstance(self.timezone.location, Location)

    def test_picture(self):
        self.assertEqual(self.picture.large, 'https://randomuser.me/api/portraits/women/46.jpg')
        self.assertEqual(self.picture.medium, 'https://randomuser.me/api/portraits/med/women/46.jpg')
        self.assertEqual(self.picture.thumbnail, 'https://randomuser.me/api/portraits/thumb/women/46.jpg')
        self.assertIsInstance(self.picture.pessoa, Pessoa)

    def test_phone(self):
        self.assertEqual(self.phone.phone, '+550154155648')
        self.assertIsInstance(self.phone.pessoa, Pessoa)

    def test_cell(self):
        self.assertEqual(self.cell.cell, '+551082645550')
        self.assertIsInstance(self.cell.pessoa, Pessoa)

class ApiTestView(TestCase):
    
    def test_api_view(self):
        self.response = self.client.get(reverse('main'))
        view = resolve('/api/')
        self.assertEqual(
            view.func.__name__,
            PessoaAPIView.as_view().__name__
        )

    def test_api_regiao_view(self):
        self.response = self.client.get(reverse('regiao', kwargs={'pk':'Sul'}))
        view = resolve('/api/regiao/Sul')
        self.assertEqual(
            view.func.__name__,
            RegiaoAPIView.as_view().__name__
        )