from django.shortcuts import render
from django.http import HttpResponse
from second.models import *


def takeSecond(elem):
    return elem[1]


def personal_page(request):
    user = User.objects.get(u_Name='zhangsan')
    return render(request, 'personalpage.html', {"user": user})


def register(request):
    m = request.method
    if m == 'GET':
        return render(request, 'register.html')
    else:
        u_name = request.POST.get('name', '')
        pwd = request.POST.get('password', '')
        if u_name and pwd:
            user = User()
            user.u_Name = u_name
            user.u_Password = pwd
            user.save()
            return HttpResponse('处理成功')
        else:
            return HttpResponse('chulishibai')


def push(request):
    user_tags = User_tag.objects.filter(Name='zhangsan')
    movies = []
    index = []
    result = []
    for user_tag in user_tags:
        temps = Movie.objects.filter(m_tag=user_tag.tag)
        if movies:
            for temp in temps:
                if temp.m_name in movies:
                    index[movies.index(temp.m_name)] += 1
                else:
                    movies.append(temp.m_name)
                    index.append(1)
        else:
            for temp in temps:
                movies.append(temp.m_name)
                index.append(1)
    for movie in movies:
        grade = Grade.objects.get(m_name=movie)
        if grade.m_grade:
            result.append((movie, index[movies.index(movie)]+float(grade.m_grade)*0.52))
        else:
            result.append((movie, index[movies.index(movie)] + 5.6 * 0.52))
    result.sort(key=takeSecond, reverse=True)
    print(result)
    return HttpResponse('chulishibai')


def push_fur(request):
    result = []
    user_tags = User_tag.objects.filter(Name='lisi')
    for user_tag in user_tags:
        O_movies = Movie.objects.filter(m_tag=user_tag.tag)
        for O_movie in O_movies:
            if O_movie.m_name not in O_movies:
                result.append(O_movie.m_name)
    print(result)
    return HttpResponse('chulishibai')
