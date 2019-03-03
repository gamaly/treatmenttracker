from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext
from django.utils.translation       import gettext_lazy as _
from django.contrib.auth.models     import User, Group


# E-mail management
from django.core.mail               import send_mail, EmailMessage, mail_admins
from .tokens             import account_activation_token
from django.template.loader         import get_template
from django.template.loader         import render_to_string
from django.contrib                 import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http              import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding          import force_bytes, force_text



def SignUpView(request):
    current_site = get_current_site(request)
    SuccessSubject = gettext('Treatment Tracker: Activate Your Account')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.age = form.cleaned_data.get('age')
            user.profile.gender = form.cleaned_data.get('gender')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            message = render_to_string('registration/NewUserEmail.html', {
                'user': user,
                'username':user.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
           
            send_mail(SuccessSubject,  #'Treatment Tracker: Activate Your Account', 
                        "", "admin@treatmenttracker.io", [user.email], fail_silently=False,html_message=message)                     
            return redirect('account_activation_sent')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

    
###############################################################################################################################################################################
###############################################################################################################################################################################
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        current_site = get_current_site(request)
        activateAlertEmail = ['gamaly@gmail.com']
        ####################################################################
        TrackerAlertSubject = 'Treatment Tracker New Account Activations'
        TrackerAlertMsg = render_to_string('registration/TreatmentTrackerActivateAlertEmail.html', {
            'username':user.username,
            'email':user.email,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        })
        ####################################################################
        ####################################################################
        send_mail(TrackerAlertSubject, 
            "", "gamaly@gmail.com", activateAlertEmail, fail_silently=False, html_message=TrackerAlertMsg)
        response = _("Thank you, this account is now active." )
        return render(request, 'registration/account_activated.html', {'response':response})
    else:
        response = _("The activation link you used has already been activated or has expired. Please contact a system administrator for assistance.")
        return render(request, 'registration/account_link_invalid.html', {'response':response})


###############################################################################################################################################################################
###############################################################################################################################################################################
def account_activation_sent(request):
    response = _("Thank you for your registering. You will receive a confirmation email with an activation link shortly.")
    return render(request, 'registration/account_activation_sent.html', {'response':response})
