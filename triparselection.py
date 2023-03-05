# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 23:17:43 2023

@author: Daryl
"""

def tri_par_sélection(list):
    for i in range(len(list)):
        minimum=i
        for j in range(i+1,len(list)):
            if list[j]<list[i]:
                minimum=list[j]
                list[j]=list[i]
                list[i]=minimum
        j=j+1
    i=i+1        
    return list 

list=[2,2,15,7,9,0]                                                                  
tri_par_sélection(list)
print(list)
                
                