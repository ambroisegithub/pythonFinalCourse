# unitest  in django

from django.test import TestCase
from .models import reservations
from datetime import datetime
# from . import modelsReservation
# Create your tests here.

class reservationModelTestCase(TestCase): 
    
    @classmethod
    def setUpTestData(cls):
        
        cls.reservation = reservations.objects.create(
            
            first_name = "ambroise",
            last_name = "Shakur"
        )

    def test_fields(self):
        
        self.assertIsInstance(self.reservation.first_name,str)
        self.assertIsInstance(self.reservation.last_name,str)
        
    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time,datetime)    
        
