
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hero,Values,OurServicesPage,AboutUS,HomePage,Service,ContactUS,ContactUSForm,Partners,ListServiceDetails,Partners
from .serializers import HeroSerializer,ValuesSerializer,OurServicesPageSerializer,AboutUSSerializer,HomePageSerializer,ServiceSerializer,ContactUSSerializer,ContactUSFormSerializer,PartnersSerializer,ListServiceDetailsSerializer,PartnerSerializer
from rest_framework import status


class HeroListAPIView(APIView):
    def get(self, request):
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True, context={'request': request})
        return Response(serializer.data)

class OurParntersApiView(APIView):
    def get(self, request):
        ourparnters = Partners.objects.all()
        serializer = OurParntersSerializer(ourparnters, many=True, context={'request': request})
        return Response(serializer.data)   

class ValuesApiView(APIView):
    def get(self, request):
        values = Values.objects.all()
        serializer = ValuesSerializer(values, many=True, context={'request': request})
        return Response(serializer.data)    

class ServiceItemApiView(APIView):
    def get(self,request,slug):
        print('request',request,"slug",slug)
        
        service_obj = Service.objects.filter(slug=slug).first()
        check_img_=lambda x:request.build_absolute_uri(x.image.url) if x.image else "" 
        check_img_ar=lambda x:request.build_absolute_uri(x.image_ar.url) if x.image else ""  
        check_img=lambda x:request.build_absolute_uri(x['image']) if x['image'] else "" 

        if service_obj:
           
            data={"servicesDetailed":{
                "en":{
                    "title": service_obj.title_en,
                    "image": check_img_(service_obj),
                    "servicesData": [
                                    {
                                    "title": li.title_en,
                                    "image": check_img_(li),
                                    "text":li.text_en,
                                    "vendor":[{
                                        "name":vendor.get('title_en'),
                                        
                                        "logo":check_img(vendor)
                                    } for vendor in PartnersSerializer(li.partners_id, many=True).data]
                                    }
                                for li in ListServiceDetails.objects.all().filter(service_id=service_obj.id)]
                   
                },
                "ar":{
                    "title": service_obj.title_ar,
                    "image": check_img_ar(service_obj),
                    "servicesData": [
                                    {
                                    "title": li.title_ar,
                                    "image": check_img_(li),
                                    "text":li.text_ar,
                                    "vendor":[{
                                        "name":vendor.get('title_ar'),
                                        
                                        "logo":check_img(vendor)
                                    } for vendor in PartnersSerializer(li.partners_id, many=True).data]
                                    
                                    }
                                for li in ListServiceDetails.objects.all().filter(service_id=service_obj.id)]
                   
                }
            }}
            return Response(data)  
        else:
            return Response({"servicesDetailed":{"en":{},"ar":{}}})  


class ServiceApiView(APIView):
    def get(self, request):
        service = OurServicesPage.objects.filter(show_in_service_page=True).first()
        print('service',service)
        serializer = OurServicesPageSerializer(service, many=False, context={'request': request})
        print(serializer,serializer.data)
        
        f=serializer.data  
        check_img_=lambda x:request.build_absolute_uri(x.image.url) if x.image else ""  
        check_img_ar=lambda x:request.build_absolute_uri(x.image_ar.url) if x.image_ar else ""  
        check_img=lambda x:request.build_absolute_uri(x['image']) if x['image'] else ""
        
        if service:
            result={"services":{"en":{
                    
                                    'titel':service.title_en,
                                    'text':service.text_en,
                                    
                                    "servicesData":[{
                                        "title":service_item.title_en,
                                        'image':check_img_(service_item),
                                        "slug":service_item.slug,
                                        'list':[
                                            li.title_en
                                        for li in ListServiceDetails.objects.all().filter(service_id=service_item.id)],
                                        # 'list':[{
                                        #     'title':li.title_en
                                        # }for li in ListServiceDetails.objects.all().filter(service_id=service_item.id)],
                                        
                                    } for service_item in Service.objects.all().filter(show_in_service_page=True)]
                            },
                                
                            "ar":{
                                    "title":service.title_ar,
                                    "text":service.text_ar,
                                    "servicesData":[{
                                        "title":service_item.title_ar,
                                        'image':check_img_(service_item),
                                        "slug":service_item.slug,
                                        'list':[
                                            li.title_ar
                                        for li in ListServiceDetails.objects.all().filter(service_id=service_item.id)],
                                        
                                    } for service_item in Service.objects.all().filter(show_in_service_page=True)]
                                }

            } 
            }
        else:
            result={"services":{"en":{'titel':"",
                                    'text':"",
                                    
                                    "servicesData":[]},
                                "ar":{'titel':"",
                                    'text':"",
                                    
                                    "servicesData":[]}}}  
          
        return Response(result)
        
                         

    
