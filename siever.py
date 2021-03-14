# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:28:20 2021

@author: steph
"""
import pandas as pd

#print(len(st))
#print(len(en))
#print(len(dst))
#print(len(den))

def sievecomments(filename, out_file):
    st = ' <span dir="ltr"><span class="_3l3x"><span>'
    en = '</span></span></span></div></div></div></div>'
    out = []
    output = []
    with open(filename, 'r', encoding="utf8") as file:
        s = file.read()
        print(len(s))
        for i in range(len(s)):
            if s[i:i+43] == st:
                j = 0
                while s[i+43+j:i+43+j+45] != en:
                    j += 1
                out.append([i, i+43+j])
                print('appended')
                
        for item in out:
            output.append(s[item[0]+43:item[1]])
            print('appended')    
            
    df = pd.DataFrame(output)
    df.to_excel(out_file,sheet_name = "Comments")
    file.close()
        
        

def sievedate(filename, out_file):
    dst = '<abbr data-tooltip-content="'
    den = '" data-hover="tooltip"'
    date = []
    dateout = []
    with open(filename, 'r', encoding="utf8") as file:
        s = file.read()
        print(len(s))
        for a in range(len(s)):
            if s[a:a+28] == dst:
                k = 0
                while s[a+28+k:a+28+k+22] != den:
                    k+=1
                date.append([a, a+28+k])
                print('appended date ind')
        for ind in date:
            dateout.append(s[ind[0]+28:ind[1]])
        
        for idx, item in enumerate(dateout):
            for l in range(len(item)):
                if item[l:l+4] == " at ":
                    item = item[:l]+","+item[l+4:]
                    dateout[idx] = item
                if item[l:l+1] == ":":
                    item = item[:l]+item[l+1:]
                    dateout[idx] = item
            
    df = pd.DataFrame(dateout)
    df.to_excel(out_file,sheet_name = "D&T")
    file.close()

def sievename(filename, out_file):
    nst = '<img alt="'
    nen = '" class="'
    namind = []
    name = []
    with open(filename, 'r', encoding="utf8") as file:
        s = file.read()
        print(len(s))
        for a in range(len(s)):
            if s[a:a+10] == nst:
                k = 0
                while s[a+10+k:a+10+k+9] != nen:
                    k+=1
                namind.append([a, a+10+k])
                print('appended name ind')
        for ind in namind:
            name.append(s[ind[0]+10:ind[1]])
        
    df = pd.DataFrame(name)
    df.to_excel(out_file,sheet_name = "Username")
    file.close()

def sievelink(filename, out_file):
     lst = 'href="https://www.facebook.com/'
     lend = '?comment_id='
     lind = []
     links = []
     with open(filename, 'r', encoding="utf8") as file:
        s = file.read()
        print(len(s))

        for a in range(len(s)):
            if s[a:a+31] == lst:
                k = 0
                while s[a+31+k:a+31+k+12] != lend:
                    k+=1
                    if k == 459271:
                        break
                lind.append([a, a+31+k])
                print('appended link ind')

        for ind in lind:
            links.append(s[ind[0]+6:ind[1]])
     
     i = 0
     n = len(links)             
     while i < n-1:
        check = links[i]
        if check == links[i+1]:
            del links[i+1]    
            n -= 1
        else:
            i += 1
    
     i = 0
     n = len(links)
     while i < n:
         check= links[i]
         if 'https://www.facebook.com/TenteraDaratMY/posts' in check:
             del links[i]
             n -= 1
         else:
             i += 1


         
             
     df = pd.DataFrame(links)        
     df.to_excel(out_file,sheet_name = "Links")
     file.close()


