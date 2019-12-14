from django.shortcuts import render

def log(request):
    return render(request, 'log.html')

def signup(request):
    return render(request, 'signup.html')

def for_candidates(request):
    return render(request, 'for_candidates.html')

def for_employers(request):
    return render(request, 'for_employers.html')

def candidate_profile(request):
    return render(request, 'candidate_profile.html')

def post_job(request):
    return render(request, 'post_job.html')

def candidates(request):
    return render(request, 'candidates.html')

def employers_profile(request):
    return render(request, 'employers_profile.html')

def search(request):
    return render(request, 'search.html')
