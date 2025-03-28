from django.shortcuts import render
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

oauth = OAuth()
oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration'
)

def home(request):
    
    return render(
        request,
        "krutiverse/home.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("home")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("home")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
    
  

def complete_profile(request):
    return render(request, "complete_profile.html")

def donor_profile(request):
    return render(request, "donor_profile.html")

def recipient_profile(request):
    return render(request, "recipient_profile.html")




    # Get the user info from Auth0
    token = oauth.auth0.authorize_access_token(request)
    userinfo = token.get('userinfo')

    # Check if user exists in our database
    try:
        user_profile = UserProfile.objects.get(auth0_user_id=userinfo['sub'])
        # Existing user - redirect to appropriate dashboard
        return redirect('donor_profile' if user_profile.is_donor else 'recipient_profile')
    except UserProfile.DoesNotExist:
        # New user - store auth0 user_id in session and redirect to complete profile
        request.session['auth0_user_id'] = userinfo['sub']
        request.session['email'] = userinfo['email']
        request.session['name'] = userinfo.get('name', '')
        return redirect('complete_profile')



