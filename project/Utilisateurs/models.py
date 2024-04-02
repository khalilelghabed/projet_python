from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxValueMultiFieldValidator
    
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    region=models.TextField(choices=REGIONS_CHOICES,max_length=255,default='TANGER-TÉTOUAN-AL HOCEIMA')
    photo_profil=models.ImageField(upload_to='photos/photos_Profil',null=True,blank=False, default='photos/photos_Profil/user_image.png')
    nom = models.CharField(max_length=50,default='&&')
    prenom = models.CharField(max_length=50, default='&&')
    date_naissenc=models.DateField(null=True,blank=False )       
    PROFIL_CHOICES = [
        ('etu', 'Etudiant'),
        ('ens', 'Enseignant'),
        ('ent','entreprise'),  
    ]
    is_public = models.BooleanField(default=True)  # Attribute for public/private profile

    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_users', blank=True)

    type_profil = models.CharField(choices=PROFIL_CHOICES, max_length=3, default='ent')
    email = models.EmailField(null=True, blank=True)
    
    tele = models.CharField(max_length=20, null=True, blank=True) #just added
    GENDER_CHOICES = [  #just added
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    bio = models.TextField(max_length=255, null=True, blank=True)
    def is_following(self, other_user):
        return self.following.filter(id=other_user.id).exists()

    def follow(self, other_user):
        if not self.is_following(other_user):
            self.following.add(other_user)
            other_user.followers.add(self)

    def unfollow(self, other_user):
        if self.is_following(other_user):
            self.following.remove(other_user)
            other_user.followers.remove(self)
            
    def __str__(self):
        return f"{self.prenom} {self.nom}"
   

@receiver(post_save, sender=User)
def create_utilisateur(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        Utilisateur.objects.create(user=instance)
    
    
    



class MyModel(models.Model):
    my_field = MultiSelectField(choices=[('value1', 'Value 1'), ('value2', 'Value 2')], max_length=100)
    
class Etudiant(Utilisateur):
    filiere=models.CharField(max_length=255)
    institution = models.CharField(max_length=255, default='Université XYZ')
    major = models.CharField(max_length=255, default='Génie logiciel')
    year_of_study = models.IntegerField(default=1)
    degree = models.CharField(max_length=255, default='Licence')
    top_skills = models.CharField(max_length=255, default='Python, Django, HTML')
    
    
    def __str__(self):
        return super().__str__()
    

class Entreprise(Utilisateur):
    company_name = models.CharField(max_length=50, default='Company X')
    owner_name = models.CharField(max_length=50, default='Sam smith')
    website3 = models.TextField(max_length=255, default='www.website.com')
    size = models.CharField(max_length=20, default='99')
    specialties =  models.TextField(max_length=255,default='Specialties')
    certifications = models.TextField(max_length=255,default='certifications')
    location = models.TextField(max_length=255,default='locations')
    working_days = models.TextField(max_length=255,default='everyday')
    def __str__(self):
        return super().__str__()
class Entreprise(models.Model):
    Industry=models.CharField(max_length=255)
    


class projet(models.Model):
    nom=models.CharField(max_length=255)
    description=models.TextField(default='')
    date_creation=models.DateTimeField( auto_now_add=True)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    





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
    specialty = models.TextField(max_length=255, default='IT')
    portfolio = models.TextField(max_length=255, default='www.portfolio.com')
    experiences=models.TextField(max_length=255, default='None')
    institution = models.CharField(max_length=255, default='Université XYZ')
    portfolio2 = models.TextField(max_length=255, default='www.portfolio.com')
    
    experiences2=models.TextField(max_length=255, default='None')
    institution2 = models.CharField(max_length=255, default='Université XYZ')


    def __str__(self):
        return super().__str__()
    

class formation(models.Model):
    titre=models.CharField(max_length=100)
    description=models.TextField(default='')
    date_debut=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_fin=models.DateField( auto_now=False, auto_now_add=False)
    etudiant=models.ManyToManyField(Etudiant)
    def __str__(self) :
        return self.titre

class ActivitePedarogique(models.Model):
    titre=models.CharField(max_length=100)
    date=models.DateField( auto_now=False, auto_now_add=False)
    nombres_participants=models.IntegerField()
    description=models.TextField(default='')
    enseignant=models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    def __str__(self):
        return self.titre


# cv models
    


class Cv(models.Model):
    utilisateur = models.OneToOneField('Utilisateur', on_delete=models.CASCADE, blank=False, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')  # Provide a default value for description
    skills = models.ManyToManyField('Skill', blank=True)
    references = models.ManyToManyField('Reference', blank=True)
    educations = models.ManyToManyField('Education', blank=True)
    certifications = models.ManyToManyField('Certification', blank=True)
    experiences = models.ManyToManyField('Experience', blank=True)
    awards = models.ManyToManyField('Award', blank=True)
    interests = models.ManyToManyField('Interest', blank=True)
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE, null=True, blank=True)
    social = models.OneToOneField('Social', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"CV of {self.utilisateur}"

    def save(self, *args, **kwargs):
        if not self.first_name:
            self.first_name = self.utilisateur.prenom
        if not self.last_name:
            self.last_name = self.utilisateur.nom
        if not self.title:
            self.title = self.utilisateur.type_profil
        if not self.description:
            self.description = self.utilisateur.bio
        super().save(*args, **kwargs)


class Skill(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    skill_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.skill_name

class Reference(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    reference_name = models.CharField(max_length=100, null=True)
    description = models.TextField(default='', null=True)

    def __str__(self):
        return self.reference_name

class Education(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    time_period = models.CharField(max_length=100, null=True)
    degree_title = models.CharField(max_length=100, null=True)
    institution = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.degree_title

class Certification(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    time_period = models.CharField(max_length=100, null=True)
    certification_title = models.CharField(max_length=100, null=True)
    description = models.TextField(default='', null=True)

    def __str__(self):
        return self.certification_title

class Experience(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    time_period = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    position_title = models.CharField(max_length=100, null=True)
    description = models.TextField(default='', null=True)

    def __str__(self):
        return self.position_title

class Award(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    time_period = models.CharField(max_length=100, null=True)
    award_title = models.CharField(max_length=100, null=True)
    description = models.TextField(default='', null=True)

    def __str__(self):
        return self.award_title

class Interest(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    interest_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.interest_name

class Contact(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.email

class Social(models.Model):
    PLATFORM_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('GitHub', 'GitHub'),
        # Add more platforms as needed
    ]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)
    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.platform}: {self.username}"
# class Etudiant(Utilisateur):
