from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_member(user):
    return user.is_authenticated and user.role == 'Member'

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'member_dashboard.html', {"message": "Welcome, Member!"})
