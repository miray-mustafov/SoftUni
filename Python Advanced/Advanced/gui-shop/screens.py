import tkinter as tk
import json
from PIL import ImageTk, Image
from author_service import login,register
PRODUCTS_FILE_LOCATION='./data_base/products.txt'

def clear_screen(window):
    for child in window.winfo_children():
        child.destroy()

def render_main_screen(window):
    tk.Button(window, bg='green',text='Login',fg='white',
              command=lambda : render_login_screen(window)).grid(row=0,column=0)
    tk.Button(window, bg='yellow',text='Register',fg='black',
              command=lambda : render_regiser_screen(window)).grid(row=0,column=1)



def render_register_screen(window):

    def on_register_click(username, email, password, cpassword):
        username = username.get()
        email = email.get()
        password = password.get()
        cpassword = cpassword.get()

        if cpassword != password:
            tk.Label(window, text='Passwords must match!', fg='red').grid(row=4, column=1)
        else:
            if register(username, email, password):
                render_login_screen(window)
            else:
                tk.Label(window, text='This user exists!', fg='red').grid(row=3, column=1)

        clear_screen(window)

        tk.Label(window, text='username: ').grid(row=0, column=0)
        username = tk.Entry(window)
        username.grid(row=0, column=1)

        tk.Label(window, text='e-mail: ').grid(row=1, column=0)
        email = tk.Entry(window)
        email.grid(row=1, column=1)

        tk.Label(window, text='password: ').grid(row=2, column=0)
        password = tk.Entry(window, show='*')
        password.grid(row=2, column=1)

        tk.Label(window, text='confirm password: ').grid(row=3, column=0)
        confirm_password = tk.Entry(window, show='*')
        confirm_password.grid(row=3, column=1)

        tk.Button(window, bg='green', text='Register', fg='black',
                  command=lambda: on_register_click(username, email, password, confirm_password)) \
            .grid(row=5, column=1)


def render_login_screen(window):

    def on_login_click(username,password):
        username=username.get()
        password = password.get()

        if login(username,password):
            render_products_screen(window)
        else:
            tk.Label(window,text="Invalid credentials!",fg='red').grid(row=2,column=1)

    clear_screen(window)

    tk.Label(window,text='username: ').grid(row=0,column=1)
    username=tk.Entry(window)
    username.grid(row=0,column=1)

    tk.Label(window,text='password: ').grid(row=1,column=0)
    password=tk.Entry(window,show='*')
    password.grid(row=1,column=1)

    tk.Button(window,text='Login',fg='black',bg='green',
              command=lambda : on_login_click(username,password))\
                    .grid(row=3,column=1)


def render_products_screen(window):
    clear_screen(window)
    with open(PRODUCTS_FILE_LOCATION, 'r') as file_prods:
        roww,coll=0,0
        for line in file_prods:
            product_info=json.loads(line.strip())

            if coll%3==0:
                coll=0
                roww+=6
            tk.Label(window,text=product_info['prodType']).grid(row=roww,column=coll)
            tk.Label(window,text=f"id: {product_info['id']}").grid(row=roww+1,column=coll)

            locate_image = Image.open(f"./data_base/images/{product_info['image']}").resize((100, 100))
            img = ImageTk.PhotoImage(locate_image)

            image_label=tk.Label(window,image=img)
            image_label.image=img
            image_label.grid(row=roww+2,column=coll)

            tk.Label(window,text=f"count: {product_info['count']}").grid(row=roww+3,column=coll)
            tk.Label(window,text=f"price: {product_info['price']} BGN",fg='red').grid(row=roww+4,column=coll)
            tk.Button(window,text="BUY",fg='yellow',bg='blue').grid(row=roww+5,column=coll)


            coll+=1
