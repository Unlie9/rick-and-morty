from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
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


@extend_schema(
    responses={
        status.HTTP_200_OK: CharacterSerializer
    }
)
@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    """Get a random character from Rick and Morty"""
    random_character = get_random_obj_from_queryset(Character.objects.all())
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Search by name contains",
                required=False,
                type=str
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        """List characters with search by name contains"""
        return super().get(request, *args, **kwargs)