class AboutUSApiView(APIView):
    def get(self, request):
        result=[]
        
        aboutus=AboutUS.objects.filter(active=True).first()
        
        serializer = AboutUSSerializer(aboutus, many=False, context={'request': request})
        partners=Partners.objects.all()
        
        
        check_img_=lambda x:request.build_absolute_uri(x.image_our_vision.url) if x.image_our_vision else ""  
        check_img_ar=lambda x:request.build_absolute_uri(x.image_our_vision_ar.url) if x.image_our_vision_ar else "" 
        check_img=lambda x:request.build_absolute_uri(x.image.url) if x.image else "" 
        check_logo=lambda x:request.build_absolute_uri(x.logo.url) if x.logo else "" 
        check_image_hero_en=lambda x:request.build_absolute_uri(x.image_hero.url) if x.image_hero else "" 
        check_image_hero_ar=lambda x:request.build_absolute_uri(x.image_hero_ar.url) if x.image_hero_ar else "" 
        check_img_parent=lambda x:request.build_absolute_uri(x.image_parent.url) if x.image_parent else "" 
        check_logo_parent=lambda x:request.build_absolute_uri(x.logo_parent.url) if x.logo_parent else "" 
        
        
        def get_values_en(value):
            if value:
                return {
                    "title":value.title_our_vision_en,
                    "text":value.text_our_vision_en,
                    
                    "image":check_img_(value),
                    "list": {
                        "title": value.title_our_values_en,
                        "listData": [li.title_en for li in Values.objects.all()]
                        }
                    }
            else:
                return {
                    "title":"",
                    "text":"",
                    "image":"",
                    "list": {
                        "title": "",
                        "listData": []
                        }
                    }  
        def get_values_ar(value):
            if value:
                return {
                    "title":value.title_our_vision_ar,
                    "text":value.text_our_vision_ar,
                    
                    "image":check_img_ar(value),
                    "list": {
                        "title": value.title_our_values_ar,
                        "listData": [li.title_ar for li in Values.objects.all()]
                        }
                    }
            else:
                return {
                    "title":"",
                    "text":"",
                    "image":"",
                    "list": {
                        "title": "",
                        "listData": []
                        }
                    }    

        def get_ourParnters_en(value):
            if value:
                return {
                    "title":value.title_parent_en ,
                    "subTitle": value.subTitle_parent_en,
                    "text": value.text_parent_en,
                    "image": check_img_parent(value),
                    "logo": check_logo_parent(value)
                    }
            else:
                return {
                    "title":"" ,
                    "subTitle": "",
                    "text": "",
                    "image": "",
                    "logo": ""
                    } 
        def get_ourParnters_ar(value):
            if value:
                return {
                    "title":value.title_parent_ar ,
                    "subTitle": value.subTitle_parent_ar,
                    "text": value.text_parent_ar,
                    "image": check_img_parent(value),
                    "logo": check_logo_parent(value)
                    }
            else:
                return {
                        "title":"" ,
                        "subTitle": "",
                        "text":"",
                        "image": "",
                        "logo": ""
                    }  
       
        def get_hero_en(value):  
            if value:
                return {
                    "title": value.title_hero_en,
                    "subtitle":  value.subtitle_hero_en,
                    "text": value.text_hero_en,
                    "image":check_image_hero_en(value)
                    }
            else:
                return {
                    "title": "",
                    "subtitle":  "",
                    "text":"",
                    "image":""
                    }   

        def get_hero_ar(value):  
            if value:
                return {
                    "title": value.title_hero_ar,
                    "subtitle":  value.subtitle_hero_ar,
                    "text": value.text_hero_ar,
                    "image":check_image_hero_ar(value)
                    }
            else:
                return {
                    "title": "",
                    "subtitle":  "",
                    "text": "",
                    "image":""
                    } 
            
        
        def get_our_partner_ar(value):  
            
            data= {
                "title": value.title_our_partner_ar,
                "subtitle":  value.sub_title_our_partner_ar,
                "logoData":[check_img(img) for img in partners]
                
                }
            return data
        def get_our_partner_en(value):  
            
            data= {
                "title": value.title_our_partner_en,
                "subtitle":  value.sub_title_our_partner_en,
                "logoData":[check_img(img) for img in partners]
                
                }
            return data
            
        if aboutus:
            data={
                'en':{
                    'aboutus':aboutus.aboutus_en,
                    "hero": get_hero_en(aboutus),
                    "values":get_values_en(aboutus),
                    "ourParents":get_ourParnters_en(aboutus),
                    "ourPartnersLogo":get_our_partner_en(aboutus)
                    
                },
                'ar':{
                    'aboutus':aboutus.aboutus_ar,
                    "hero":get_hero_ar(aboutus),
                    "values": get_values_ar(aboutus),
                    "ourParents":get_ourParnters_ar(aboutus),
                    "ourPartnersLogo":get_our_partner_ar(aboutus)
                
            }}
            return Response(data)
        else:
            return Response({"en":{},"ar":{}}) 


