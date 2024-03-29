from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxValueMultiFieldValidator



class Utilisateur(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    REGIONS_CHOICES = [
    ('TANGER-TÉTOUAN-AL HOCEIMA', 'Tanger-Tétouan-Al Hoceima'),
    ('ORIENTAL', 'Oriental'),
    ('FÈS-MEKNÈS', 'Fès-Meknès'),
    ('RABAT-SALÉ-KÉNITRA', 'Rabat-Salé-Kénitra'),
    ('BÉNI MELLAL-KHÉNIFRA', 'Béni Mellal-Khénifra'),  
    ('CASABLANCA-SETTAT', 'Casablanca-Settat'),
    ('MARRAKECH-SAFI', 'Marrakech-Safi'),
    ('DRÂA-TAFILALET', 'Drâa-Tafilalet'),
    ('SOUSS-MASSA', 'Souss-Massa'),
    ('GUELMIM-ES-SEMARA', 'Guelmim-Oued Noun'),
    ('LAÂYOUNE-SAKIA EL HAMRA', 'Laâyoune-Sakia El Hamra'),
    ('DAKHLA-OUED ED-DAHAB', 'Dakhla-Oued Ed-Dahab'),
]
    region=models.CharField(choices=REGIONS_CHOICES,max_length=255,default='TANGER-TÉTOUAN-AL HOCEIMA')
    photo_profil=models.ImageField(upload_to='photos/photos_Profil',null=True,blank=False, default='photos/photos_Profil/user_image.png')
    nom = models.CharField(max_length=50,default='&&')
    prenom = models.CharField(max_length=50, default='&&')
    date_naissenc=models.DateField(null=True)       
    PROFIL_CHOICES = [
        ('etu', 'Etudiant'),
        ('ens', 'Enseignant'),
        ('ent','entreprise'),   #just added
    ]
    is_public = models.BooleanField(default=True)  # Attribute for public/private profile

    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_users', blank=True)

    type_profil = models.CharField(choices=PROFIL_CHOICES, max_length=3, default='etu')
    email = models.EmailField(null=True, blank=True)
    
    tele = models.CharField(max_length=20, null=True, blank=True) #just added
    GENDER_CHOICES = [  #just added
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    def __str__(self):
        
        return f"{self.nom} {self.prenom}"
    
    

class Etudiant(Utilisateur):
    filiere=models.CharField(max_length=255)
    #just added
    institution = models.CharField(max_length=255, default='Université XYZ')
    major = models.CharField(max_length=255, default='Génie logiciel')
    year_of_study = models.IntegerField(default=1)
    degree = models.CharField(max_length=255, default='Licence')
    top_skills = models.CharField(max_length=255, default='Python, Django, HTML')
    experiences = models.TextField(default='Aucune expérience')

    def __str__(self):
        return super().__str__()
    


class projet(models.Model):
    nom=models.CharField(max_length=255)
    description=models.TextField()
    date_creation=models.DateTimeField( auto_now_add=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    


class Cv(models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    date_naissance=models.DateField()
    email=models.EmailField( max_length=254)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$',message='le numero de telephone doit etre saisir dans un format valide')
    telephone=models.CharField(validators=[phone_regex],max_length=20,blank=True)
    comptences=models.TextField(max_length=500)
    experiences=models.TextField()
    formaion=models.TextField()
    langues_choices = [
    ('FR', 'Français'),
    ('EN', 'Anglais'),
    ('ES', 'Espagnol'),
    ('ar','arabe')
    ]
    langues=MultiSelectField(choices=langues_choices,max_choices=4, validators=[MaxValueMultiFieldValidator(4)])
    centre_interet=models.TextField(max_length=255)
    utilisateur=models.OneToOneField(Utilisateur,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.utilisateur.nom} {self.utilisateur.prenom}"
    

class Enseignant(Utilisateur):
    departement_choices= [
        ('GI','GENIE INFORMATIQUE'),
        ('GM','GENIE MECANIQUE'),
        ('GC','GENIE CHIMIQUE'),
        ('SDT','SIENCES DE LA TERRE'),
        ('SDV','SIECES DE LA VIE'),
        ('GE','GENIE ELECTRIQUE'),   
    ]
    departement=models.CharField(choices=departement_choices,max_length=50)
    
    def __str__(self):
        return super().__str__()
    

class formation(models.Model):
    titre=models.CharField(max_length=100)
    description=models.TextField()
    date_debut=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_fin=models.DateField( auto_now=False, auto_now_add=False)
    etudiant=models.ManyToManyField(Etudiant)
    def __str__(self) :
        return self.titre

class ActivitePedarogique(models.Model):
    titre=models.CharField(max_length=100)
    date=models.DateField( auto_now=False, auto_now_add=False)
    nombres_participants=models.IntegerField()
    description=models.TextField()
    enseignant=models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    def __str__(self):
        return self.titre





# class Etudiant(Utilisateur):






# Create your models here.
