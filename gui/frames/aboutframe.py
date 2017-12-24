from tkinter import Frame
from tkinter.ttk import Label

class AboutFrame(Frame):
    """Frame container for the About screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        label_text = "We were inspired by Microsoft's Contoso University example \n" + \
        "https://docs.microsoft.com/en-us/aspnet/mvc/overview/getting-started/ \n " + \
        "getting-started-with-ef-using-mvc/creating-an-entity-framework-data-model-for-an-asp-net-mvc-application \n" + \
        "THIS IS NOT OUR ORIGINAL IDEA"

        Label(self, text="About Frame").grid(row=0, column=0, sticky="w")
