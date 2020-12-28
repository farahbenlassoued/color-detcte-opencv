from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import os
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x650+100+50")
        self.logo_icon = ImageTk.PhotoImage(file="images/logo.png")
        self.kbe = ImageTk.PhotoImage(file="images/kbe-tu-logo.png")
        self.entcom = ImageTk.PhotoImage(file="images/entcom.png")
        self.usernameicon = ImageTk.PhotoImage(file="images/icons8-name-64.png")
        self.passwordicon = ImageTk.PhotoImage(file="images/icons8-forgot-password-64.png")
        self.start = ImageTk.PhotoImage(file="images/icons8-play-64.png")
        self.stop = ImageTk.PhotoImage(file="images/stop.png")

        # === na5dmw lbaground remeber to  change it===#
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ===== login form =====#
        self.Frame_login = Frame(self.root, bg="white")
        self.Frame_login.place(x=150, y=150, height=400, width=500)

        title = Label(self.Frame_login, text="Login System", font=("Impact", 25, "bold"), fg="#000066", bg="white").place(
            x=100, y=70)
        desc = Label(self.Frame_login, text=" ", font=("Impact", 16, "bold"), fg="#33ccff", bg="white").place(x=90, y=90)
        logokbe = Label(self.Frame_login, image=self.kbe).place(x=10, y=1, width=70, height=70)
        logoent = Label(self.Frame_login, image=self.entcom).place(x=420, y=0)
        userlogo = Label(self.Frame_login, image=self.usernameicon).place(x=10, y=150, width=50, height=50)
        passlogo = Label(self.Frame_login, image=self.passwordicon).place(x=10, y=230, width=50, height=50)
        # user
        label_user = Label(self.Frame_login, text="Username: ", font=("bold", 15, "bold"), fg="#000000", bg="white").place(
            x=90, y=140)
        self.txt_user = Entry(self.Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)
        # pass
        label_pass = Label(self.Frame_login, text="Password: ", font=("bold", 15, "bold"), fg="#000000", bg="white").place(
            x=90, y=220)
        self.txt_pass = Entry(self.Frame_login, font=("times new roman", 15), show='*', bg="lightgray")
        self.txt_pass.place(x=90, y=250, width=350, height=35)
        # login
        login_btn = Button(self.root, command=self.login_function, text="Login", font=("times new roman", 20),
                           fg="white", bg="#000066").place(
            x=300, y=470, width=200, height=70)

    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get() == "farah" or self.txt_user.get() == "farah":
            messagebox.showinfo("Welcome Admin", "Success Login", parent=self.root)
            self.adminpanel()
        else:
            messagebox.showinfo("Welcome User", "Success Login", parent=self.root)
            self.userpanel()

    def adminpanel(self):
        self.newWindow = Toplevel(self.root)
        self.app = AdminInterface(self.newWindow)
    def userpanel(self):
        self.newWindow = Toplevel(self.root)
        self.app = UserInterface(self.newWindow)

