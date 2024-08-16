from django.urls import path

from characters.views import get_random_character_view, CharacterListView

urlpatterns = [
    path("characters/", CharacterListView.as_view(), name="character-list"),
    path("get_random_character/", get_random_character_view, name="get-character"),
]

app_name = "characters"
