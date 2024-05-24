from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserLoginForm, VacancyForm, ResumeForm, UserCreationForm
from .models import Vacancy, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')
        if password1 != password2:
            return render(request, 'registration.html', {'error_message': 'Далбаэб??'})
        user = User.objects.create_user(username, email, password1)
        if role == 'appliciant':
            user.groups.add(Group.objects.get(name='Applicant'))
        elif role == 'company':
            user.groups.add(Group.objects.get(name='Company'))
        login(request, user)
        if role == 'appliciant':
            return redirect('home_appliciant/')
        elif role == 'company':
            return redirect('home_company/')
        else:
            return redirect('home_page/')
    else:
        return render(request, 'registration.html')


def login_view(request):
    return render(request, 'login.html')


def create_job_view(request):
    return render(request, 'create_job.html')


def create_resume_view(request):
    return render(request, 'create_resume.html')


def home_appliciant(request):
    return render(request, 'home_appliciant.html')


def job_list_view(request):
    return render(request, 'jobs_list.html')


def resume_list_view(request):
    return render(request, 'resume_list.html')


def home_company(request):
    return render(request, 'home_company.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                pass
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def create_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_company')  # +=+
    else:
        form = VacancyForm()
    return render(request, 'create_vacancy.html', {'form': form})


def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_appliciant')  # =+=
    else:
        form = ResumeForm()
    return render(request, 'create_resume.html', {'form': form})


def vacancy_list(request):
    category = request.GET.get('category', None)
    vacancies = Vacancy.objects.all()
    if category:
        vacancies = vacancies.filter(category=category)
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})


def recommend_vacancies(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_skills = user_profile.skills
    all_vacancies = Vacancy.objects.all()
    recommended_vacancies = []
    for vacancy in all_vacancies:
        if any(skill in user_skills for skill in vacancy.skills):
            recommended_vacancies.append(vacancy)
    return render(request, 'recommended_vacancies.html', {'recommended_vacancies': recommended_vacancies})


def home_page(request):
    return render(request, 'home.html')


@login_required
def register(request):
    user = request.user
    if user.role == 'appliciant':
        resumes = user.resumes.all()
        vacancies = Vacancy.objects.all()
        return render(request, 'home_appliciant.html', {'resumes': resumes, 'vacancies': vacancies})
    elif user.role == 'company':
        vacancies = user.vacancies.all()
        return render(request, 'home_company.html', {'vacancies': vacancies})
    else:
        return render(request, 'home.html')











