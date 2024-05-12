from EnglSite.models import dictonary
from django.db.models import F

def db_get_word():
    dic = []
    for i, item in enumerate(dictonary.objects.all().order_by("eng_word")):
        dic.append([i+1, item.eng_word, item.rus_word])
    return dic

def db_write_word(n_eng_word='', n_rus_word=''):
    if dictonary.objects.filter(eng_word=n_eng_word).exists():
        return False
    else:
        dic = dictonary(eng_word = n_eng_word.lower(), rus_word = n_rus_word.lower())
        dic.save()
        return True

def update_word(n_eng_word, n_rus_word=''):
    if dictonary.objects.filter(eng_word=n_eng_word).exists():
        dictonary.objects.filter(eng_word = n_eng_word).update(rus_word = n_rus_word)
        return True
    else: 
        return False

def delete(n_eng_word=''):
    if dictonary.objects.filter(eng_word=n_eng_word).exists():
        dictonary.objects.filter(eng_word=n_eng_word).delete()
    else:
        return False

def take():
    dic = []
    for i, item in enumerate(dictonary.objects.order_by("?")[:6]):
        dic.append([i+1, item.eng_word, item.rus_word])
    return dic

def check_translate(words):
    answer = []
    word = dictonary.objects 
    for i in range(len(words)):
        for item in word.filter(eng_word = words[i][0]):
            if words[i][1] == item.rus_word:
                answer.append([item.eng_word, item.rus_word, words[i][1], True])
            else:
                answer.append([item.eng_word, item.rus_word, words[i][1], False])
    return answer
