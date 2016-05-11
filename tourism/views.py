from django.shortcuts import render

# Create your views here.

def home_page(request):
	return render(request,'tourism/base_file.html')

def hotel_booking(request):
	return render(request,'tourism/files/hotel_booking.html')

def visa(request):
	return render(request,'tourism/files/visa.html')

def hajj_package(request):
	return render(request,'tourism/files/hajj_package.html')

def hajj_intro(request):
	return render(request,'tourism/files/hajj_intro.html')

def hajj_guides_tips(request):
	return render(request,'tourism/files/hajj_guides_tips.html')

def common_mistakes(request):
	return render(request,'tourism/files/common_mistakes.html')

def hajj_tour_faqs(request):
	return render(request,'tourism/files/hajj_faqs.html')

def hajj_schedule(request):
	return render(request,'tourism/files/hajj_schedule.html')

def hajj_booking_form(request):
	return render(request,'tourism/files/hajj_booking_form.html')

def umrah_package(request):
	return render(request,'tourism/files/umrah_package.html')

def umrah_intro(request):
	return render(request,'tourism/files/umrah_intro.html')

def umrah_how(request):
	return render(request,'tourism/files/umrah_how.html')

def umrah_booking_form(request):
	return render(request,'tourism/files/umrah_booking_form.html')

def booking_form(request):
	return render(request,'tourism/files/booking_form.html')
def hajj_interest_form(request):
	return render(request,'tourism/files/hajj_interest_form.html')

def umrah_interest_form(request):
	return render(request,'tourism/files/umrah_interest_form.html')

def membership(request):
	return render(request,'tourism/files/membership.html')

def media_gallery(request):
	return render(request,'tourism/files/media_gallery.html')

def live_coverage(request):
	return render(request,'tourism/files/live_coverage.html')

def islamic_tour(request):
	return render(request,'tourism/files/islamic_tour.html')

def terms_and_conditions(request):
	return render(request,'tourism/files/terms_and_conditions.html')

def all_mekkah_hotels(request):
	return render(request,'tourism/files/all_mekkah_hotels.html')

def all_medinah_hotels(request):
	return render(request,'tourism/files/all_medinah_hotels.html')

def online_payment(request):
	return render(request,'tourism/files/online_payment.html')

def about_us(request):
	return render(request,'tourism/files/about_us.html')

def contact_us(request):
	return render(request,'tourism/files/contact_us.html')

def flight_booking(request):
	return render(request,'tourism/files/flight_booking.html')