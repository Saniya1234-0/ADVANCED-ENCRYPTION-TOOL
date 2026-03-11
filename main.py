import customtkinter as ctk
from tkinter import filedialog, messagebox
from logic import VaultEngine # Importing the code we wrote in Step 2

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Advanced AES-256 Vault")
        self.geometry("500x400")
        ctk.set_appearance_mode("dark")

        # UI Components
        self.label = ctk.CTkLabel(self, text="File Encryption Tool", font=("Arial", 22, "bold"))
        self.label.pack(pady=30)

        self.pass_input = ctk.CTkEntry(self, placeholder_text="Secret Password", show="*", width=300)
        self.pass_input.pack(pady=10)

        self.btn_enc = ctk.CTkButton(self, text="Encrypt File", fg_color="green", command=self.run_encrypt)
        self.btn_enc.pack(pady=10)

        self.btn_dec = ctk.CTkButton(self, text="Decrypt File", fg_color="blue", command=self.run_decrypt)
        self.btn_dec.pack(pady=10)

    def run_encrypt(self):
        path = filedialog.askopenfilename()
        pwd = self.pass_input.get()
        if path and pwd:
            VaultEngine(pwd).encrypt(path)
            messagebox.showinfo("Done", "File Encrypted Successfully!")

    def run_decrypt(self):
        path = filedialog.askopenfilename()
        pwd = self.pass_input.get()
        if path and pwd:
            data = VaultEngine(pwd).decrypt(path)
            if data:
                output = path.replace(".enc", "_decrypted")
                with open(output, 'wb') as f:
                    f.write(data)
                messagebox.showinfo("Success", "File Decrypted!")
            else:
                messagebox.showerror("Error", "Invalid Password or File.")

if __name__ == "__main__":
    App().mainloop()