import tkinter as tk
import importlib

def show_page(page_name):
    # Oculta todas as páginas
    for page in pages.values():
        page.pack_forget()
    
    # Exibe a página selecionada
    pages[page_name].pack()

# Cria a janela principal
root = tk.Tk()
root.title("Menu de Páginas")

# Cria os botões para cada página
page1_btn = tk.Button(root, text="Página 1", command=lambda: show_page("page1"))
page1_btn.pack()

page2_btn = tk.Button(root, text="Página 2", command=lambda: show_page("page2"))
page2_btn.pack()

page3_btn = tk.Button(root, text="Página 3", command=lambda: show_page("page3"))
page3_btn.pack()

# Dicionário para armazenar as páginas
pages = {}

# Carrega o conteúdo das páginas a partir de arquivos Python
for page_name in ["page1", "page2", "page3"]:
    module = importlib.import_module(page_name)
    create_page_func = getattr(module, "create_page")
    page = create_page_func()
    pages[page_name] = page

# Define a página inicial
show_page("page1")

# Inicia o loop principal da aplicação
root.mainloop()
