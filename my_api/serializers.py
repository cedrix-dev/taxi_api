from .models import *
from rest_framework import serializers

class personneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=personne
        fields=['nom','prenom','age','lieuResidence','sexe']


class taximanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=taximan
        fields=['nom','prenom','age','lieuResidence','sexe','username','password','etattaximan']
class administrateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=administrateur
        fields=['nom','prenom','age','lieuResidence','sexe','username','password',]

class messageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Message
        fields=['emmeteurMessage','recepteurMessage','dateEnvoie']
class objetPerduSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=objetPerdu
        fields=['description','date_de_perte','date_de_remise','heure_perte','heure_remise']

class reservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=reservation
        fields=['dateReservation','etatReservation','passsager','taximan']
class declarationDePerteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=declarationDePerte
        fields=['descriptionObjectPerdu','reservation','passager']
class passagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=passager
        fields=['nom','prenom','age','lieuResidence','sexe','username','password']
