def is_leap(year):
    leap = False
    
    if year%100==0 and year%400!=0:
        leap= False
    elif year%400==0:
        leap= True
    elif year%4==0:
        leap = True
    
    return leap


year= int(input("year"))

print (is_leap(year))

