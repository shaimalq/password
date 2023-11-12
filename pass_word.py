def nbcmin(passe):
    count=0
    for car in passe:
        if car>="a" and car<="z":
            count+=1
            return count
def nbcmaj(passe):
  count=0
  for car in passe:
        if car>="A" and car<="Z":
            count+=1
            return count
def nbcalpha(passe):
      count=0
      for car in passe:
        if (car.alpha)or (car.digit):
            count+=1
            return count
def score(passe):
    score=nbcmaj(passe)*2
    score= nbcalpha(passe)*5
    score=len(passe)*4
    score=nbcmin(passe)*2
    return score  
passeword=input("entrer le mot de passe")
if score<20:
    print("tres faible")
if score<=40:
    print(" faible")
if score<=80:
    print(" fort")
else:
    print("tres fort")