class UserInterface:

    # runing gold script get out results
    def goldcheck(self, val):
        self.stop = Button(self.Frame_login, text="Stop", border=0,
                           font=("times new roman", 10), state=NORMAL,
                           fg="black", bg="red", command=lambda: self.stopgold()).place(
            x=500, y=150, width=70, height=70)
        # try to open the file and set the value of val to its contents

        try:
            with open("result/gold", "r") as f:
                val = f.read()
                with open("result/hsvgold", "r") as f:
                    val2 = f.read()
        except IOError as e:
            print (e)
        else:
            self.colorgold = Label(self.Frame_login, text=val, font=("times new roman", 10),
                                   fg="black", bg="#e6e6e6").place(
                x=200, y=150, width=70, height=70)
            self.hsvgold = Label(self.Frame_login, text=val2, font=("times new roman", 10),
                                 fg="black", bg="#e6e6e6").place(
                x=300, y=150, width=70, height=70)
            self.ent_btn = Button(self.Frame_login, state=DISABLED, text="Etain", font=("times new roman", 10),
                                  fg="black", command=lambda: self.etaincheck(self.val)).place(
                x=100, y=250, width=70, height=70)
            self.gold_btn = Button(self.Frame_login, text="", image=self.ladoinggold, border=0,
                                   font=("times new roman", 10), state=NORMAL,
                                   fg="black", command=lambda: self.goldcheck(self.val)).place(
                x=100, y=150, width=70, height=70)
            if val == "gold":
                self.logoon = Label(self.Frame_login, image=self.on, border=0).place(
                    x=400, y=150)
            else:

                self.logoon = Label(self.Frame_login, image=self.off).place(
                    x=400, y=150)
            exec (open("./gold-color.py").read())
            global golstopx
            golstopx = root.after(2000, lambda: self.goldcheck(val))
    def etaincheck(self, val):
        # try to open the file and set the value of val to its contents
        self.stop = Button(self.Frame_login, text="Stop", border=0,
                           font=("times new roman", 10), state=NORMAL,
                           fg="black", bg="red", command=lambda: self.stoetain()).place(
            x=500, y=250, width=70, height=70)
        try:
            with open("result/etain", "r") as f:
                val = f.read()
                with open("result/hsvetain", "r") as f:
                    val2 = f.read()
        except IOError as e:
            print (e)
        else:
            self.coloretain = Button(self.Frame_login, text=val, font=("times new roman", 10), border=0,
                                fg="black", bg="#e6e6e6").place(
                x=200, y=250, width=70, height=70)
            self.ent_btn = Button(self.Frame_login, state=DISABLED, image=self.ladoinggold, text="Etain", font=("times new roman", 10),
                                  fg="black", command=lambda: self.etaincheck(self.val)).place(
                x=100, y=250, width=70, height=70)
            self.gold_btn = Button(self.Frame_login, text="GOLD", border=0,
                                   font=("times new roman", 10), state=DISABLED,
                                   fg="black", command=lambda: self.goldcheck(self.val)).place(
                x=100, y=150, width=70, height=70)
            self.hsvetain = Label(self.Frame_login,  border=0, text=val2, font=("times new roman", 10),
                                  fg="black", bg="#e6e6e6").place(
                x=300, y=250, width=70, height=70)
            if val == "silver":
                self.logoon = Label(self.Frame_login, image=self.on, border=0).place(
                    x=400, y=150)
            else:

                self.logoon = Label(self.Frame_login, image=self.off, border=0).place(
                    x=400, y=150)
            exec (open("./Silver-color.py").read())
            global etaistopx
            etaistopx = root.after(2000, lambda: self.etaincheck(val))


    def stoetain(self):
        root.after_cancel(etaistopx)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="Etain", font=("times new roman", 10),
                              fg="black", command=lambda: self.etaincheck(self.val)).place(
            x=100, y=250, width=70, height=70)
        self.gold_btn = Button(self.Frame_login, text="GOLD",
                               font=("times new roman", 10), state=NORMAL,
                               fg="black", command=lambda: self.goldcheck(self.val)).place(
            x=100, y=150, width=70, height=70)
        self.stop = Button(self.Frame_login, text="", border=0,
                           font=("times new roman", 10), state=DISABLED,
                            bg="#f2f2f2", command=lambda: self.stoetain()).place(
            x=500, y=250, width=70, height=70)
    def stopgold(self):
        root.after_cancel(golstopx)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="Etain", font=("times new roman", 10),
                              fg="black", command=lambda: self.etaincheck(self.val)).place(
            x=100, y=250, width=70, height=70)
        self.gold_btn = Button(self.Frame_login, text="GOLD",
                               font=("times new roman", 10), state=NORMAL,
                               fg="black", command=lambda: self.goldcheck(self.val)).place(
            x=100, y=150, width=70, height=70)
        self.stop = Button(self.Frame_login, text="", border=0,
                           font=("times new roman", 10), state=DISABLED,
                            bg="#f2f2f2", command=lambda: self.stopgold()).place(
            x=500, y=150, width=70, height=70)
    # runing etain script get out results


    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x650+100+50")
        self.logo_icon = ImageTk.PhotoImage(file="images/logo.png")
        self.kbe = ImageTk.PhotoImage(file="images/kbe-tu-logo.png")
        self.setting = ImageTk.PhotoImage(file="images/settings.png")
        self.on = ImageTk.PhotoImage(file="images/icons8-green-circle-48.png")
        self.off = ImageTk.PhotoImage(file="images/icons8-red-circle-48.png")
        self.start = ImageTk.PhotoImage(file="images/power.png")
        self.stop = ImageTk.PhotoImage(file="images/stop.png")
        self.ladoinggold = ImageTk.PhotoImage(file="images/ezgif-6-f8494d291094.gif")
        # === na5dmw lbaground remeber to  change it===#
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===== login form =====#
        self.Frame_login = Frame(self.root, bg="#f2f2f2")
        self.Frame_login.place(x=150, y=150, height=340, width=800)
        title = Label(self.Frame_login, text="Intelligent Color Detection System", font=("Impact", 25, "bold"),
                      fg="#000066",
                      bg="#f2f2f2").place(
            x=50, y=10)

        # ==================== text in interface admin =================== #
        self.select = Label(self.Frame_login, text="Select", font=("bold", 15, "bold"), fg="black",
                            bg="#f2f2f2").place(
            x=100, y=100)
        self.color = Label(self.Frame_login, text="Color", font=("bold", 15, "bold"), fg="black",
                           bg="#f2f2f2").place(
            x=200, y=100)
        self.HSV = Label(self.Frame_login, text="HSV", font=("bold", 15, "bold"), fg="black",
                         bg="#f2f2f2").place(
            x=300, y=100)
        self.State = Label(self.Frame_login, text="State", font=("bold", 15, "bold"), fg="black",
                           bg="#f2f2f2").place(
            x=400, y=100)

        # ========================= buttons interface admin ================ #
        self.val = StringVar()
        self.colorgold = Label(self.Frame_login, text="", font=("times new roman", 10),
                               fg="white", bg="#f2f2f2").place(
            x=200, y=150, width=70, height=70)
        self.coloretain = Label(self.Frame_login, text="", font=("times new roman", 10),
                                fg="white", bg="#f2f2f2").place(
            x=200, y=250, width=70, height=70)
        self.gold_btn = Button(self.Frame_login, text="GOLD", border=0, font=("times new roman", 10), state=NORMAL,
                               fg="black", bg="#bfbfbf", command=lambda: self.goldcheck(self.val)).place(
            x=100, y=150, width=70, height=70)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="ETAIN", border=0, font=("times new roman", 10),
                              fg="black", bg="#bfbfbf", command=lambda: self.etaincheck(self.val)).place(
            x=100, y=250, width=70, height=70)

