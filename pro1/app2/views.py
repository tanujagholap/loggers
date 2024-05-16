from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Otp
from .serializers import UserSerializers
from uuid import uuid4
from rest_framework.response import Response

import logging

logger = logging.getLogger( 'demo_loggers' )

class DemoAPIView(APIView):
    def get(self, request):
        logger.warning('some warning..')
        return Response(data={'msg': 'logs......'})




class OtpAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = str(uuid4())
        Otp.objects.create(email=email, otp=otp)
        return Response(data={'msg': 'done......'})


class UserAPIView(APIView):
    def post(self, request):
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            username = request.data.get('username')
            otp = request.data.get('otp')
            otp_obj = get_object_or_404(Otp, email=username, otp=otp)
            if otp_obj:
                serializers.save()
                return Response(data={'msg': 'save...'})
        return Response(data={'msg': 'done!!!!!!'})
