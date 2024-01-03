class Açoes:


# TENTAR MISTURAR ISSO COM O MAGIAS E PERSONAGENS 

    def __init__(self, raça):
        self.raça = raça
        self.text = ""
        self.texto = ""

    def le_entrada(self):
        self.text = input("voce deseja abrir esta porta na sua frente???? ")
        self.texto = int(input("qual a seu nivel? "))


    def abrir_porta(self):
        for self.text in range(0, 75):
            if self.texto > 6:
                print("Parabéns, você abriu uma porta!")
                return
            elif self.texto < 6:
                print("Seu nivel é muito baixo para executar esta ação ")
                return
            

        #player1 = Açoes("humano")
        #player1.le_entrada()
        #player1.abrir_porta()


#COLOCAR TODOS OS ARQUIVOS EM UMA UNICA PASTA 
#TERMINADO ASDASDASD








