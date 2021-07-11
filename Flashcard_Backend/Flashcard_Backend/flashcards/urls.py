from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionList.as_view()),
    path('flashcards/', views.FlashcardList.as_view()),
    path('collection/flashcards/<int:collection_id>', views.FlashcardsInCollection.as_view()),
    path('collection/<int:pk>/', views.CollectionDetails.as_view()),
    path('collection/flashcards/<int:collection_id>/<int:pk>', views.FlashcardDetails.as_view()),
]
