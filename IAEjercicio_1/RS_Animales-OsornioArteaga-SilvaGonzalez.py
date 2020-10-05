# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:22:59 2020

@author: juanc
"""
ConocimientoEs = [
        ("TORTUGA","SAUROPSIDOS"),
        ("GALLO","SAUROPSIDOS"),        
        ("COCODRILO","SAUROPSIDOS"),        
        ("IGUANA","SAUROPSIDOS"),
        ("GATO","MAMMALIA"),
        ("BALLENA","MAMMALIA"),
        ("OSO","MAMMALIA"),
        ("DELFIN","MAMMALIA"),
        ("TORTUGA","OVIPARO"),
        ("GALLO","OVIPARO"),        
        ("COCODRILO","OVIPARO"),        
        ("IGUANA","OVIPARO"),
        ("GATO","VIVIPARO"),
        ("BALLENA","VIVIPARO"),
        ("OSO","VIVIPARO"),
        ("DELFIN","VIVIPARO"),
        ("TORTUGA","VERTEBRADOS"),
        ("GALLO","VERTEBRADOS"),
        ("COCODRILO","VERTEBRADOS"),
        ("IGUANA","VERTEBRADOS"),
        ("GATO","VERTEBRADOS"),
        ("BALLENA","VERTEBRADOS"),
        ("OSO","VERTEBRADOS"),
        ("DELFIN","VERTEBRADOS"),
        ("MAMMALIA","VIVIPARO"),
        ("VIVIPARO","VERTEBRADOS"),
        ("SAUROPSIDOS","OVIPARO"),
        ("OVIPARO","VERTEBRADOS"),
        ("TORTUGA","TETRAPODOS"),
        ("COCODRILO","TETRAPODOS"),
        ("IGUANA","TETRAPODOS"),
        ("GATO","TETRAPODOS"),
        ("OSO","TETRAPODOS")
]

ConocimientoTiene = [
        ("COCODRILO","GARRAS"),
        ("GATO","GARRAS"),
        ("OSO","GARRAS"),
        ("GATO","PELO"),
        ("OSO","PELO"),
        ("MAMMALIA","G MAMARIAS"),
        ("SAUROPSIDOS","PROTECCION QUERATINA")
]

ConocimientoVive = [
        ("TORTUGA","AGUA"),
        ("TORTUGA","TIERRA"),
        ("GALLO","TIERRA"),        
        ("COCODRILO","AGUA"),
        ("COCODRILO","TIERRA"),
        ("IGUANA","TIERRA"),
        ("GATO","TIERRA"),
        ("BALLENA","AGUA"),
        ("OSO","TIERRA"),
        ("DELFIN","AGUA")
]

def es(A,B,CON1):
    r=0
    l=len(CON1)
    while r!=l :
        if CON1[r][0] == A:
            if CON1[r][1] == B:
                return True
        r+=1
    else:
        return False
    
def tiene(A,B,CON2):
    r=0
    l=len(CON2)
    while r!=l :
        if CON2[r][0] == A:
            if CON2[r][1] == B:
                return True
        r+=1
    else:
        return False
    
def vive(A,B,CON3):
    r=0
    l=len(CON3)
    while r!=l :
        if CON3[r][0] == A:
            if CON3[r][1] == B:
                return True
        r+=1
    else:
        return False

print(es("COCODRILO","SAUROPSIDOS",ConocimientoEs))
print(es("TORTUGA","MAMMALIA",ConocimientoEs))
print(tiene("BALLENA","PROTECCION QUERATINA",ConocimientoTiene))
print(tiene("IGUANA","PELO",ConocimientoTiene))
print(vive("TORTUGA","AGUA",ConocimientoVive))
print(vive("DELFIN","TIERRA",ConocimientoVive))