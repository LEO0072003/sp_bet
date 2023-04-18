import time
import json
import requests
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.response import Response

# Create your views here.


class RegisterUserApiView(generics.CreateAPIView):
    """Viewset for Registering User"""

    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer



class FetchBettDetailsApiView(APIView):
    """Viewset For fetching and storing sports Bets """

    permission_classes = [IsAuthenticated]

    def get(self,*args,**kwargs):
        """Method To Handle Get request"""

        sports = ['MLB', 'CPB', 'TNS', 'FTB']
        game_date = '2023-04-18' # 請更改至一個月內的日期
        access_token = 'FREE_20_TIMES_PRE_DAY_FOR_TEST_ONLY'
        endpoint = 'https://api.sportsbot.tech/odds_movements'
        results = {}
        for sport in sports:
            url = endpoint + '/' + sport + '/' + game_date
            params = {'access_token': access_token}
            response = requests.get(url, params=params)
            result = json.loads(response.text)
            results.update({f"{sport}" : result})
            time.sleep(5)
        return Response(results)



