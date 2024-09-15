from django.urls import path
from .views import FruitFAQListCreate, FruitFAQRetrieveUpdateDelete

urlpatterns = [
    path('faqs/', FruitFAQListCreate.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FruitFAQRetrieveUpdateDelete.as_view(), name='faq-detail'),
]
