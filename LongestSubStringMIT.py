# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:22:29 2017

@author: deepak
"""
s='deepak'
i=1
subs=s[0]
subs2=s[0]
while(i<len(s)):
    j=i
    while(j<len(s)):
        if(s[j]>=s[j-1]):
            subs+=s[j]
            j+=1 
        else:
            subs=subs.replace(subs[:len(subs)],s[i])   
            break
                
        if(len(subs)>len(subs2)):
            subs2=subs2.replace(subs2[:len(subs2)], subs[:len(subs)])
    subs=subs.replace(subs[:len(subs)],s[i])
        
    if(len(subs)==len(s)):
        subs2=subs2.replace(subs2[:len(subs2)], subs[:len(subs)])
        print( "not here" )   
        break;     
            
    i+=1
print ("Longest substring in alphabetical order is:",subs2)
               