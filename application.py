from fun_lib import *

print('''Qual tipo de busca deseja realizar? Selecione uma das opções:
- PERFIL 
- HASHTAG
''')
scraper_input = str(input())
upper_case = scraper_input.upper()

while(upper_case != "PERFIL") and (upper_case != "HASHTAG") :
    print('''>>> INFORME UM MÉTODO VÁLIDO <<<
Qual tipo de busca deseja realizar? Selecione uma das opções:
- PERFIL 
- HASHTAG
''')
    scraper_input = str(input())
    upper_case = scraper_input.upper()

if(upper_case == "PERFIL"):
    new_scraper_input = str(input("Informe qual perfil você deseja buscar: "))
    lower_case = new_scraper_input.lower()
    search_profile(lower_case)

elif(upper_case == "HASHTAG"):
    new_scraper_input = str(input("Informe qual hashtag você deseja buscar: "))
    lower_case = new_scraper_input.lower()
    search_hashtag(lower_case)    