class AdminInterface:

    # runing gold script get out results
    def goldcheck(self, val):
        self.stop = Button(self.Frame_login, text="Stop", border=0,
                           font=("times new roman", 10), state=NORMAL,
                           fg="black", bg="red", command=lambda: self.stopgold()).place(
            x=500, y=150, width=70, height=70)
        # try to open the file and set the value of val to its contents

        try:
            with open("result/gold", "r") as f:
                val = f.read()
                with open("result/hsvgold", "r") as f:
                    val2 = f.read()
        except IOError as e:
            print (e)
        else:
            self.colorgold = Label(self.Frame_login, text=val, font=("times new roman", 10),
                                   fg="black", bg="#e6e6e6").place(
                x=200, y=150, width=70, height=70)
            self.hsvgold = Label(self.Frame_login, text=val2, font=("times new roman", 10),
                                 fg="black", bg="#e6e6e6").place(
                x=300, y=150, width=70, height=70)
            self.ent_btn = Button(self.Frame_login, state=DISABLED, text="Etain", font=("times new roman", 10),
                                  fg="black", command=lambda: self.etaincheck(self.val)).place(
                x=100, y=250, width=70, height=70)
            self.gold_btn = Button(self.Frame_login, text="", image=self.ladoinggold, border=0,
                                   font=("times new roman", 10), state=NORMAL,
                                   fg="black", command=lambda: self.goldcheck(self.val)).place(
                x=100, y=150, width=70, height=70)
            if val == "gold":
                self.logoon = Label(self.Frame_login, image=self.on, border=0).place(
                    x=400, y=150)
            else:

                self.logoon = Label(self.Frame_login, image=self.off).place(
                    x=400, y=150)
            exec (open("./gold-color.py").read())
            global golstopx
            golstopx = root.after(2000, lambda: self.goldcheck(val))
    def etaincheck(self, val):
        # try to open the file and set the value of val to its contents
        self.stop = Button(self.Frame_login, text="Stop", border=0,
                           font=("times new roman", 10), state=NORMAL,
                           fg="black", bg="red", command=lambda: self.stoetain()).place(
            x=500, y=250, width=70, height=70)
        try:
            with open("result/etain", "r") as f:
                val = f.read()
                with open("result/hsvetain", "r") as f:
                    val2 = f.read()
        except IOError as e:
            print (e)
        else:
            self.coloretain = Button(self.Frame_login, text=val, font=("times new roman", 10), border=0,
                                fg="black", bg="#e6e6e6").place(
                x=200, y=250, width=70, height=70)
            self.ent_btn = Button(self.Frame_login, state=DISABLED, image=self.ladoinggold, text="Etain", font=("times new roman", 10),
                                  fg="black", command=lambda: self.etaincheck(self.val)).place(
                x=100, y=250, width=70, height=70)
            self.gold_btn = Button(self.Frame_login, text="GOLD", border=0,
                                   font=("times new roman", 10), state=DISABLED,
                                   fg="black", command=lambda: self.goldcheck(self.val)).place(
                x=100, y=150, width=70, height=70)
            self.hsvetain = Label(self.Frame_login,  border=0, text=val2, font=("times new roman", 10),
                                  fg="black", bg="#e6e6e6").place(
                x=300, y=250, width=70, height=70)
            if val == "silver":
                self.logoon = Label(self.Frame_login, image=self.on, border=0).place(
                    x=400, y=150)
            else:

                self.logoon = Label(self.Frame_login, image=self.off, border=0).place(
                    x=400, y=150)
            exec (open("./Silver-color.py").read())
            global etaistopx
            etaistopx = root.after(2000, lambda: self.etaincheck(val))


    def stoetain(self):
        root.after_cancel(etaistopx)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="Etain", font=("times new roman", 10),
                              fg="black", command=lambda: self.etaincheck(self.val)).place(
            x=100, y=250, width=70, height=70)
        self.gold_btn = Button(self.Frame_login, text="GOLD",
                               font=("times new roman", 10), state=NORMAL,
                               fg="black", command=lambda: self.goldcheck(self.val)).place(
            x=100, y=150, width=70, height=70)
        self.stop = Button(self.Frame_login, text="", border=0,
                           font=("times new roman", 10), state=DISABLED,
                            bg="#f2f2f2", command=lambda: self.stoetain()).place(
            x=500, y=250, width=70, height=70)
    def stopgold(self):
        root.after_cancel(golstopx)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="Etain", font=("times new roman", 10),
                              fg="black", command=lambda: self.etaincheck(self.val)).place(
            x=100, y=250, width=70, height=70)
        self.gold_btn = Button(self.Frame_login, text="GOLD",
                               font=("times new roman", 10), state=NORMAL,
                               fg="black", command=lambda: self.goldcheck(self.val)).place(
            x=100, y=150, width=70, height=70)
        self.stop = Button(self.Frame_login, text="", border=0,
                           font=("times new roman", 10), state=DISABLED,
                            bg="#f2f2f2", command=lambda: self.stopgold()).place(
            x=500, y=150, width=70, height=70)
    # runing etain script get out results


    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x650+100+50")
        self.logo_icon = ImageTk.PhotoImage(file="images/logo.png")
        self.kbe = ImageTk.PhotoImage(file="images/kbe-tu-logo.png")
        self.setting = ImageTk.PhotoImage(file="images/settings.png")
        self.on = ImageTk.PhotoImage(file="images/icons8-green-circle-48.png")
        self.off = ImageTk.PhotoImage(file="images/icons8-red-circle-48.png")
        self.start = ImageTk.PhotoImage(file="images/power.png")
        self.stop = ImageTk.PhotoImage(file="images/stop.png")
        self.ladoinggold = ImageTk.PhotoImage(file="images/ezgif-6-f8494d291094.gif")
        # === na5dmw lbaground remeber to  change it===#
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===== login form =====#
        self.Frame_login = Frame(self.root, bg="#f2f2f2")
        self.Frame_login.place(x=150, y=150, height=340, width=800)
        title = Label(self.Frame_login, text="Intelligent Color Detection System", font=("Impact", 25, "bold"),
                      fg="#000066",
                      bg="#f2f2f2").place(
            x=50, y=10)

        # ==================== text in interface admin =================== #
        self.select = Label(self.Frame_login, text="Select", font=("bold", 15, "bold"), fg="black",
                            bg="#f2f2f2").place(
            x=100, y=100)
        self.color = Label(self.Frame_login, text="Color", font=("bold", 15, "bold"), fg="black",
                           bg="#f2f2f2").place(
            x=200, y=100)
        self.HSV = Label(self.Frame_login, text="HSV", font=("bold", 15, "bold"), fg="black",
                         bg="#f2f2f2").place(
            x=300, y=100)
        self.State = Label(self.Frame_login, text="State", font=("bold", 15, "bold"), fg="black",
                           bg="#f2f2f2").place(
            x=400, y=100)

        # ========================= buttons interface admin ================ #
        self.val = StringVar()
        self.colorgold = Label(self.Frame_login, text="", font=("times new roman", 10),
                               fg="white", bg="#f2f2f2").place(
            x=200, y=150, width=70, height=70)
        self.coloretain = Label(self.Frame_login, text="", font=("times new roman", 10),
                                fg="white", bg="#f2f2f2").place(
            x=200, y=250, width=70, height=70)
        self.gold_btn = Button(self.Frame_login, text="GOLD", border=0, font=("times new roman", 10), state=NORMAL,
                               fg="black", bg="#bfbfbf", command=lambda: self.goldcheck(self.val)).place(
            x=100, y=150, width=70, height=70)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="ETAIN", border=0, font=("times new roman", 10),
                              fg="black", bg="#bfbfbf", command=lambda: self.etaincheck(self.val)).place(
            x=100, y=250, width=70, height=70)
        self.btnsetting = Button(self.Frame_login, state=NORMAL, image=self.setting, command=lambda: self.settingx(),
                                 border=0,
                                 font=("times new roman", 10),
                                 ).place(
            x=680, y=250)

        # ====================================================================#
    def settingx(self):
        self.newWindow = Toplevel(self.root)
        self.app = Setting(self.newWindow)
