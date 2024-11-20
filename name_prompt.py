import tkinter as tk

class NamePrompt:
    """
    Sanya Gupta
    CMSY 257
    GUI used for the Name Prompt
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Enter Your Name")
        
        self.label = tk.Label(self.root, text="Enter your name:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.name_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_name)
        self.submit_button.pack(pady=10)

        self.name = None

    def submit_name(self):
        self.name = self.name_entry.get().strip()
        if self.name:  # Ensure a name is entered
            self.root.quit()  # Stop mainloop after name is entered

    def get_name(self):
        return self.name