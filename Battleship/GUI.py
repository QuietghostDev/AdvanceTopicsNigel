# v 0.1 Build 001  d 10/2/17
# TODO Add playing grid
# TODO Add Ship/shot placement


from tkinter import *


class Window:
    def __init__(self, master, placeShipCMD):
        self.master = master
        master.title("Battleship")

        self.addShip_button = Button(master, text="Add Ship", command=placeShipCMD)

