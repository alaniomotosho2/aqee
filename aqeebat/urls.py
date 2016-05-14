"""aqeebat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',"tourism.views.home_page",name="home_page"),
    url(r'^hotelbooking/$',"tourism.views.hotel_booking",name="hotel_booking"),
    url(r'^visa/$',"tourism.views.visa",name="visa"),
    url(r'^hajj-tour-faqs/$',"tourism.views.hajj_tour_faqs",name="hajj_tour_faqs"),
    url(r'^hajj-schedule/$',"tourism.views.hajj_schedule",name="hajj_schedule"),
    url(r'^hajj-intro/$',"tourism.views.hajj_intro",name="hajj_intro"),
    url(r'^umrah-intro/$',"tourism.views.umrah_intro",name="umrah_intro"),
    url(r'^hajj-booking-form/$',"tourism.views.hajj_booking_form",name="hajj_booking_form"),
    url(r'^hajj-guides-tips/$',"tourism.views.hajj_guides_tips",name="hajj_guides_tips"),
    url(r'^common-mistakes/$',"tourism.views.common_mistakes",name="common_mistakes"),
    url(r'^umrah-package/$',"tourism.views.umrah_package",name="umrah_package"),
    url(r'^umrah-how/$',"tourism.views.umrah_how",name="umrah_how"),
    url(r'^umrah-booking-form/$',"tourism.views.umrah_booking_form",name="umrah_booking_form"),
    url(r'^hajj-package/$',"tourism.views.hajj_package",name="hajj_package"),
    url(r'^booking-form/$',"tourism.views.booking_form",name="booking_form"),
    url(r'^hajj-interest-form/$',"tourism.views.hajj_interest_form",name="hajj_interest_form"),
    url(r'^umrah-interest-form/$',"tourism.views.umrah_interest_form",name="umrah_interest_form"),
    url(r'^membership/$',"tourism.views.membership",name="membership"),
    url(r'^media-gallery/$',"tourism.views.media_gallery",name="media_gallery"),
    url(r'^live-coverage/$',"tourism.views.live_coverage",name="live_coverage"),
    url(r'^islamic-tour/$',"tourism.views.islamic_tour",name="islamic_tour"),
    url(r'^all-mekkah-hotels/$',"tourism.views.all_mekkah_hotels",name="all_mekkah_hotels"),
    url(r'^all-medinah-hotels/$',"tourism.views.all_medinah_hotels",name="all_medinah_hotels"),
    url(r'^terms-and-conditions/$',"tourism.views.terms_and_conditions",name="terms_and_conditions"),
    url(r'^online-payment/$',"tourism.views.online_payment",name="online_payment"),
    url(r'^about-us/$',"tourism.views.about_us",name="about_us"),
    url(r'^contact-us/$',"tourism.views.contact_us",name="contact_us"),
    url(r'^quote/$',"tourism.views.quote",name="quote"),
    url(r'^flight-booking/$',"tourism.views.flight_booking",name="flight_booking"),
    url(r'^tourism/', include('tourism.urls',namespace='tourism',app_name='tourism')),
]
