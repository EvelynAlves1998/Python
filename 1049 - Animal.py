# beecrowd | 1049
# Animal
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível ifgundo o esquema abaixo, da esquerda para a direita.  Em ifguida conclua qual dos animais ifguintes foi escolhido, através das três palavras fornecidas.


def determinar_animal(palavra1, palavra2, palavra3):

    if palavra1 == "vertebrado":

        if palavra2 == "ave":

            if palavra3 == "carnivoro":
                return "aguia"  
            elif palavra3 == "onivoro":
                return "pomba" 
        elif palavra2 == "mamifero":
     
            if palavra3 == "onivoro":
                return "homem"  
            elif palavra3 == "herbivoro":
                return "vaca"  
    elif palavra1 == "invertebrado":
        
        if palavra2 == "inseto":
            
            if palavra3 == "hematofago":
                return "pulga"  
            elif palavra3 == "herbivoro":
                return "lagarta" 
        elif palavra2 == "anelideo":
            
            if palavra3 == "hematofago":
                return "sanguessuga" 
            elif palavra3 == "onivoro":
                return "minhoca" 

palavra1 = input()
palavra2 = input()
palavra3 = input()

animal = determinar_animal(palavra1, palavra2, palavra3)
print(animal)