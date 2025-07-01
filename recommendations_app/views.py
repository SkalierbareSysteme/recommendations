import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .models import Recommendation


@api_view(['GET'])
def healthcheck(request):
    return HttpResponse({"Recommendation service is alive!"})


@api_view(['GET'])
def get_all_recommendations(request):
    recommendations = Recommendation.objects.filter(amount_of_recommendations__gte=3).values()
    return JsonResponse(list(recommendations), safe=False, status=200)


@api_view(['GET'])
def get_recommendation(request, recommendation_id):
    recommendation = get_object_or_404(Recommendation, id=recommendation_id)

    recommendation_json = {
        'name': recommendation.name,
        'description': recommendation.description,
        'address': recommendation.address,
        'tags': recommendation.tags,
        'posted_by': recommendation.posted_by,
        'posted_on': recommendation.posted_on,
        'poster_id': recommendation.poster_id,
        'amount_of_recommendations': recommendation.amount_of_recommendations,
        'reviewer_id': recommendation.reviewer_id
    }

    return JsonResponse(recommendation_json, status=200, safe=False)


@api_view(['POST'])
def add_recommendation(request):

    request_body = json.loads(request.body)

    r_name = request_body.get('name')
    r_address = request_body.get('address')
    r_tags = request_body.get('tags')
    r_description = request_body.get('description')
    #reviewer_id?

    recommendation = Recommendation.objects.create(
        name=r_name,
        address=r_address,
        tags=r_tags,
        description=r_description,
        posted_by="guy",
        poster_id="1",
        amount_of_recommendations=1,
        reviewer_id=0,
    )

    return JsonResponse({"Recommendation:": recommendation.id}, status=200)


@api_view(['DELETE'])
def delete_recommendation(request, recommendation_id):
    recommendation = get_object_or_404(Recommendation, id=recommendation_id)
    rec_id = recommendation.id
    name = recommendation.name

    recommendation.delete()

    return HttpResponse({f"deleted recommendation {name} with id: {rec_id}"}, status=200)


@api_view(['PATCH'])
def update_amount_of_recommendations(request, recommendation_id):
    recommendation = get_object_or_404(Recommendation, id=recommendation_id)
    old_amount = recommendation.amount_of_recommendations
    recommendation.amount_of_recommendations += 1

    recommendation.save()
    new_amount = recommendation.amount_of_recommendations

    return HttpResponse({f"new amount {new_amount}. old amount {old_amount}"}, status=200)