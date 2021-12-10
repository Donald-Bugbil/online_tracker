from django.urls import path
from . import views

urlpatterns = [
    path(
        route='<str:username>/',
        view=views.UserDetailPage.as_view(),
        name='userdetail'
    ),
    path(
        route='<int:year>/<int:month>/<int:date>/<int:hour>/<int:minute>/<int:second>/',
        view=views.ClockinDetail.as_view(),
        name='clockindetail'
    ),
    path (
        route='<str:username>/create/',
        view = views.ClockInCreatePage.as_view(),
        name = 'clockincreatepage'
    )
]
