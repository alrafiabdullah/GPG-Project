from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("decryptMessage", views.PostPayloadView.as_view()),
    path("api/v1/payloads", views.PayloadList.as_view()),
]
