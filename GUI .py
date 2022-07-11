#!/usr/bin/env python
# coding: utf-8

# 
# GUI

# In[13]:


names=[
   "Arun", "Arul", "Alexander", "Angel", "Aru", "Alex", "Amir", "Amirtha", "Alan", "Arjun",
   "Balaji", "Banu", "Bhavanavika", "Bhoomika", "Billy", "Barron", "Bakkiyam", "Bhaviya",
   "Chandha", "Chandhini", "Clara", "Caroline", "Carson", "Charles", "Cassius", "Carl", "Charan", "Chitra",
   "Daksha", "Daisy", "Dhaya", "Deepak", "Davind", "Dhuraisami", "Denial", "Deepika","Davin","Dhanu",
   "Elakiya", "Ezhil", "Ezra", "Elisha", "Elon", "Efren", "Egypt", "Ely", "Eren", "Emili",
   "Freya", "Falvi", "Fathima", "Falvin", "Farvin", "Fathi", "Farzeen", "Feriya", "Follan", "Fulwa",
   "Gokul", "Gauri", "Gauravi", "Gajalakshmi", "Ganga", "Gandhari", "Ganesh", "Gagakuli", "Gayathiri", "Ganika",
   "Humaira", "Hakini", "Hamiya", "Harish", "Harini", "Hanitha", "Harvesh", "Haniya", "Hagana", "Hanshini",
   "Inchara", "Idhika", "Ikshana", "Ilakiya", "Iniya", "Indira", "Indravati", "Indu", "Indumathi", "Induja",
   "Jaikumar", "Jaya", "Jaipal", "Jothi", "Jothika", "Jaimathi", "Jayanthi", "Jayamravi", "Jaisnavi", "Jamini",
   "Keerthi", "Kiran", "Karan", "Kamal", "Keerthika", "Kajal", "Kajol", "Kalaivani", "Kayal", "Kaviya",
   "Lakshmi", "Latha", "Laasya", "Lathija", "Lavanya", "Lakshita", "Lakshya", "Laila", "Lalitha", "Laranya",
   "Manoharan", "Malar", "Maanasa", "Mani", "Maina", "Madhavan", "Manisha", "Mano", "Mogana", "Monisha",
   "Nagaraj", "Narayanan", "Nayandhara", "Naresh", "Nivetha", "Nithya", "Nirmal", "Navya", "Naisha", "Nakul",
   "Oisha", "Ojaswani", "Olena", "Ojeta", "Oliya", "Onaira", "Omisha", "Oparna", "Ovie", "Oyshree",
   "Pari", "Pamila", "Paavani", "Padma", "Priya", "Paramesh", "Pooja", "Parthi", "Pavi", "Peter",
   "Raji", "Raj", "Raja", "Ramesh", "Renu", "Roja", "Rogini", "Renuka", "Ragini", "Ranjini",
   "Sasi", "Sanjay", "Sangeetha", "Sruthi", "Suganya", "Swetha" , "Sandy", "Soniya", "Sonu", "Sabitha",
   "Teju", "Tenarasi", "Tina", "Teenu", "Tamil", "Thamarai", "Thamana", "Thangam", "Thinesh", "Tharani",
   "Usha", "Udhaya", "Uvenesh", "Umaniya", "Ugesh", "Umayal", "Ushakan", "Uthayan", "Udvita", "Uma",
   "Vinitha",  "Vini", "Vino", "Vidhya", "Vinu", "Vimala", "Vani", "Varun", "Varsha", "Varshini",
   "Wasan", "Wasi", "Wishma", "Waani", "Wamana", "Wamika", "Wanasha", "Waran", "Warna", "Wilson",
   "Xiyamila", "Xaivier", "Xeno", "Xylan", "Xadiel", "Xenos", "Xamir", "Xenos", "Xander",
   "Yogesh", "Yogi", "Yoga", "Yokesh", "Yuvanesh", "Yaasika", "Yarlini", "Yashmika", "Yesha", "Yashmitha",
   "Zana", "Zofia", "Zaya", "Zobitha", "Zujitha", "Zahmy", "Zeena", "Zeno", "Zintha", "Zuhan"
]


# In[14]:


def babyname():
    letter=input("enter letter\n")
    for x in names:
        if(letter==x[0]):
            print(x)


# In[15]:


babyname()


# In[4]:


import tkinter as tk
from tkinter import *
from time import strftime
from PIL import Image, ImageTk

window_main=tk.Tk(className=" Baby Name Generator ")
window_main.geometry('1000x525')

#image for background
img=ImageTk.PhotoImage(Image.open("C:\\Users\\M.Parijatham\\Documents\\babyimage\\babypic.jpg"))
l=Label(image=img)
l.pack()
#Lable for title
title_label=tk.Label(window_main, text="DISNEY INSPIRED BABY NAMES", font=('Times New Roman',30,'bold'), foreground="black")
title_label.place(x=200 , y=5)

#Input label for user
name_label=tk.Label(window_main, text="Please Enter the Letter", font=('Times New Roman',19))
name_label.place(x=25 , y=80)

#input box of user
a_var=tk.StringVar()
alphabet_letter=tk.Entry(window_main, font=('Times New Roman',25,'bold'),textvariable=a_var).place(x=290  ,y=77.8 , 
width=180, height=40)

