# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:04:01 2021

@author: TEFJE
"""

#importerer biblioteker for å kontrollere om det er skuddår


import calendar 
from datetime import date

#finner i år og kontrollere om i år er skuddår

dato =date.today()
aar=dato.year
skuddaar=calendar.isleap(aar)


#Klassen bilkost som innholder alle attributene nødvendig for å beregne kost pr år
#og funksjoner for å kalkulere kostnad og differanse for en gitt kjørelengde

class bil:
    '''Klassen bilkost som innholder alle attributene nødvendig for å beregne kost pr år
    og funksjoner for å kalkulere kostnad og differanser for en gitt kjørelengde for en drivstofftype. 

    tar argumentene ("forsikring, årsavgift, drivstoff, bom) som er: 
    forsikringskost pr år, 
    trafikkforsikringsavgift pr dag
    drivstoff kost pr km og 
    bom kost pr km'''
    
    def __init__(self, forsikring, aarsavgift, forbruk, bom):
        
        #atributter i klassen, årsavgift regnes om til kr/år ved å gang med 366 eller 365 om det er skuddår eller ikke
        
        self.forsikring = forsikring
         
        if skuddaar:
            self.aarsavgift = aarsavgift*366
        else:
            self.aarsavgift = aarsavgift*365
        self.forbruk = forbruk
        self.bom = bom
    #funsjon som regner kostnad for en gitt kjørelengde        
    def kostPerAar(self, kjoreLengde):
        """funksjon til klassen bilkost som tar argumentet kjorelengde i km pr år og beregner kost basert på attributer i objektet"""
        return(((self.forsikring+self.aarsavgift+(self.forbruk*kjoreLengde)+(self.bom*kjoreLengde))))
    
    def differanse(self, other,kjoreLengde):
        """funksjon som beregner differansen mellom denne instansen og en annen for en gitt kjørelengde. 
        tar argumentene (other,kjoreLengde) som er:
        other er ett objekt av samme klasse
        kjøreLengde er kjørelengde i km per år det skal regnes en differanse for"""
        
        return (self.kostPerAar(kjoreLengde)-other.kostPerAar(kjoreLengde))

#opperetter bil objektene med gitte attributter for oppgaven 
elbil = bil(5000,5.85,(0.2*0.9),0.1)
bensinbil = bil(7000,8.4,1,0.3)


#bruker funksjonene kostPerAar i bilkost klassen og beregner kost for elbil.
#skriver det ut formatert til 2 desimaler med print funksjonen  
print("Elbil kostnad pr år med kjørelengde 10 000 km: " + str(format(elbil.kostPerAar(10000),'.2f'))+"kr")
#bruker funksjonene kostPerAar i bilkost klassen og beregner kost for elbil 
print("Bensinbil kostnad pr år med kjørelengde 10 000 km: " + str(format(bensinbil.kostPerAar(10000),'.2f'))+"kr")
#bruker funksjonen kostnadsdifferanse og regner kostnads differansen for bensinbil og elbil
print("kostnadsdifferansen mellom bensinbil og elbil blir: "+ str(format((bensinbil.differanse(elbil,10000)),'.2f'))+ "kr per år for år "+str(aar))
