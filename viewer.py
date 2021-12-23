from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Dev's Image Viewer")
root.iconbitmap('c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/icon.ico')

my_img7= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic1.jpg"))
my_img6= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic2.jpg"))
my_img3= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic3.jpg"))
my_img4= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic4.jpg"))
my_img5= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic5.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic6.jpg"))
my_img1= ImageTk.PhotoImage(Image.open("c:/Users/Devansh-PC/Desktop/Python Projects/Viewer/pic7.jpg"))

image_list= [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7]

#Status Bar
status=Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label=Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

#Button Foward
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number== len(image_list):
        button_forward=Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status=Label(root, text="Image " + str(image_number) + " of  " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#Button Back
def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back=Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    #Status Bar
    status=Label(root, text="Image " + str(image_number) + " of  " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)    
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


#designing buttons initially
button_back=Button(root, text="<<", command=back, state=DISABLED)
button_exit=Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward=Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()