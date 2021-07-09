from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionList.as_view()),
    path('flashcard/', views.FlashcardList.as_view()),
    path('collection/<int:pk>/', views.CollectionDetails.as_view()),
    path('collection/<int:collection_id>/flashcard/<int:pk>/', views.FlashcardDetails.as_view()),
]