class HomePageApiView(APIView):
    def get(self, request):
        homepage = HomePage.objects.filter(active=True).first()
        print('homepage',homepage)
        serializer = HomePageSerializer(homepage, many=False, context={'request': request})
        hero = Hero.objects.filter(show_in_home=True)
        print('serializer',serializer.data)
        f=serializer.data
        check_img=lambda x:request.build_absolute_uri(x['image']) if x['image'] else "" 
        check_img_=lambda x:request.build_absolute_uri(x.image.url) if x.image else ""  
        check_img_ar=lambda x:request.build_absolute_uri(x.image_ar.url) if x.image_ar else "" 
        partners=Partners.objects.all()
        service=Service.objects.all().filter(show_in_home=True)
         
        def get_about_hero_en(value):  
            if value:
                return {
                    "title": value.title_en,
                    "subtitle":  value.subtitle_en,
                    "text": value.text_en,
                    "image":check_img_(value)
                    }
            else:
                return {
                    "title": "",
                    "subtitle":  "",
                    "text": "",
                    "image":""
                    } 

        def get_about_hero_ar(value):  
            if value:
                return {
                    "title": value.title_ar,
                    "subtitle":  value.subtitle_ar,
                    "text": value.text_ar,
                   
                    "image":check_img_(value)
                    }
            else:
                return {
                    "title": "",
                    "subtitle":  "",
                    "text":"",
                    
                    "image":""
                    }           
        if homepage:
            data={
                'en':{
                    
                    "hero":[{
                        'title':item.title_en,
                        'description':item.description_en,
                        'image':check_img_(item)
                                }for item in hero],
                    "servicesData":[{
                        'title':item.title_en,
                        'image':check_img_(item),
                        "slug":item.slug,
                        'list':[
                            li.title_en
                        for li in ListServiceDetails.objects.all().filter(service_id=item.id)]
                                }for item in service],
                    # "AboutUsHero":get_about_hero_en(homepage.about_hero_id),
                    "AboutUsHero":get_about_hero_en(homepage),
                    "ourPartnersLogo": {
                        "title": homepage.ourPartners_title_en,
                        "subtitle": homepage.ourPartners_subtitle_en,
                        "logoData": [check_img_(img) for img in partners]
                    }                     
                    
                    
                },
                'ar':{
                
                    "hero":[{
                        'title':item.title_ar,
                        'description':item.description_ar,
                        'image':check_img_ar(item)
                                }for item in hero],
                    "servicesData":[{
                        'title':item.title_ar,
                        'image':check_img_ar(item),
                        "slug":item.slug,
                        'list':[
                            li.title_ar
                        for li in ListServiceDetails.objects.all().filter(service_id=item.id)]
                                }for item in service],
                    # "AboutUsHero":get_about_hero_ar(homepage.about_hero_id),
                    "AboutUsHero":get_about_hero_ar(homepage),
                    "ourPartnersLogo": {
                        "title": homepage.ourPartners_title_ar,
                        "subtitle": homepage.ourPartners_subtitle_ar,
                        "logoData": [check_img_(img) for img in partners]
                    }                   

                
                
            }}
            return Response(data)
        else:
            return Response({"en":{},"ar":{}})


