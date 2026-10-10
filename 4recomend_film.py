import json

def search_word(text: str, search: str):
    if len(text) < len(search):
        return False
    len_text = len(text)
    len_search = len(search)
    for i in range(len_text - len_search+1):
        if text[i:i+len_search] == search:
            return True
    return False

def search_word(text: str, search: str):
    if len(text) < len(search):
        return False
    len_text = len(text)
    len_search = len(search)
    for i in range(len_text - len_search+1):
        if text[i:i+len_search] == search:
            return True
    return False

def collect_genres(film_genres):
    list_of_genres = []
    for i in range(0,len(film_genres)):
        list_of_genres.append(film_genres[i]["name"])
    return list_of_genres

def search_genres (film, catalog):
    for filmN in catalog:
        if "original_title" in filmN:
            if filmN["original_title"] == film:
                return collect_genres(filmN["genres"])
    return "not found"

def genres_relatability (list1, list2):
    N = 0
    for i in range (0,len(list2)):
        if list2[i] in list1:
            N += 1

    if N == 1 and len(list1) == 1:
        return True
    elif N >= 2:
        return True
    else:
        return False

result_simular_names = []

while result_simular_names == []:
    request_original = input ("Enter movie name part: ")
    title_list = []
    result_simular_names = []

    with open("films2.json", "r") as f:
        f_text = json.load(f)

        for i in range(0,len(f_text)):
            if "original_title" in f_text[i]:
                title_of_the_film = f_text[i]["original_title"]
                l_title = title_of_the_film.lower()
                l_request = request_original.lower()
                if search_word (l_title,l_request):
                    result_simular_names.append (title_of_the_film)

    if result_simular_names == []:
        print ("Try again")

request = result_simular_names[0]
print (request)

with open("films2.json", "r") as f:
    f_text = json.load(f)
    list_of_genres = search_genres(request, f_text)
    print (list_of_genres)

    for i in range(0,len(f_text)):
        if "original_title" in f_text[i]:
            list_of_genres2 = collect_genres(f_text[i]["genres"])
            if genres_relatability(list_of_genres,list_of_genres2):
                title_list.append(f_text[i]["original_title"])

title_list.remove(request)
for i in range (0,len(title_list)):
    print (title_list[i])