class Setting:
    def savex(self):
        val = self.entryText.get()
        val2 = self.entryText1.get()
        val3 = self.entryText2.get()
        val4 = self.entryText3.get()
        open("result/goldhsvmin", "w").write(val)
        open("result/hsvetainmin", "w").write(val2)
        open("result/hsvetainmax", "w").write(val4)
        open("result/goldhsvmax", "w").write(val3)
    def __init__(self, root):
        self.root = root
        self.root.title("Setting dashboard")
        self.root.geometry("1199x650+100+50")
        self.logo_icon = ImageTk.PhotoImage(file="images/logo.png")
        self.kbe = ImageTk.PhotoImage(file="images/kbe-tu-logo.png")
        self.setting = ImageTk.PhotoImage(file="images/settings.png")
        self.on = ImageTk.PhotoImage(file="images/icons8-green-circle-48.png")
        self.off = ImageTk.PhotoImage(file="images/icons8-red-circle-48.png")
        self.start = ImageTk.PhotoImage(file="images/power.png")
        self.stop = ImageTk.PhotoImage(file="images/stop.png")
        self.ladoinggold = ImageTk.PhotoImage(file="images/ezgif-6-f8494d291094.gif")
        self.save = ImageTk.PhotoImage(file="images/save.png")
        # === na5dmw lbaground remeber to  change it===#
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===== login form =====#
        self.Frame_login = Frame(self.root, bg="#f2f2f2")
        self.Frame_login.place(x=150, y=150, height=340, width=800)
        title = Label(self.Frame_login, text="Intelligent Color Detection System", font=("Impact", 25, "bold"),
                      fg="#000066",
                      bg="#f2f2f2").place(
            x=50, y=10)
        # ==================== text in interface admin =================== #
        self.select = Label(self.Frame_login, text="Select", font=("bold", 15, "bold"), fg="black",
                            bg="#f2f2f2").place(
            x=100, y=100)
        self.color = Label(self.Frame_login, text="Min", font=("bold", 15, "bold"), fg="black",
                           bg="#f2f2f2").place(
            x=250, y=100)
        self.HSV = Label(self.Frame_login, text="MAX", font=("bold", 15, "bold"), fg="black",
                         bg="#f2f2f2").place(
            x=400, y=100)
        ################################ read old values #####################
        try:
            with open("result/goldhsvmin", "r") as f:
                self.val = f.read()
                with open("result/goldhsvmax", "r") as f:
                    self.val2 = f.read()
                    with open("result/hsvetainmin", "r") as f:
                        self.val3 = f.read()
                        with open("result/hsvetainmax", "r") as f:
                            self.val4 = f.read()
        except IOError as e:
            print (e)
        # ========================= buttons interface admin ================ #
        self.gold_btn = Button(self.Frame_login, text="GOLD", border=0, font=("times new roman", 10), state=NORMAL,
                               fg="black", bg="#bfbfbf").place(
            x=100, y=150, width=70, height=70)
        self.ent_btn = Button(self.Frame_login, state=NORMAL, text="ETAIN", border=0, font=("times new roman", 10),
                              fg="black", bg="#bfbfbf").place(
            x=100, y=250, width=70, height=70)
        self.entryText = StringVar()
        self.entryText.set(self.val)
        self.mingold = Entry(self.Frame_login,border=2, font=("bold", 15), textvariable=self.entryText,
                               fg="black", bg="#f2f2f2",justify='center').place(
            x=210, y=150, width=150, height=70)
        self.entryText1 = StringVar()
        self.entryText1.set(self.val3)
        self.minetain = Entry(self.Frame_login,border=2, font=("bold", 15),textvariable=self.entryText1,
                         fg="black", bg="#f2f2f2",justify='center').place(
            x=210, y=250, width=150, height=70)
        self.entryText2 = StringVar()
        self.entryText2.set(self.val2)
        self.maxgold = Entry(self.Frame_login, border=2,font=("bold", 15),textvariable=self.entryText2,
                              fg="black", bg="#f2f2f2",justify='center').place(
            x=365, y=150, width=150, height=70)
        self.entryText3 = StringVar()
        self.entryText3.set(self.val4)
        self.maxetain = Entry(self.Frame_login,border=2, font=("bold", 15),textvariable=self.entryText3,
                              fg="black", bg="#f2f2f2",justify='center').place(
            x=365, y=250, width=150, height=70)
        self.savegold = Button(self.Frame_login, font=("bold", 15),text="Save", command=lambda: self.savex(),
                              fg="black", bg="#e6e6e6",border=2).place(
            x=600, y=200, width=70, height=70)


root = Tk()
obj = Login(root)
root.mainloop()

