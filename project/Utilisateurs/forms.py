from django import forms
from .models import Cv, Skill, Reference, Education, Certification, Experience, Award, Interest, Contact, Social

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['profile_image', 'first_name', 'last_name', 'title', 'description']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['reference_name', 'description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['time_period', 'degree_title', 'institution']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['time_period', 'certification_title', 'description']

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['platform', 'username']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['utilisateur', 'skill_name']

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['utilisateur', 'reference_name', 'description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['utilisateur', 'time_period', 'degree_title', 'institution']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['utilisateur', 'time_period', 'certification_title', 'description']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['utilisateur', 'time_period', 'company_name', 'position_title', 'description']

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['utilisateur', 'time_period', 'award_title', 'description']

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['utilisateur', 'interest_name']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['utilisateur', 'location', 'phone_number', 'email']

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['utilisateur', 'platform', 'username']