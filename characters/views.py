from django.shortcuts import render
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import Max
import random

from characters.models import Character
from characters.serializers import CharacterSerializer


def get_random_obj_from_queryset(queryset):
    max_pk = queryset.aggregate(max_pk=Max("pk"))['max_pk']
    while True:
        obj = queryset.filter(pk=random.randint(1, max_pk)).first()
        if obj:
            return obj


@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    random_character = get_random_obj_from_queryset(Character.objects.all())
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
