from rest_framework import serializers
from .models import Book, B_rating

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre" ]

class B_ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = B_rating
        fields = ["id", "rating", "description"]
    #
    # def create(self, validated_data):
    #     book_id = self.context["book_id"]
    #     profile_id =self.context["user_id"]
    #     rating = B_rating.objects.create(book_id = book_id, profile_id = profile_id, **self.validated_data)
    #     return rating
