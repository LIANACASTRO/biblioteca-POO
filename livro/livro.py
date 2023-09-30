class Livro:
    def __init__(self, livro_id, autor, titulo, ano_publi):
        self.__livro_id = livro_id
        self.__autor = autor
        self.__titulo = titulo
        self.__ano_publi = ano_publi
        self.__disponivel = True

    def estaDisponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Livro emprestado com sucesso")
        else:
            print("Livro indisponivel")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print("Livro devolvido a estante!")
        else:
            print("O livro já foi devolvido")


    @property
    def livro_id(self):
        return self.livro_id

    @livro_id.setter
    def livro_id(self, value):
        self.livro_id = value

    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self, value):
        self.titulo = value

    @property
    def ano_publi(self):
        return self.ano_publi

    @ano_publi.setter
    def ano_publi(self, value):
        self.ano_publi = value

    @property
    def autor(self):
        return self.autor

    @autor.setter
    def autor(self, value):
        self.autor = value
