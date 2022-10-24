from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Request, Response, status
from movie.models import Movie


from review.models import Review
from review.permissions import IsAdminOrReadOnly

from review.serializers import ReviewSerializer

from rest_framework.pagination import PageNumberPagination

from rest_framework.authentication import TokenAuthentication

from user.permissions import IsCriticOrOwner


# Create your views here.
class ReviewView(APIView, PageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        reviews = Review.objects.all().filter(movie=movie_id)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = Movie.objects.get(id=movie_id)

        request.data["movie"] = movie.id

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(critic=request.user)

        return Response(serializer.data)


class ReviewDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsCriticOrOwner]

    def get(self, request: Request, movie_id: int, review_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        review = get_object_or_404(Review, id=review_id)

        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int, review_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        review = get_object_or_404(Review, id=review_id)

        self.check_object_permissions(request, review.critic)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
