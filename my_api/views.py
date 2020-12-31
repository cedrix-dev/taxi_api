from .models import *
from rest_framework import viewsets,permissions
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

class objetPerduViewSet(viewsets.ModelViewSet):
    ## et ça egalement
    queryset=objetPerdu.objects.all().order_by('description')
    serializer_class=objetPerduSerializer
