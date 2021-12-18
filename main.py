from tkinter import *
from Screens.main_screen import MainNoteBook

def main() -> None:
    root = Tk()
    tabs = [
            'Vehicle Info',
            'Labor Info',
            'In Progress',
            'Completed',
        ]
    mainWindow = Main(root, "Work Log", '800x600', tabs)

class Main:

    def __init__(self, root, title, geom, tabs) -> None:
        
        self.root = root
        self.root.title(title)
        self.root.geometry(geom)
        
        self.notebook = MainNoteBook(self.root, tabs)
        self.root.mainloop()


if __name__ == "__main__":
    main()
