
def saisieChaineMajuscules(question):
    inputOk=False
    while not inputOk:    
        chaine=input(question)
        lgChaine=len(chaine)
        inputOk=True
        for i in range(lgChaine):
            code=ord(chaine[i])
            if not (code>=65 and code<=90):
                inputOk=False
    return chaine


def cleSousFormedEntiers(cle):
    nbDec=len(cle)
    liste=[] 
    for i in range(nbDec):
        code=ord(cle[i])
        #ramener le decalage de 0 à 25
        dec=code-65
        liste.append(dec)
    return liste


def codageVigenere(chaine, liste):   
    lgChaine=len(chaine)
    nbDec=len(liste)
    chaineCodee=""

    for i in range(lgChaine):
        code=ord(chaine[i])
        #il n'y a que des majuscules        
        code=(code-65+liste[i%nbDec])%26+65
        chaineCodee=chaineCodee+chr(code)

    return chaineCodee

def decodageVigenere(chaine, liste):
    lgChaine=len(chaine)
    nbDec=len(liste)
    chaineDecodee=""
    
    for i in range(lgChaine):
        code=ord(chaine[i])
        #traiter les majuscules
        if (code>=65 and code<=90):
            code=code-65 #on raisonne de 0 à 25
            code=((code-liste[i%nbDec])%26)+65
        chaineDecodee=chaineDecodee+chr(code)
    return chaineDecodee

question1="chaine (majuscules) ? >>> "
chaine=saisieChaineMajuscules(question1);
question2="clé (majuscules) ? >>> "
cle=saisieChaineMajuscules(question2);

liste=cleSousFormedEntiers(cle)

message="la liste des valeurs de décalage est: "+str(liste)
print(message)

chaineCodee=codageVigenere(chaine, liste)
message="Chaine codée: "+chaineCodee
print(message)

chaineDecodee=decodageVigenere(chaineCodee, liste)
message="Chaine décodée: "+chaineDecodee
print(message)
