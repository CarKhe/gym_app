import tkinter as tk


class TopLevel:
    def __init__(self,ventana):
        vetnana_toplevel = tk.Toplevel(ventana)
        vetnana_toplevel.title("Ventana toplevel")
        vetnana_toplevel.geometry("400x200")