names=[
    "Arun", "Arul", "Alexander", "Angel", "Aru", "Alex", "Amir", "Amirtha", "Alan", "Arjun","Amy","Austin","Andrea",
    "Balaji", "Banu", "Bhavanavika", "Bhoomika", "Billy", "Barron", "Bakkiyam", "Bhaviya","Betty","Brittany","Brenda",
    "Chandha", "Chandhini", "Clara", "Caroline", "Carson", "Charles", "Cassius", "Carl", "Charan", "Chitra",
    "Daksha", "Daisy", "Dhaya", "Deepak", "Davind", "Dhuraisami", "Denial", "Deepika","Davin","Dhanu",
    "Elakiya", "Ezhil", "Ezra", "Elisha", "Elon", "Efren", "Egypt", "Ely", "Eren", "Emili",
    "Freya", "Falvi", "Fathima", "Falvin", "Farvin", "Fathi", "Farzeen", "Feriya", "Follan", "Fulwa",
    "Gokul", "Gauri", "Gauravi", "Gajalakshmi", "Ganga", "Gandhari", "Ganesh", "Gagakuli", "Gayathiri", "Ganika",
    "Humaira", "Hakini", "Hamiya", "Harish", "Harini", "Hanitha", "Harvesh", "Haniya", "Hagana", "Hanshini",
    "Inchara", "Idhika", "Ikshana", "Ilakiya", "Iniya", "Indira", "Indravati", "Indu", "Indumathi", "Induja",
    "Jaikumar", "Jaya", "Jaipal", "Jothi", "Jothika", "Jaimathi", "Jayanthi", "Jayamravi", "Jaisnavi", "Jamini",
    "Keerthi", "Kiran", "Karan", "Kamal", "Keerthika", "Kajal", "Kajol", "Kalaivani", "Kayal", "Kaviya",
    "Lakshmi", "Latha", "Laasya", "Lathija", "Lavanya", "Lakshita", "Lakshya", "Laila", "Lalitha", "Laranya",
    "Manoharan", "Malar", "Maanasa", "Mani", "Maina", "Madhavan", "Manisha", "Mano", "Mogana", "Monisha",
    "Nagaraj", "Narayanan", "Nayandhara", "Naresh", "Nivetha", "Nithya", "Nirmal", "Navya", "Naisha", "Nakul",
    "Oisha", "Ojaswani", "Olena", "Ojeta", "Oliya", "Onaira", "Omisha", "Oparna", "Ovie", "Oyshree",
    "Pari", "Pamila", "Paavani", "Padma", "Priya", "Paramesh", "Pooja", "Parthi", "Pavi", "Peter",
    "Raji", "Raj", "Raja", "Ramesh", "Renu", "Roja", "Rogini", "Renuka", "Ragini", "Ranjini",
    "Sasi", "Sanjay", "Sangeetha", "Sruthi", "Suganya", "Swetha" , "Sandy", "Soniya", "Sonu", "Sabitha",
    "Teju", "Tenarasi", "Tina", "Teenu", "Tamil", "Thamarai", "Thamana", "Thangam", "Thinesh", "Tharani",
    "Usha", "Udhaya", "Uvenesh", "Umaniya", "Ugesh", "Umayal", "Ushakan", "Uthayan", "Udvita", "Uma",
    "Vinitha",  "Vini", "Vino", "Vidhya", "Vinu", "Vimala", "Vani", "Varun", "Varsha", "Varshini",
    "Wasan", "Wasi", "Wishma", "Waani", "Wamana", "Wamika", "Wanasha", "Waran", "Warna", "Wilson",
    "Xiyamila", "Xaivier", "Xeno", "Xylan", "Xadiel", "Xenos", "Xamir", "Xenos", "Xander",
    "Yogesh", "Yogi", "Yoga", "Yokesh", "Yuvanesh", "Yaasika", "Yarlini", "Yashmika", "Yesha", "Yashmitha",
    "Zana", "Zofia", "Zaya", "Zobitha", "Zujitha", "Zahmy", "Zeena", "Zeno", "Zintha", "Zuhan"
 ]

# function
def babyname():
    for i in names:
        if i[0][0].lower()==a_var.get().lower():
            textarea.insert(END,(i+"\n"))
#button to load
display_button=tk.Button(window_main, font=('Times New Roman',25,'bold'), foreground='black' ,background='green', 
text='click',command=babyname)
display_button.place(x=200  ,y=135 , width=70, height=45)


def displayfunc():
    a_var.set("0.0 ")
    textarea.append("0.1" ,"end")

# text area
textarea_var=tk.StringVar()
textarea=tk.Text(window_main, font=('Times New Roman',17))
textarea.place(x=28,y=200,width=500,height=290)

#function for clear
def clearFunc():
    a_var.set("")
    textarea.delete("1.0","end")
#clear button
clear_button=tk.Button(window_main,font=('Times New Roman',12,'bold'),foreground="black",background="white",text="Clear",
command=clearFunc)
clear_button.place(x=550 ,y=480,width=65 ,height=30)


#Exit button
exit_button=tk.Button(window_main,font=('Times New Roman',12,'bold'), foreground="black",background="red", text="Exit",
command=window_main.destroy)
exit_button.place(x=640 ,y=480,width=65 ,height=30)



window_main.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




