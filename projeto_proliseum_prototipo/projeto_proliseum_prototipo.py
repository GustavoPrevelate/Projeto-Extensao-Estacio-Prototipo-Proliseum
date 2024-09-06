################################################# IMPORTANTE!!! #################################################

# Só deixando um aviso rápido que essa plataforma foi construída para ser um protótipo do projeto PROLISEUM,
# Para realizar alguns testes na plataforma e verificar na prática qual é a proposta do projeto PROLISEUM.

##################################################################################################################


# Aqui são alguns imports realizado para poder trabalhar com calendários (formulários de data), trabalhar com manipulação de imaagens,
# Realizar conexão com o banco de dados e mais algumas funções do tkinter.
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import psycopg2


# App é a minha classe principal, onde eu montei as funções como ponto de referencia para as telas da aplicação,
# fora isso também estou definindo o tamanho da tela, o titulo da aplicação e definindo o usuario_logado_id como none
# para futuramente salvar o ID do usuario.
class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Proliseum Protótipo")
        self.root.iconphoto(False, tk.PhotoImage(file="icone_do_projeto.png"))
        
        self.current_frame = None
        self.usuario_logado_id = None  
        self.mostrar_tela_home()  

    def mostrar_tela_home(self):
        self.mudar_tela(TelaHome(self.root, self))

    def mostrar_tela_login(self):
        self.mudar_tela(TelaLogin(self.root, self))

    def mostrar_tela_dashboard(self):
        self.mudar_tela(TelaDashboard(self.root, self))

    def mostrar_tela_cadastro(self):
        self.mudar_tela(TelaCadastro(self.root, self))

    def mostrar_tela_perfil(self):
        self.mudar_tela(TelaPerfil(self.root, self))
    
    def mostrar_tela_editar_perfil(self):
        self.mudar_tela(TelaEditarPerfil(self.root, self))
        
    def mostrar_tela_lista_jogadores(self):
        self.mudar_tela(TelaListaJogadores(self.root, self))
        
    def mostrar_tela_criar_jogador(self):
        self.mudar_tela(TelaCriarJogador(self.root, self))
        
    def mostrar_tela_lista_times(self):
        self.mudar_tela(TelaListaTimes(self.root, self))
        
    def mostrar_tela_criar_time(self):
        self.mudar_tela(TelaCriarTime(self.root, self))
        
    def mostrar_tela_busca_jogadores(self):
        self.mudar_tela(TelaBuscaJogadores(self.root, self))

    def mostrar_tela_peneira(self):
        self.mudar_tela(TelaPeneira(self.root, self))

    def mostrar_tela_campeonatos(self):
        self.mudar_tela(TelaCampeonatos(self.root, self))
        
        
# Aqui é uma função para mudar de tela
    def mudar_tela(self, tela):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = tela
        self.current_frame.pack(fill="both", expand=True)

# Aqui é a onde eu faço a conexão com o meu banco de dados.
    def conectar_db(self):
        try:
            conn = psycopg2.connect(
                dbname="db_projeto_extensao_estacio_gustavo_prevelate",
                user="postgres",
                password="sgbdpsqlgp",
                host="localhost",
                port="5432",
                options="-c client_encoding=utf8"
            )
            print("Conectado ao banco de dados com sucesso!")
            return conn
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
        
# Essa classe é a que determina qual tela será exibida quando o usuário clicar em um dos botões no menu lateral
class MenuLateral:
    def __init__(self, parent, app):
        
        self.parent = parent
        self.app = app
        self.menu_lateral = tk.Frame(self.parent, bg="#191828", width=800, height=1080)
        self.menu_lateral.pack(side="left", fill="y")

        botoes_menu = ["Meu perfil", "Lista de jogadores", "Lista de times", "Busca por jogadores", "Peneira", "Campeonatos", "Sair da plataforma"]
        for i, botao_nome in enumerate(botoes_menu):
            if i == 6: 
                spacer = tk.Frame(self.menu_lateral, height=400, bg="#191828")
                spacer.pack()

            # Aqui verifica o nome do botão para associar a função/Tela correta
            if botao_nome == "Meu perfil":
                comando = self.app.mostrar_tela_perfil
            elif botao_nome == "Lista de jogadores":
                comando = self.app.mostrar_tela_lista_jogadores
            elif botao_nome == "Lista de times":
                comando = self.app.mostrar_tela_lista_times 
            elif botao_nome == "Busca por jogadores":
                comando = self.app.mostrar_tela_busca_jogadores  
            elif botao_nome == "Peneira":
                comando = self.app.mostrar_tela_peneira  
            elif botao_nome == "Campeonatos":
                comando = self.app.mostrar_tela_campeonatos  
            elif botao_nome == "Sair da plataforma":
                comando = self.app.root.destroy  
            else:
                comando = None

            botao = tk.Button(self.menu_lateral, text=botao_nome, font=("Arial", 16), bg="red", fg="white", command=comando)
            botao.pack(pady=20, padx=10, fill="x")


