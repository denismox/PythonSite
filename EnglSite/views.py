from django.shortcuts import render
from django.core.cache import cache
from eng import ORM_dict

def for_base(request):
    return render(request, 'for_base.html')

def dictonary(request):
    dic = ORM_dict.db_get_word()
    return render(request, 'dictonary.html', context={"dic" : dic})

def write_word(request):
    return render(request, 'write_word.html')

def check(request):
    chec = ORM_dict.take()
    return render(request, 'check.html', context={"chec" : chec})

def send_check(request):
    if request.method == "POST":
        cache.clear()
        words = list(request.POST.items())
        answer = ORM_dict.check_translate(words)
    return render(request, "check_translate.html", context={"answer": answer})

def send_word(request):
    if request.method == "POST":
        cache.clear()
        n_eng_word = request.POST.get("n_eng_word")
        n_rus_word = request.POST.get("n_rus_word", "")
        context = {}
        if len(n_eng_word) == 0:
            context["success"] = False
            context["comment"] = "Поле с иностранным словом обязательно нужно заполнить"
        elif len(n_rus_word) == 0:
            context["success"] = False
            context["comment"] = "Поле с переводом обязательно нужно заполнить"
        else:
            if ORM_dict.db_write_word(n_eng_word, n_rus_word):
                context["success"] = True
                context["comment"] = "Слово добавлено"
            else:
                context["success"] = False
                context["comment"] = "Такое слово уже есть"
        return render(request, "write_word_request.html", context)
    else:
        write_word(request)

def delete_word(request):
    if request.method == "POST":
        cache.clear()
        n_eng_word = request.POST.get("n_eng_word")
        # n_rus_word = request.POST.get("n_rus_word", "")
        context = {}
        if len(n_eng_word) == 0:
            context["success"] = False
            context["comment"] = "Поле с иностранным словом обязательно нужно заполнить"
        elif ORM_dict.delete(n_eng_word):
            context["success"] = False
            context["comment"] = "Такого слова нет в словаре"  
        else:
            context["success"] = True
            context["comment"] = "Слово удалено"
        if context["success"]:
            context["success-title"] = ""
        return render(request, "write_word_request.html", context)
    else:
        write_word(request)

def update_word(request):
    if request.method == "POST":
        cache.clear()
        n_eng_word = request.POST.get("n_eng_word")
        n_rus_word = request.POST.get("n_rus_word", "")
        context = {}
        if len(n_eng_word) == 0:
            context["success"] = False
            context["comment"] = "Поле с иностранным словом обязательно нужно заполнить"
        elif len(n_rus_word) == 0:
            context["success"] = False
            context["comment"] = "Поле с переводом обязательно нужно заполнить"
        else:
            if ORM_dict.update_word(n_eng_word, n_rus_word):
                context["success"] = True
                context["comment"] = "Слово обновлено"
            else:
                context["success"] = False
                context["comment"] = "Такого слова нет в словаре"
        return render(request, "write_word_request.html", context)
    else:
        write_word(request)
# Create your views here.
