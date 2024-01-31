from rest_framework import serializers
# from .models import Hero,OurParnters,Values,Service,OurServicesPage,AboutUS,HomePage,AboutUsHero,Partners,ContactUS,ContactUSForm,ListServiceDetails
from .models import Hero,Values,Service,OurServicesPage,AboutUS,HomePage,Partners,ContactUS,ContactUSForm,ListServiceDetails


class HeroSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Hero
        fields = '__all__'

    

 

class ValuesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Values
        fields = '__all__'     

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class ListServiceDetailsSerializer(serializers.ModelSerializer):
    partners=PartnerSerializer(source='partners_id',many=True)
    class Meta:
        model = ListServiceDetails
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


    
class OurServicesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServicesPage
        fields = '__all__'  

class AboutUSSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AboutUS
        fields = '__all__'                 
        

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class HomePageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HomePage
        fields = '__all__'

class ContactUSFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUSForm
        fields = '__all__' 

class ContactUSSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ContactUS
        fields = '__all__' 