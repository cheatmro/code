import tkinter as tk

def send_message():
    msg = entry.get().strip()
    if msg:
        chat_text.config(state='normal')
        chat_text.insert(tk.END, "Вы: " + msg + "\n")
        chat_text.config(state='disabled')
        entry.delete(0, tk.END)
        chat_text.see(tk.END)  # прокрутка вниз

root = tk.Tk()
root.title("Простой чат")

chat_text = tk.Text(root, state='disabled', width=50, height=20, wrap='word')
chat_text.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))

send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=(0,10))

root.mainloop()
