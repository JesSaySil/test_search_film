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

request = input ("Enter movie name part: ")
result = []

with open("films.json", "r") as f:
    f_text = json.load(f)
    print ("r")
    for i in range(0,len(f_text)):
        title_of_the_film = f_text[i]["original_title"]
        L_title = title_of_the_film.lower()
        L_request = request.lower()
        if search_word (L_title,L_request):
            result.append (title_of_the_film)
for i in range((len(result))):
    print (result[i])
        