# Aqui é a tela Home, a tela principal onde o usuário vai navegar pela plataforma.
class TelaHome(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        try:
            self.bg_image = Image.open("background_proliseum_.png")
            self.bg_image = self.bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            print("Imagem de fundo carregada com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar a imagem de fundo: {e}")
            self.bg_photo = None

        self.canvas = tk.Canvas(self, width=1920, height=1080, bg="#1F1E31")
        self.canvas.pack(fill="both", expand=True)

        if self.bg_photo:
            self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.canvas.create_text(492, 442, text="PROLISEUM", font=("Arial", 56, "bold"), fill="red")
        self.canvas.create_text(490, 440, text="PROLISEUM", font=("Arial", 56, "bold"), fill="white")

        self.canvas.create_text(540, 540, text="A melhor plataforma para encontrar seu time dos sonhos", font=("Arial", 16, "bold"), fill="white")

        login_button = tk.Button(self, text="LOGIN", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.app.mostrar_tela_login)
        login_button.place(x=1690, y=100, width=150, height=60)

        pro_button = tk.Button(self, text="TORNE-SE UM PRO", font=("Arial", 16), bg="red", fg="white", command=self.app.mostrar_tela_cadastro)
        pro_button.place(x=1210, y=720, width=280, height=60)


# Aqui é onde fica a tela de Cadastro, juntamente com o formulário para o usuário se cadastrar na plataforma.
class TelaCadastro(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        
        try:
            self.img_perfil = Image.open("img_perfil_de_usuario.png")
            self.img_perfil = self.img_perfil.resize((300, 300), Image.Resampling.LANCZOS)
            self.img_perfil_photo = ImageTk.PhotoImage(self.img_perfil)
        except Exception as e:
            print(f"Erro ao carregar a imagem de perfil: {e}")
            self.img_perfil_photo = None

        self.right_canvas = tk.Canvas(self, width=960, height=1080, bg="#1F1E31")
        self.right_canvas.place(x=960, y=0)

        if self.img_perfil_photo:
            self.right_canvas.create_image(330, 50, anchor="nw", image=self.img_perfil_photo)

        tk.Label(self.right_canvas, text="Biografia:", font=("Arial", 16, "bold"), bg="#1F1E31", fg="white").place(x=150, y=400)
        self.text_biografia = tk.Text(self.right_canvas, width=60, height=15, font=("Arial", 14))
        self.text_biografia.place(x=150, y=440, height=400)

        self.left_canvas = tk.Canvas(self, width=960, height=1080, bg="#1F1E31", highlightthickness=0)
        self.left_canvas.place(x=0, y=0)
        self.left_canvas.create_text(472, 122, text="CADASTRO", font=("Arial", 48, "bold"), fill="red")
        self.left_canvas.create_text(470, 120, text="CADASTRO", font=("Arial", 48, "bold"), fill="white")

        campos = ["Nome de Usuário:", "Nome Completo:", "Email:", "Senha:", "Confirmar Senha:", "Gênero:"]
        self.entries = {}

        y_position = 300
        for campo in campos:
            tk.Label(self, text=campo, font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=300, y=y_position)
            entry = tk.Entry(self, width=40, font=("Arial", 16))
            entry.place(x=300, y=y_position + 40, width=400, height=40)
            self.entries[campo] = entry
            y_position += 100

        self.entries["Senha:"].config(show="*")
        self.entries["Confirmar Senha:"].config(show="*")

        tk.Label(self, text="Data de Nascimento:", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=300, y=200)
        self.date_nascimento = DateEntry(self, width=40, font=("Arial", 16), date_pattern='y-mm-dd', background="darkblue", foreground="white", borderwidth=2)
        self.date_nascimento.place(x=300, y=200 + 40, width=400, height=40)

        y_position += 100

        self.cadastrar_button = tk.Button(self, text="CADASTRAR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.cadastrar_usuario)
        self.cadastrar_button.place(x=550, y=900, width=150, height=60)

        self.voltar_button = tk.Button(self, text="VOLTAR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.app.mostrar_tela_home)
        self.voltar_button.place(x=300, y=900, width=150, height=60)

    def cadastrar_usuario(self):
        nome_usuario = self.entries["Nome de Usuário:"].get()
        email = self.entries["Email:"].get()
        senha = self.entries["Senha:"].get()
        confirmar_senha = self.entries["Confirmar Senha:"].get()
        nome_completo = self.entries["Nome Completo:"].get()
        genero = self.entries["Gênero:"].get()
        biografia = self.text_biografia.get("1.0", tk.END).strip()
        data_nascimento = self.date_nascimento.get()

        if senha != confirmar_senha:
            self.show_error("As senhas não coincidem!")
            return

        conn = self.app.conectar_db()
        
        # Aqui é a onde eu utilizo uma Query para cadastrar o usuário na tbl_usuario com base nos parametros fornecidos pelo mesmo.
        if conn:
            try:
                cur = conn.cursor()
                query = """
                    INSERT INTO tbl_usuario (nome_completo, nome_de_usuario, senha, biografia, genero, data_de_nascimento)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING id_de_usuario;
                """
                cur.execute(query, (nome_completo, nome_usuario, senha, biografia, genero, data_nascimento))
                id_de_usuario = cur.fetchone()[0]

                query_email = """
                    INSERT INTO tbl_email (email, id_de_usuario)
                    VALUES (%s, %s);
                """
                cur.execute(query_email, (email, id_de_usuario))

                conn.commit()
                self.show_message("Usuário cadastrado com sucesso!")
                self.app.mostrar_tela_login()
            except Exception as e:
                conn.rollback()
                self.show_error(f"Erro ao cadastrar o usuário: {e}")
            finally:
                cur.close()
                conn.close()

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Erro")
        tk.Label(error_window, text=message, font=("Arial", 16, "bold"), fg="red").pack(padx=20, pady=20)

    def show_message(self, message):
        message_window = tk.Toplevel(self)
        message_window.title("Sucesso")
        tk.Label(message_window, text=message, font=("Arial", 16, "bold"), fg="green").pack(padx=20, pady=20)

# Aqui é a tela de Login, caso o usuário ja esteja cadastrado na plataforma, ele poderá logar sem problemas! Ou voltar para tela Home
# Para ir para tela cadastro e efetuar seu cadastro na plataforma.
class TelaLogin(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
    
        self.left_canvas = tk.Canvas(self, width=960, height=1080, bg="#1F1E31", highlightthickness=0)
        self.left_canvas.place(x=0, y=0)
        
        try:
            self.icon_proliseum = Image.open("icon_proliseum.png")
            self.icon_proliseum = self.icon_proliseum.resize((200, 200), Image.Resampling.LANCZOS)
            self.icon_proliseum_photo = ImageTk.PhotoImage(self.icon_proliseum)
        except Exception as e:
            print(f"Erro ao carregar o ícone: {e}")
            self.icon_proliseum_photo = None

        if self.icon_proliseum_photo:
            self.left_canvas.create_image(50, 50, anchor="nw", image=self.icon_proliseum_photo)

        self.left_canvas.create_text(502, 322, text="LOGIN", font=("Arial", 48, "bold"), fill="red")
        self.left_canvas.create_text(500, 320, text="LOGIN", font=("Arial", 48, "bold"), fill="white")

        tk.Label(self, text="Nome de Usuário:", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=300, y=400)
        self.entry_usuario = tk.Entry(self, width=40, font=("Arial", 16))
        self.entry_usuario.place(x=300, y=440, width=400, height=50)

        tk.Label(self, text="Senha:", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=300, y=520)
        self.entry_senha = tk.Entry(self, show="*", width=40, font=("Arial", 16))
        self.entry_senha.place(x=300, y=560, width=400, height=50)

        self.login_button = tk.Button(self, text="LOGIN", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.verificar_login)
        self.login_button.place(x=550, y=640, width=150, height=60)

        self.voltar_button = tk.Button(self, text="VOLTAR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.app.mostrar_tela_home)
        self.voltar_button.place(x=300, y=640, width=150, height=60)

        try:
            self.img_login = Image.open("img_login.png")
            self.img_login = self.img_login.resize((960, 1080), Image.Resampling.LANCZOS)
            self.img_login_photo = ImageTk.PhotoImage(self.img_login)
        except Exception as e:
            print(f"Erro ao carregar a imagem de login: {e}")
            self.img_login_photo = None

        self.right_canvas = tk.Canvas(self, width=960, height=1080, bg="#1F1E31")
        self.right_canvas.place(x=960, y=0)
        if self.img_login_photo:
            self.right_canvas.create_image(0, 0, anchor="nw", image=self.img_login_photo)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        conn = self.app.conectar_db()
        
        # Realizando uma Query para selecionar algumas informações do usuário e verificar se existe no banco de dados ou não.
        if conn:
            try:
                cur = conn.cursor()
                query = "SELECT id_de_usuario FROM tbl_usuario WHERE nome_de_usuario=%s AND senha=%s"
                cur.execute(query, (usuario, senha))
                result = cur.fetchone()

                if result:
                    id_usuario = result[0]  
                    self.app.usuario_logado_id = id_usuario  
                    self.app.mostrar_tela_dashboard()
                else:
                    self.show_error("Usuário ou senha incorretos!")
            except Exception as e:
                self.show_error(f"Erro ao verificar o login: {e}")
            finally:
                cur.close()
                conn.close()

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Erro")
        tk.Label(error_window, text=message, font=("Arial", 16, "bold"), fg="red").pack(padx=20, pady=20)

# Aqui é a tela Dashboard, é a tela principal após o usuário conseguir logar na plataforma com sucesso.
class TelaDashboard(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        MenuLateral(self, self.app)

        tela_direita = tk.Frame(self, bg="#1F1E31")
        tela_direita.pack(side="right", fill="both", expand=True)

        # Parte superior (Imagem)
        parte_superior = tk.Frame(tela_direita, bg="#1F1E31", height=400)
        parte_superior.pack(fill="x")

        try:
            self.img_tela_main = Image.open("img_tela_main.png")
            self.img_tela_main = self.img_tela_main.resize((1920, 400), Image.Resampling.LANCZOS)
            self.img_tela_main_photo = ImageTk.PhotoImage(self.img_tela_main)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.img_tela_main_photo = None

        canvas_superior = tk.Canvas(parte_superior, width=1120, height=400, bg="#1F1E31")
        canvas_superior.pack(fill="both", expand=True)
        if self.img_tela_main_photo:
            canvas_superior.create_image(0, 0, anchor="nw", image=self.img_tela_main_photo)

        parte_inferior = tk.Frame(tela_direita, bg="#1F1E31", height=680)
        parte_inferior.pack(fill="both", expand=True)

        canvas_inferior = tk.Canvas(parte_inferior, bg="#1F1E31", width=1120, height=680)
        canvas_inferior.pack(fill="both", expand=True)
        canvas_inferior.create_text(860, 100, text="PROLISEUM", font=("Arial", 56, "bold"), fill="red")
        canvas_inferior.create_text(858, 98, text="PROLISEUM", font=("Arial", 56, "bold"), fill="white")

        canvas_inferior.create_text(860, 200, text="Mais funcionalidades no futuro...", font=("Arial", 20, "italic"), fill="white")


# Aqui é a tela de Perfil do usuário, onde ele poderá ver seu perfil com algumas informações.
class TelaPerfil(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.app.usuario_logado_id
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        MenuLateral(self, self.app)

        parte_superior = tk.Frame(self, bg="#1F1E31", height=400)
        parte_superior.pack(fill="x")

        try:
            self.img_capa_usuario = Image.open("background_usuario_teste.png").resize((1920, 400), Image.Resampling.LANCZOS)
            self.img_capa_usuario_photo = ImageTk.PhotoImage(self.img_capa_usuario)
        except Exception as e:
            print(f"Erro ao carregar a imagem de capa: {e}")
            self.img_capa_usuario_photo = None

        canvas_capa = tk.Canvas(parte_superior, width=1120, height=400, bg="#1F1E31", highlightthickness=0)
        canvas_capa.pack(fill="both", expand=True)

        if self.img_capa_usuario_photo:
            canvas_capa.create_image(0, 0, anchor="nw", image=self.img_capa_usuario_photo)

        conn = self.app.conectar_db()
        
        # Mais uma Query para puxar as informações do usuário e mostrar na tela de perfil.
        if conn:
            try:
                cur = conn.cursor()
                query = """
                    SELECT nome_de_usuario
                    FROM tbl_usuario
                    WHERE id_de_usuario = %s
                """
                cur.execute(query, (self.app.usuario_logado_id,))  # Usando o ID do usuário logado
                result = cur.fetchone()

                if result:
                    nome_usuario = result[0]
                else:
                    nome_usuario = "Nome não encontrado"

            except Exception as e:
                print(f"Erro ao buscar dados do usuário: {e}")
                nome_usuario = "Erro ao carregar nome"
            finally:
                cur.close()
                conn.close()

        try:
            self.img_usuario = Image.open("imagem_padrao_usuario.png").resize((300, 300), Image.Resampling.LANCZOS)

            borda = 10 
            img_com_borda = Image.new("RGB", (300 + 2 * borda, 300 + 2 * borda), "white") 
            img_com_borda.paste(self.img_usuario, (borda, borda))

            self.img_usuario_photo = ImageTk.PhotoImage(img_com_borda)
        except Exception as e:
            print(f"Erro ao carregar a imagem de usuário: {e}")
            self.img_usuario_photo = None

        if self.img_usuario_photo:
            
            canvas_usuario = tk.Canvas(self, width=320, height=320, bg="#1F1E31", highlightthickness=0)
            canvas_usuario.create_image(0, 0, anchor="nw", image=self.img_usuario_photo)
            canvas_usuario.place(x=300, y=250)

        tk.Label(self, text=nome_usuario, font=("Arial", 24, "bold"), fg="white", bg="#1F1E31").place(x=290, y=600)

        tk.Label(self, text="Informações de jogador adicionadas na versão final", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=290, y=680)

        tk.Label(self, text="Redes sociais na versão final", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=650, y=420)

        editar_button = tk.Button(self, text="EDITAR PERFIL", font=("Arial", 14, "bold"), bg="red", fg="white",
                                  command=self.app.mostrar_tela_editar_perfil)  
        editar_button.place(x=1500, y=450, width=150, height=40)

# Aqui é a tela onde o usuário pode editar o perfil dele, algumas informações já são retornadas como referência para o usuário editar
# eu só não retornei a senha dele por questão de segurança, deixando o usuário criar e confirmar a nova senha.
class TelaEditarPerfil(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.user_id = self.app.usuario_logado_id
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
    
        self.canvas_title = tk.Canvas(self, width=1920, height=100, bg="#1F1E31", highlightthickness=0)
        self.canvas_title.pack()

        self.canvas_title.create_text(362, 52, text="EDITAR PERFIL", font=("Arial", 48, "bold"), fill="red")
        self.canvas_title.create_text(360, 50, text="EDITAR PERFIL", font=("Arial", 48, "bold"), fill="white")

        form_frame = tk.Frame(self, bg="#1F1E31")
        form_frame.place(x=100, y=120, width=800, height=500)

        campos = ["Nome de Usuário:", "Email:", "Nova Senha:", "Confirmar Nova Senha:", "Nome Completo:", "Gênero:"]
        self.entries = {}

        y_position = 20
        for i, campo in enumerate(campos):
            tk.Label(form_frame, text=campo, font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=20 if i % 2 == 0 else 420, y=y_position)
            entry = tk.Entry(form_frame, width=30, font=("Arial", 14))
            entry.place(x=20 if i % 2 == 0 else 420, y=y_position + 30, width=350, height=60)
            self.entries[campo] = entry
            if i % 2 != 0:
                y_position += 100

        self.entries["Nova Senha:"].config(show="*")
        self.entries["Confirmar Nova Senha:"].config(show="*")

        tk.Label(form_frame, text="Data de Nascimento:", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=20, y=y_position)
        self.date_nascimento = DateEntry(form_frame, width=30, font=("Arial", 14), date_pattern='y-mm-dd', background="darkblue", foreground="white", borderwidth=2)
        self.date_nascimento.place(x=20, y=y_position + 30, width=350, height=60)


        tk.Label(self, text="FOTO:", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=950, y=120)

        try:
            self.img_perfil = Image.open("imagem_padrao_usuario.png").resize((300, 300), Image.Resampling.LANCZOS)
            self.img_perfil_photo = ImageTk.PhotoImage(self.img_perfil)
        except Exception as e:
            print(f"Erro ao carregar a imagem de perfil: {e}")
            self.img_perfil_photo = None

        if self.img_perfil_photo:
            canvas = tk.Canvas(self, width=300, height=300, bg="#1F1E31", highlightthickness=0)
            canvas.create_image(0, 0, anchor="nw", image=self.img_perfil_photo)
            canvas.place(x=950, y=160)

        tk.Label(self, text="BIO:", font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=950, y=480)
        self.text_biografia = tk.Text(self, width=60, height=10, font=("Arial", 14))
        self.text_biografia.place(x=950, y=520)

        voltar_button = tk.Button(self, text="VOLTAR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.app.mostrar_tela_perfil)
        voltar_button.place(x=950, y=760, width=200, height=50)

        salvar_button = tk.Button(self, text="SALVAR ALTERAÇÕES", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.salvar_alteracoes)
        salvar_button.place(x=1365, y=760, width=250, height=50)

        self.carregar_dados_atuais()

# A função é auto explicativa, mas aqui é onde eu criei uma função para mostrar alguns dados do usuário para ele ter referência para poder editar.
    def carregar_dados_atuais(self):
        conn = self.app.conectar_db()
        if conn and self.user_id is not None:
            try:
                cur = conn.cursor()

                query_usuario = """
                    SELECT nome_de_usuario, nome_completo, genero, biografia, data_de_nascimento
                    FROM tbl_usuario
                    WHERE id_de_usuario = %s
                """
                cur.execute(query_usuario, (self.user_id,))
                result_usuario = cur.fetchone()

                if result_usuario:
                    self.entries["Nome de Usuário:"].insert(0, result_usuario[0])
                    self.entries["Nome Completo:"].insert(0, result_usuario[1])
                    self.entries["Gênero:"].insert(0, result_usuario[2])
                    self.text_biografia.insert(tk.END, result_usuario[3])
                    self.date_nascimento.set_date(result_usuario[4])
                else:
                    print("Usuário não encontrado.")

                query_email = """
                    SELECT email
                    FROM tbl_email
                    WHERE id_de_usuario = %s
                """
                cur.execute(query_email, (self.user_id,))
                result_email = cur.fetchone()

                if result_email:
                    self.entries["Email:"].insert(0, result_email[0])
                else:
                    print("Email não encontrado.")
                    
            except Exception as e:
                print(f"Erro ao carregar dados do usuário: {e}")
            finally:
                cur.close()
                conn.close()

# Aqui é a função para salvar as alterações que o usuário fez e também validar se a senha que ele colocou é igual a senha do campo confirmar senha.
    def salvar_alteracoes(self):
        nome_usuario = self.entries["Nome de Usuário:"].get()
        email = self.entries["Email:"].get()
        nova_senha = self.entries["Nova Senha:"].get()
        confirmar_senha = self.entries["Confirmar Nova Senha:"].get()
        nome_completo = self.entries["Nome Completo:"].get()
        genero = self.entries["Gênero:"].get()
        biografia = self.text_biografia.get("1.0", tk.END).strip()
        data_nascimento = self.date_nascimento.get()

        if nova_senha and nova_senha != confirmar_senha:
            self.show_error("As senhas não coincidem!")
            return

        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()

                query_usuario = """
                    UPDATE tbl_usuario
                    SET nome_de_usuario = %s, nome_completo = %s, genero = %s, biografia = %s, data_de_nascimento = %s
                    WHERE id_de_usuario = %s
                """
                cur.execute(query_usuario, (nome_usuario, nome_completo, genero, biografia, data_nascimento, self.user_id))

                query_email = """
                    UPDATE tbl_email
                    SET email = %s
                    WHERE id_de_usuario = %s
                """
                cur.execute(query_email, (email, self.user_id))  

                if nova_senha:
                    query_senha = """
                        UPDATE tbl_usuario
                        SET senha = %s
                        WHERE id_de_usuario = %s
                    """
                    cur.execute(query_senha, (nova_senha, self.user_id))

                conn.commit()

                print("Perfil atualizado com sucesso!")
                self.show_message("Perfil atualizado com sucesso!")
            except Exception as e:
                conn.rollback()
                print(f"Erro ao atualizar perfil: {e}")
            finally:
                cur.close()
                conn.close()

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Erro")
        tk.Label(error_window, text=message, font=("Arial", 16, "bold"), fg="red").pack(padx=20, pady=20)

    def show_message(self, message):
        message_window = tk.Toplevel(self)
        message_window.title("Sucesso")
        tk.Label(message_window, text=message, font=("Arial", 16, "bold"), fg="green").pack(padx=20, pady=20)
        
        
# Aqui é a tela onde vai mostrar a lista dos jogadores da plataforma
class TelaListaJogadores(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        MenuLateral(self, self.app)

        try:
            self.img_jogadores = Image.open("imagem_lista_jogadores.png")
            self.img_jogadores = self.img_jogadores.resize((1920, 400), Image.Resampling.LANCZOS)
            self.img_jogadores_photo = ImageTk.PhotoImage(self.img_jogadores)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.img_jogadores_photo = None

        self.canvas_top = tk.Canvas(self, width=1920, height=400, bg="#1F1E31", highlightthickness=0)
        self.canvas_top.pack()

        if self.img_jogadores_photo:
            self.canvas_top.create_image(0, 0, anchor="nw", image=self.img_jogadores_photo)

        tk.Label(self, text="Filtros de jogadores na versão final...", font=("Arial", 24, "bold"), fg="white", bg="#1F1E31").place(x=300, y=450)

        criar_perfil_button = tk.Button(self, text="CRIAR PERFIL DE JOGADOR", font=("Arial", 16, "bold"), bg="red", fg="white", 
                                        command=self.app.mostrar_tela_criar_jogador)
        criar_perfil_button.place(x=1500, y=450, width=350, height=60)

        frame_lista_jogadores = tk.Frame(self, bg="#1F1E31", bd=2, relief="groove")
        frame_lista_jogadores.place(x=650, y=550, width=800, height=400)

        style = ttk.Style(self)
        style.configure("Treeview", 
                        background="#1F1E31", 
                        foreground="white", 
                        rowheight=40, 
                        fieldbackground="#1F1E31",
                        font=("Arial", 12, "bold"))
        style.map("Treeview", background=[("selected", "red")])

        style.configure("Treeview.Heading", font=("Arial", 16, "bold"), background="#333", foreground="black")

        scrollbar = tk.Scrollbar(frame_lista_jogadores)
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(frame_lista_jogadores, yscrollcommand=scrollbar.set, 
                                 columns=("Nickname", "Jogo"), show="headings", 
                                 style="Treeview")
        self.tree.column("Nickname", width=200, anchor="center")
        self.tree.column("Jogo", width=280, anchor="center")
        self.tree.heading("Nickname", text="Nickname", anchor="center")
        self.tree.heading("Jogo", text="Jogo", anchor="center")
        self.tree.pack(fill="both", expand=True)

        scrollbar.config(command=self.tree.yview)

        self.carregar_dados_jogadores()

# Aqui é onde outra Query é inicializada no banco de dados para carregar os dados dos jogadores na lista.
    def carregar_dados_jogadores(self):
        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()
                
                query = """
                    SELECT j.nickname, g.nome_do_jogo
                    FROM tbl_jogador j
                    JOIN tbl_disponibilidade_de_jogador dj ON j.id_de_jogador = dj.id_de_jogador
                    JOIN tbl_jogo g ON dj.id_jogo = g.id_jogo;
                """
                cur.execute(query)
                jogadores = cur.fetchall()

                for i, jogador in enumerate(jogadores):
                    tag = "evenrow" if i % 2 == 0 else "oddrow"
                    self.tree.insert("", "end", values=jogador, tags=(tag,))

                self.tree.tag_configure("evenrow", background="#2A2A45")
                self.tree.tag_configure("oddrow", background="#1F1E31")

            except Exception as e:
                print(f"Erro ao carregar os dados dos jogadores: {e}")
            finally:
                cur.close()
                conn.close()
                


# Aqui é a tela onde caso o usuário queira, ele pode criar o perfil de jogador na plataforma, para futuramente participar de um time e também campeonatos.
class TelaCriarJogador(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.user_id = self.app.usuario_logado_id
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        
        self.canvas_title = tk.Canvas(self, width=1920, height=100, bg="#1F1E31", highlightthickness=0)
        self.canvas_title.pack()
        self.canvas_title.create_text(960, 52, text="CRIAR PERFIL DE JOGADOR", font=("Arial", 48, "bold"), fill="red")
        self.canvas_title.create_text(958, 50, text="CRIAR PERFIL DE JOGADOR", font=("Arial", 48, "bold"), fill="white")

        form_frame = tk.Frame(self, bg="#1F1E31")
        form_frame.place(x=560, y=200, width=800, height=500)  

        campos = ["Nickname:", "Biografia:", "Selecione o Jogo:", "Selecione a Função:", "Selecione o Rank:"]
        self.entries = {}

        y_position = 20
        for i, campo in enumerate(campos[:2]):
            tk.Label(form_frame, text=campo, font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=200, y=y_position)
            entry = tk.Entry(form_frame, width=40, font=("Arial", 14))
            entry.place(x=200, y=y_position + 30, width=510, height=40) 
            self.entries[campo] = entry
            y_position += 100

        for i, campo in enumerate(campos[2:], start=2):
            tk.Label(form_frame, text=campo, font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=200, y=y_position)
            combobox = ttk.Combobox(form_frame, width=38, font=("Arial", 14))
            combobox.place(x=200, y=y_position + 30, width=510, height=40)
            self.entries[campo] = combobox
            y_position += 100

        self.carregar_opcoes()

        voltar_button = tk.Button(self, text="VOLTAR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.app.mostrar_tela_lista_jogadores)
        voltar_button.place(x=760, y=750, width=150, height=50)

        salvar_button = tk.Button(self, text="CRIAR PERFIL JOGADOR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.salvar_jogador)
        salvar_button.place(x=970, y=750, width=300, height=50)

# Essa função foi criada para em vez do usuário digitar o jogo, a função ou o rank que ele ta, 
# ele poder selecionar já uma opção que esta no banco de dados, a partir de uma caixa de seleção (Combo Box).
    def carregar_opcoes(self):
        """Carregar opções de jogos, funções e ranks nas Combobox."""
        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()

                cur.execute("SELECT id_jogo, nome_do_jogo FROM tbl_jogo")
                jogos = cur.fetchall()
                self.entries["Selecione o Jogo:"].config(values=[jogo[1] for jogo in jogos])

                cur.execute("SELECT id_funcao, nome_da_funcao FROM tbl_funcao")
                funcoes = cur.fetchall()
                self.entries["Selecione a Função:"].config(values=[funcao[1] for funcao in funcoes])

                cur.execute("SELECT id_rank, nome_do_rank FROM tbl_rank")
                ranks = cur.fetchall()
                self.entries["Selecione o Rank:"].config(values=[rank[1] for rank in ranks])

                self.jogos = {jogo[1]: jogo[0] for jogo in jogos}
                self.funcoes = {funcao[1]: funcao[0] for funcao in funcoes}
                self.ranks = {rank[1]: rank[0] for rank in ranks}

            except Exception as e:
                print(f"Erro ao carregar opções: {e}")
            finally:
                cur.close()
                conn.close()

# Essa função utiliza duas Query para inserir os dados que o usuário selecionou para criar o perfil de jogador
# tanto na tbl_jogador quanto na tbl_disponibilidade_de_jogador esses dados são preenchidos e enviados para o banco de dados.
    def salvar_jogador(self):
        nickname = self.entries["Nickname:"].get()
        biografia = self.entries["Biografia:"].get()
        nome_jogo = self.entries["Selecione o Jogo:"].get()
        nome_funcao = self.entries["Selecione a Função:"].get()
        nome_rank = self.entries["Selecione o Rank:"].get()

        if not (nickname and nome_jogo and nome_funcao and nome_rank):
            self.show_error("Preencha todos os campos obrigatórios!")
            return

        id_jogo = self.jogos.get(nome_jogo)
        id_funcao = self.funcoes.get(nome_funcao)
        id_rank = self.ranks.get(nome_rank)

        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()

                query_jogador = """
                    INSERT INTO tbl_jogador (nickname, biografia_de_jogador, id_de_usuario)
                    VALUES (%s, %s, %s) RETURNING id_de_jogador;
                """
                cur.execute(query_jogador, (nickname, biografia, self.user_id))
                id_de_jogador = cur.fetchone()[0]

                query_disponibilidade = """
                    INSERT INTO tbl_disponibilidade_de_jogador (id_de_jogador, id_jogo, id_rank, id_funcao, descricao, horario_disponivel)
                    VALUES (%s, %s, %s, %s, '', NOW());
                """
                cur.execute(query_disponibilidade, (id_de_jogador, id_jogo, id_rank, id_funcao))

                conn.commit()
                self.show_message("Perfil de jogador criado com sucesso!")
                self.app.mostrar_tela_lista_jogadores()
            except Exception as e:
                conn.rollback()
                self.show_error(f"Erro ao criar o perfil de jogador: {e}")
            finally:
                cur.close()
                conn.close()

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Erro")
        tk.Label(error_window, text=message, font=("Arial", 16, "bold"), fg="red").pack(padx=20, pady=20)

    def show_message(self, message):
        message_window = tk.Toplevel(self)
        message_window.title("Sucesso")
        tk.Label(message_window, text=message, font=("Arial", 16, "bold"), fg="green").pack(padx=20, pady=20)
    
# Aqui é a tela onde faz a listagem de todos os times da plataforma
class TelaListaTimes(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        
        MenuLateral(self, self.app)

        try:
            self.img_times = Image.open("imagem_lista_times.png")
            self.img_times = self.img_times.resize((1920, 400), Image.Resampling.LANCZOS)
            self.img_times_photo = ImageTk.PhotoImage(self.img_times)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.img_times_photo = None

        self.canvas_top = tk.Canvas(self, width=1920, height=400, bg="#1F1E31", highlightthickness=0)
        self.canvas_top.pack()

        if self.img_times_photo:
            self.canvas_top.create_image(0, 0, anchor="nw", image=self.img_times_photo)

        tk.Label(self, text="Filtros de times na versão final...", font=("Arial", 24, "bold"), fg="white", bg="#1F1E31").place(x=300, y=450)

        criar_time_button = tk.Button(self, text="CRIAR PERFIL DE TIME", font=("Arial", 16, "bold"), bg="red", fg="white", 
                                      command=self.app.mostrar_tela_criar_time)  
        criar_time_button.place(x=1500, y=450, width=350, height=60)

        frame_lista_times = tk.Frame(self, bg="#1F1E31", bd=2, relief="groove")
        frame_lista_times.place(x=650, y=550, width=800, height=400)

        style = ttk.Style(self)
        style.configure("Treeview", 
                        background="#1F1E31", 
                        foreground="white", 
                        rowheight=40, 
                        fieldbackground="#1F1E31",
                        font=("Arial", 12, "bold"))
        style.map("Treeview", background=[("selected", "red")])

        style.configure("Treeview.Heading", font=("Arial", 16, "bold"), background="#333", foreground="black")

        scrollbar = tk.Scrollbar(frame_lista_times)
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(frame_lista_times, yscrollcommand=scrollbar.set, 
                                 columns=("Nome do Time", "Jogo"), show="headings", 
                                 style="Treeview")
        self.tree.column("Nome do Time", width=200, anchor="center")
        self.tree.column("Jogo", width=280, anchor="center")
        self.tree.heading("Nome do Time", text="Nome do Time", anchor="center")
        self.tree.heading("Jogo", text="Jogo", anchor="center")
        self.tree.pack(fill="both", expand=True)

        scrollbar.config(command=self.tree.yview)

        self.carregar_dados_times()

# Aqui uma Query de SELECT é utilizada para retornar os dados dos times.
    def carregar_dados_times(self):
        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()
                query = """
                    SELECT t.nome_do_time, g.nome_do_jogo
                    FROM tbl_time t
                    JOIN tbl_jogo g ON t.id_jogo = g.id_jogo;
                """
                cur.execute(query)
                times = cur.fetchall()

                for i, time in enumerate(times):
                    tag = "evenrow" if i % 2 == 0 else "oddrow"
                    self.tree.insert("", "end", values=time, tags=(tag,))

                self.tree.tag_configure("evenrow", background="#2A2A45")
                self.tree.tag_configure("oddrow", background="#1F1E31")

            except Exception as e:
                print(f"Erro ao carregar os dados dos times: {e}")
            finally:
                cur.close()
                conn.close()


# Aqui é a tela onde o usuário pode criar seu time, para futuramente convidar jogadores e também participar de campeonatos.
class TelaCriarTime(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.user_id = self.app.usuario_logado_id
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        
        self.canvas_title = tk.Canvas(self, width=1920, height=100, bg="#1F1E31", highlightthickness=0)
        self.canvas_title.pack()
        self.canvas_title.create_text(950, 72, text="CRIAR TIME", font=("Arial", 48, "bold"), fill="red")
        self.canvas_title.create_text(958, 70, text="CRIAR TIME", font=("Arial", 48, "bold"), fill="white")

        form_frame = tk.Frame(self, bg="#1F1E31")
        form_frame.place(x=560, y=200, width=800, height=500)

        campos = ["Nome do Time:", "Biografia do Time:", "Selecione o Jogo:"]
        self.entries = {}

        y_position = 20
        for i, campo in enumerate(campos[:2]):  
            tk.Label(form_frame, text=campo, font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=200, y=y_position)
            entry = tk.Entry(form_frame, width=40, font=("Arial", 14))
            entry.place(x=200, y=y_position + 30, width=510, height=40)
            self.entries[campo] = entry
            y_position += 100

        tk.Label(form_frame, text=campos[2], font=("Arial", 16, "bold"), fg="white", bg="#1F1E31").place(x=200, y=y_position)
        combobox_jogo = ttk.Combobox(form_frame, width=38, font=("Arial", 14))
        combobox_jogo.place(x=200, y=y_position + 30, width=510, height=40)
        self.entries[campos[2]] = combobox_jogo

        self.carregar_jogos()

        voltar_button = tk.Button(self, text="VOLTAR", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.app.mostrar_tela_lista_times)
        voltar_button.place(x=760, y=550, width=150, height=50)

        salvar_button = tk.Button(self, text="CRIAR TIME", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.salvar_time)
        salvar_button.place(x=1020, y=550, width=250, height=50)

# Essa é a função para carregar as opções de jogos na combobox, utilizando uma Query de SELECT para puxar
# essas informações da tbl_jogo.
    def carregar_jogos(self):
        """Carregar opções de jogos na combobox."""
        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()

                cur.execute("SELECT id_jogo, nome_do_jogo FROM tbl_jogo")
                jogos = cur.fetchall()
                self.entries["Selecione o Jogo:"].config(values=[jogo[1] for jogo in jogos])

                self.jogos = {jogo[1]: jogo[0] for jogo in jogos}

            except Exception as e:
                print(f"Erro ao carregar jogos: {e}")
            finally:
                cur.close()
                conn.close()

# Função para quando o usuário tiver preenchido todas as informações necessárias, rodar uma Query para
# Inserir esses dados na tbl_time.
    def salvar_time(self):

        nome_time = self.entries["Nome do Time:"].get()
        biografia_time = self.entries["Biografia do Time:"].get()
        nome_jogo = self.entries["Selecione o Jogo:"].get()

        if not (nome_time and nome_jogo):
            self.show_error("Preencha todos os campos obrigatórios!")
            return

        id_jogo = self.jogos.get(nome_jogo)

        conn = self.app.conectar_db()
        if conn:
            try:
                cur = conn.cursor()

                query_time = """
                    INSERT INTO tbl_time (nome_do_time, biografia_do_time, id_jogo)
                    VALUES (%s, %s, %s) RETURNING id_time;
                """
                cur.execute(query_time, (nome_time, biografia_time, id_jogo))
                conn.commit()

                self.show_message("Perfil de time criado com sucesso!")
                self.app.mostrar_tela_lista_times()

            except Exception as e:
                conn.rollback()
                self.show_error(f"Erro ao criar o perfil do time: {e}")
            finally:
                cur.close()
                conn.close()

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Erro")
        tk.Label(error_window, text=message, font=("Arial", 16, "bold"), fg="red").pack(padx=20, pady=20)

    def show_message(self, message):
        message_window = tk.Toplevel(self)
        message_window.title("Sucesso")
        tk.Label(message_window, text=message, font=("Arial", 16, "bold"), fg="green").pack(padx=20, pady=20)
        
# OBSERVAÇÕES IMPORTANTES!!!!
# 
# As próximas três telas que vou mostrar, são imagens de como seriam aquelas telas caso a aplicação estivesse em seu 
# estágio final, como isso é um protótipo e também por falta de tempo, optei por apenas deixar algumas imagens de como
# seriam essas telas caso estivessem na versão final do projeto.
# 
# AS TELAS EM QUESTÃO -->
#
# Tela de Buscar Jogadores (Aqui seria a tela onde os times podem buscar por jogadores e enviar propostas a eles).
# Tela de Peneira (Essa é a tela onde um jogador pode se inscrever em uma peneira para ser filtrado e escolhido em um time).
# Tela de Campeonatos (Essa tela é onde seriam os campeonatos realizados pela plataforma).

# A tela de busca por jogadores
class TelaBuscaJogadores(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        MenuLateral(self, self.app)
        self.carregar_imagem("imagem_jogadores_disponiveis.png")

    def carregar_imagem(self, caminho_imagem):
        try:
            self.img = Image.open(caminho_imagem)
            self.img = self.img.resize((1620, 1080), Image.Resampling.LANCZOS)
            self.img_photo = ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.img_photo = None

        canvas = tk.Canvas(self, width=1620, height=1080, bg="#1F1E31", highlightthickness=0)
        canvas.pack(side="right", fill="both", expand=True)
        if self.img_photo:
            canvas.create_image(0, 0, anchor="nw", image=self.img_photo)

# A tela de Peneira
class TelaPeneira(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        MenuLateral(self, self.app)
        self.carregar_imagem("imagem_peneira_times.png")

    def carregar_imagem(self, caminho_imagem):
        try:
            self.img = Image.open(caminho_imagem)
            self.img = self.img.resize((1620, 1080), Image.Resampling.LANCZOS)
            self.img_photo = ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.img_photo = None

        canvas = tk.Canvas(self, width=1620, height=1080, bg="#1F1E31", highlightthickness=0)
        canvas.pack(side="right", fill="both", expand=True)
        if self.img_photo:
            canvas.create_image(0, 0, anchor="nw", image=self.img_photo)

# A tela de campeonatos
class TelaCampeonatos(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#1F1E31")
        self.carregar_widgets()

    def carregar_widgets(self):
        MenuLateral(self, self.app)
        self.carregar_imagem("imagem_campeonato.png")

    def carregar_imagem(self, caminho_imagem):
        try:
            self.img = Image.open(caminho_imagem)
            self.img = self.img.resize((1620, 1080), Image.Resampling.LANCZOS)
            self.img_photo = ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.img_photo = None

        canvas = tk.Canvas(self, width=1620, height=1080, bg="#1F1E31", highlightthickness=0)
        canvas.pack(side="right", fill="both", expand=True)
        if self.img_photo:
            canvas.create_image(0, 0, anchor="nw", image=self.img_photo)


# Aqui é onde ocorre a inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()