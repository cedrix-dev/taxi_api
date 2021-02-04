from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from django.shortcuts import redirect

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


class personViewSet(viewsets.ModelViewSet):
    """
    c'est ici le endpoint de l'api
    """

    ## je suppose qu'on vas modifier les querysets, pour les requett
    queryset=personne.objects.all().order_by('nom')
    serializer_class=personneSerializer
    
class passagerViewSet(viewsets.ModelViewSet):
    
    ## et ça egalement
    queryset=passager.objects.all().order_by('username')
    serializer_class=passagerSerializer

class taximanViewSet(viewsets.ModelViewSet):

    ## et ça egalement
    queryset=taximan.objects.all().order_by('username')
    serializer_class=taximanSerializer

class messageViewSet(viewsets.ModelViewSet):
    ## et ça egalement
    queryset=Message.objects.all().order_by('emmeteurMessage')
    serializer_class=messageSerializer

class declarationDePerteViewSet(viewsets.ModelViewSet):
    ## et ça egalement
    queryset=declarationDePerte.objects.all().order_by('reservation')
    serializer_class=declarationDePerteSerializer

class administrateurViewSet(viewsets.ModelViewSet):
    ## et ça egalement
    queryset=administrateur.objects.all().order_by('username')
    serializer_class=administrateurSerializer

class reservationViewSet(viewsets.ModelViewSet):
    ## et ça egalement
    queryset=reservation.objects.all().order_by('passsager')
    serializer_class=reservationSerializer
    @api_view(['POST'])
    def faireReservation(self,request):
        serializer = reservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class objetPerduViewSet(viewsets.ModelViewSet):
    ## et ça egalement
    queryset=objetPerdu.objects.all().order_by('description')
    serializer_class=objetPerduSerializer


@api_view(['POST'])
def authentification(request):
    if request.method=='POST':
        username=request.data['username']
        password=request.data['password']
        type_log=request.data['type']
        try:
            if type_log=='passager':
                passager.objects.get(username=username,password=password)
            elif type_log=='taximan':
                taximan.objects.get(username=username,password=password)
            elif type_log=="admin":
                administrateur.objects.get(username=username,password=password)
            else:
                result={
                    'code':"Error type",
                    "status":"FAILLED",
                    "message":'type invalide'
                }
                return Response(result,status.HTTP_200_OK)
            result={
                'code':"HTTP_200_OK",
                'status':"SUCCESS",
                'user':username,
                'type':type_log
            }
            return Response(result , status.HTTP_200_OK)
        except:
            result={
                    "code":"Error Credentials",
                    "status":"FAILLED",
                    "username":username,
                    "message":"bad credentials"
                }
            return Response(result,status.HTTP_200_OK)
        


   
@api_view(['GET'])
def taximanDetail(request,pk):
    taximan_d=taximan.objects.get(id=pk)
    serializer=taximanSerializer(taximan_d)
    return Response(serializer.data)
@api_view(['GET'])
def objectDetail(request,pk):
    object_d=objetPerdu.objects.get(id=pk)
    serializer=objetPerduSerializer(object_d)
    return Response(serializer.data)
@api_view(['POST'])
def nouveauTaximan(request):
    serializer =taximanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def faireReservation(request):
    serializer =reservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def declarerPerte(request):
    serializer =declarationDePerteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['POST'])
def nouveauPassager(request):
    serializer =passagerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def suppPassager(request,pk):
    passage = passager.objects.get(id=pk)
    passage.delete()
    return Response('passager supprimer')

@api_view(['DELETE'])
def suppTaximan(request,pk):
    taxima = taximan.objects.get(id=pk)
    taxima.delete()
    return Response('taximan supprimer')


