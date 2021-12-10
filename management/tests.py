import pytest 

pytestmark = pytest.mark.django_db
from .models import clockIn, clockOut
from accounts.models import customUserModel
from datetime import datetime


# Create your tests here.
def test__str__():
    prince = customUserModel.objects.create_user(
        username="Prince", 
        password="prince123456",

    )

    created = datetime.now()
    prince_attendance = clockIn.objects.create(teacher=prince, created=created)
    prince_clock_out = clockOut.objects.create(clock_in=prince_attendance, created = created)

    
    assert prince_attendance.__str__() == f"created on {prince_attendance.created}"
    assert str(prince_attendance) == f"created on {prince_attendance.created}"
    assert prince_clock_out.__str__() == f"updated on {prince_clock_out.created}"
    assert str(prince_clock_out) == f"updated on {prince_clock_out.created}"