class ContactUSApiView(APIView):
    def get(self, request):
        contact_us = ContactUS.objects.filter(active=True).first()
        print('contact_us',contact_us)
        serializer = ContactUSSerializer(contact_us, many=False, context={'request': request})
        print('serializer',serializer.data)
        f=serializer.data
          
        check_img_=lambda x:request.build_absolute_uri(x.image.url) if x.image else "" 
        check_img_ar=lambda x:request.build_absolute_uri(x.image_ar.url) if x.image_ar else "" 
        check__loc_img_=lambda x:request.build_absolute_uri(x.locaction_image.url) if x.locaction_image else "" 
        if contact_us:
            data={
                "en":{
                    "company":contact_us.company_name_en,
                    "locaction":contact_us.locaction_en,
                    "mobile_number":contact_us.mobile_number,
                    "email":contact_us.email,
                    "image":check_img_(contact_us),
                    # "locaction_image":check__loc_img_(contact_us)
                    "locaction_url":contact_us.locaction_url
                },
                "ar":{
                    "company":contact_us.company_name_ar,
                    "locaction":contact_us.locaction_ar,
                    "mobile_number":contact_us.mobile_number,
                    "email":contact_us.email,
                    "image":check_img_ar(contact_us),
                    # "locaction_image":check__loc_img_(contact_us)
                    "locaction_url":contact_us.locaction_url
                }
                
            }
            return Response(data)
        else:    
            return Response({"en":{},"ar":{}})


class ContactUSFormApiView(APIView):
    def post(self, request):
        print("request",request)
        serializer=ContactUSFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


class PartnersApiView(APIView):
    def get(self, request):
        result=[]
        services = Service.objects.all().filter(show_in_service_page=True)
        print("services",services)
        serializer = ServiceSerializer(services, many=True, context={'request': request})
        print('serializer',serializer.data)
        f=serializer.data
        
          
        check_img_=lambda x:request.build_absolute_uri(x.image.url) if x.image else "" 
        check_img=lambda x:request.build_absolute_uri(x['image']) if x['image'] else "" 
        check__loc_img_=lambda x:request.build_absolute_uri(x.locaction_image.url) if x.locaction_image else "" 
        
        
        result={"partnersData":{"en":[{
                    "title":item.title_en,
                    "partnerData": [
                        {
                        "subTitle": service_item.title_en,
                        "vendors": [{'title':partner.get('title_en'),'logo':check_img(partner)} for partner in ListServiceDetailsSerializer(service_item, many=False).data.get('partners')],
                        }
                    for service_item in ListServiceDetails.objects.all().filter(service_id=item.id)]
            }for item in services],
            "ar":[{
                    "title":item.title_ar,
                    "partnerData": [
                        {
                        "subTitle": service_item.title_ar,
                        "vendors": [{'title':partner.get('title_ar'),'logo':check_img(partner)} for partner in ListServiceDetailsSerializer(service_item, many=False).data.get('partners')],
                        }
                    for service_item in ListServiceDetails.objects.all().filter(service_id=item.id)]
            }for item in services]}}
            
               
        return Response(result)


        