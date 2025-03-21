from tkinter import *
import check_in
import check_out
import display_info
import customer_info


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Hotel Management System")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # message displayed
        self.label = Label(top, font=('CASTELLAR', 50, 'bold'), text="WELCOME!!!", fg="#ab56d6", anchor="center")
        self.label.grid(row=0, column=3)

        # check in button
        self.check_in_button = Button(bottom, text="CHECKING IN", font=('arial', 20), bg="#e581eb", relief=RIDGE, height=2,width=50,fg="black", anchor="center",command=check_in.check_in_fun)
        # calling check_in_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # check out button
        self.check_out_button = Button(bottom, text="CHECKING OUT", font=('arial', 20), bg="#e581eb", relief=RIDGE, height=2,width=50, fg="black", anchor="center",command=check_out.check_out_ui)
        # calling check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # show list button
        self.room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=('arial', 20), bg="#e581eb", relief=RIDGE,height=2,width=50, fg="black", anchor="center",command=display_info.display_info_ui)
        # calling display_info_ui function from display_info.py file
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # getting information of all the guests
        self.get_info_button = Button(bottom, text="INFORMATION OF ALL GUESTS", font=('arial', 20), bg="#e581eb",relief=RIDGE,height=2, width=50, fg="black", anchor="center",command=customer_info.customer_info_ui)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('arial', 20), bg="#eb81c0", relief=RIDGE, height=2, width=50,fg="black",anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()
