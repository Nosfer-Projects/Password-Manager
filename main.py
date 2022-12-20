
import random
from tkinter import *
from tkinter import messagebox
import json



def generator():
  """
  Function that creates a combination of upper case letters, lower case letters, numbers and special characters to create a strong password
  """
  pass_entry.delete(0, END)  
  letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
    'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
  password_nr = [random.choice(numbers) for _ in range(random.randint(2, 4))]
  password_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]

  password_list = password_letters + password_nr + password_sym
  random.shuffle(password_list)

  password = "".join(password_list)



  pass_entry.insert(0, password) 


def save():
  """
  Function retrieves data from the program. Checks if all fields in the program are filled in, then adds a new password, login and website to the json file.
  """
  
    page= web_entry.get()
    e_mail = email_entry.get()
    password = pass_entry.get()

    new_data = {
        page :{
            "email" : e_mail,
            "password": password

        }

    }


    if page == "" or e_mail == "" or password == "":
        messagebox.showwarning(title = "Error", message= "Please fill all fields! ")
    else:
            try:
                with open ("data.json", "r") as file:
                    data = json.load(file)
                    
            except FileNotFoundError:
                    with open("data.json", "w") as file:
                        json.dump(new_data, file, indent= 4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent= 4)

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


def find_password():

    page= web_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title = "Error", message= "There is no data about that(data.json) ")
    else:   
        if page in data :
            email_search = data[page]["email"]
            password_search = data[page]["password"]
            messagebox.showwarning(title = page, message= f"email : {email_search}\npassword: {password_search}")
        else:
            messagebox.showwarning(title = "Error", message= f"There is no data about that {page} ") 



    
   
window = Tk()
window.title("Password Manager".center(1))
window.geometry("450x400")
window.config(padx= 20, pady= 20)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row= 0) 

website = Label(text="Website")
website.grid(column=0, row=1)


email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row= 3)

web_entry = Entry(width=19)
web_entry.grid(column=1, row=1, sticky="W")
web_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_entry.insert(0, "123@gmail.com")

pass_entry = Entry(width=19)
pass_entry.grid(column=1, row=3, sticky="W")

generate_pass = Button(text="Generate Password", command=generator)
generate_pass.grid(column=1, row=3, sticky="E", columnspan=2)

add_pass = Button(text="Add", width=32, command=save)
add_pass.grid(column=1, row=4, columnspan=2, sticky="W")

search = Button(text= "Search", command=find_password, width= 15)
search.grid(column= 1, row= 1, sticky="E", columnspan=2)





window.mainloop()
