from django.shortcuts import render
from django.shortcuts import render_to_response
from csi.models import Blogpost, Team , Contact, Event, Homebanner


def index(request):
    levents = Event.objects.order_by('event_id').reverse()
    ban = Homebanner.objects.order_by('banner_id').reverse()
    return render(request, 'index.html', {'levents':levents, 'ban':ban})
 




def team(request):
    myteam = Team.objects.order_by('member_id')
    return render(request, 'team.html',
                  {'myteam': myteam})


def events(request):
    myevents = Event.objects.order_by('event_id').reverse()
    return render(request, 'events.html', {'myevents':myevents})

def eventspost(request, eid ):
    epost = Event.objects.filter(event_id = eid)
    return render(request, 'eventspost.html', {'epost':epost[0]})



def blog(request):
    myposts = Blogpost.objects.all().reverse()
    print(myposts)
    return render(request, 'blog.html',
                  {'myposts': myposts})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)
    return render(request, 'blogpost.html',
                  {'post': post[0]})


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})



def error_404(request, exception, template_name="error_404.html"): 
    response = render_to_response("error_404.html") 
    response.status_code = 404 
    return response


def error_500(request): 
    response = render_to_response("error_500.html") 
    response.status_code = 500
    return response

def error_403(request, exception, template_name="error_404.html"): 
    response = render_to_response("error_500.html") 
    response.status_code = 500
    return response


def error_400(request, exception, template_name="error_404.html"): 
    response = render_to_response("error_500.html") 
    response.status_code = 500
    return response
