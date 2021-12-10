from django.urls import path 
from . import views 

urlpatterns = [
    path(
        route='custom-email/',
        view= views.VerifyPage.as_view(),
        name = 'verifypage'
    )
]
