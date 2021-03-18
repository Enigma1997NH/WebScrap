#........................................................................................................................................
import builtwith
import whois
import time
from tkinter import messagebox
from tkinter import *
import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
main.title("Web Scraping")
main.geometry("500x700")

list1 = ['https://www.programiz.com','http://authoraditiagarwal.com','https://www.tutorialspoint.com','https://www.geeksforgeeks.org','https://stackoverflow.com/',
         'https://www.yahoo.com','https://www.amazon.in','https://www.indiatimes.com','https://www.instagram.com','https://www.office.com','https://www.medium.com',
         'https://www.naukri.com','https://www.irctc.co.in','https://www.justdial.com','https://www.tumblr.com','https://www.wordpress.com','https://www.manoramaonline.com',
         'https://www.whatsapp.com','https://www.linkedin.com'
        ]

#Function To Scraping Data of Website eg:Programming language,framework,server
def web():
    list2 = []
    for i in range(len(list1)):
        
        print(list1[i])
        data = builtwith.parse(list1[i])
        st = str(data)
        list2.append(st)

    return list2

#Function to Scraping Data of Owner's 
def who():
    list2 = []
    for i in range(len(list1)):
        print(list1[i])
        data = whois.whois(list1[i])
        st = str(data)
        #time.sleep(1)
        #print(st)
        list2.append(st)
        text.insert(END,st+"done");

    return list2

def save_file():
    list2 = []
    for i in range(len(list1)):
        
        
        data = builtwith.parse(list1[i])
        st = str(data)
        list2.append(st)

    list3 = []
    for i in range(len(list1)):
        
        data = whois.whois(list1[i])
        st = str(data)
        list3.append(st)
    
        
    with open('ScrapedData.txt','w+',encoding = 'utf-8') as f1:
        for itmes in list2:
            f1.write('%s\n' %itmes)



    with open('OwnerData.txt','w+',encoding = 'utf-8') as f2:
        for itmes in list3:
            f2.write('%s\n' %itmes)

            
    with open('WebsiteData.txt','w+',encoding = 'utf-8') as f3:
        for itmes in list1:
            f3.write('%s\n' %itmes)



font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=50)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=50,y=120)
text.config(font=font1)

font1 = ('times', 14, 'bold')
Button = Button(main, text="For Web Scrap", command=web, bg='#ffb3fe')
Button.place(x=100,y=50)
Button.config(font=font1)

font1 = ('times', 14, 'bold')
Button = Button(main, text="Who is Owner", command=who, bg='#ffb3fe')
Button.place(x=300,y=50)
Button.config(font=font1)

font1 = ('times', 14, 'bold')
Button = Button(main, text="Save as TXT", command=save_file, bg='#ffb3fe')
Button.place(x=200,y=550)
Button.config(font=font1)


main.config(bg="Blue")
main.mainloop()
#..............................................................................................................................................................
