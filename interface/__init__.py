import tkinter as tk
from tkinter import ttk

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screenWidth}x{self.screenHeight}")
        self.root.title("GeoLine")

        self.topFrame = tk.Frame(self.root, bg="RoyalBlue4", pady=30)
        self.topFrame.pack(fill="x")

        tk.Label(self.topFrame, text="GeoLine", font=("Arial", 35, "bold"), bg="RoyalBlue4", fg="white").pack()
        tk.Label(self.topFrame, text="Sistema de construção e análise de retas", font=("Arial", 14), bg="RoyalBlue4", fg="white").pack()

        self.bottomFrame = tk.Frame(self.root)
        self.bottomFrame.pack(fill="both", expand=True)

        tk.Label(self.bottomFrame, text="Menu principal", font=("Arial", 18, "bold"), foreground="RoyalBlue4").pack(pady=(30, 0))
        ttk.Button(self.bottomFrame, text="Construir reta no R²").pack(pady=(30, 0))
        ttk.Button(self.bottomFrame, text="Construir reta no R³").pack(pady=(30, 0))
        ttk.Button(self.bottomFrame, text="Analisar duas retas").pack(pady=(30, 0))
        ttk.Button(self.bottomFrame, text="Gráficos 2D / 3D", padding=(516, 18)).pack(pady=(30, 0))

        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Arial", 14, "bold"), background="DodgerBlue2", foreground="white", padding=(500, 18))

if __name__ == "__main__":
    interface = Interface();
    interface.root.mainloop();