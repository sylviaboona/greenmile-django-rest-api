from django.urls import path
from . import views
from .views import LoadersList, SuppliersList, PackagesList

urlpatterns = [
    path('loaders/', LoadersList.as_view()),
    path('suppliers/', SuppliersList.as_view()),
    path('packages/', PackagesList.as_view())
]