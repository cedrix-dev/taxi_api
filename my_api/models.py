from django.db import models

# Create your models here.
class personne(models.Model):
    nom=models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    age=models.IntegerField()
    lieuResidence=models.CharField(max_length=200)
    sexe=models.CharField(max_length=200)

class objetPerdu(models.Model): 
    description=models.CharField(max_length=200)
    date_de_perte=models.DateField()
    date_de_remise=models.DateField()
    heure_perte=models.TimeField()
    heure_remise=models.TimeField()


class taximan(personne):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    etattaximan=models.CharField(max_length=200) # bizarre 


class Message(models.Model):
    emmeteurMessage=models.CharField(max_length=200)
    recepteurMessage=models.CharField(max_length=200)
    dateEnvoie=models.DateField()
    taximan=models.ForeignKey(taximan,on_delete=models.CASCADE)
    

class passager(personne):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
class declarationDePerte(models.Model):
    descriptionObjectPerdu=models.CharField(max_length=200)
    reservation=models.CharField(max_length=200)# c'est pas une clé etrangère ?
    passager=models.ForeignKey(passager,on_delete=models.CASCADE)
    

class administrateur(personne):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    objetperdu=models.ManyToManyField(objetPerdu)
    declaration=models.ManyToManyField(declarationDePerte)
    message=models.ManyToManyField(Message)


class reservation(models.Model):
    dateReservation=models.DateField()
    etatReservation=models.CharField(max_length=200)
    passsager=models.ForeignKey(passager,on_delete=models.CASCADE)
    taximan=models.ForeignKey(taximan,on_delete=models.CASCADE)

