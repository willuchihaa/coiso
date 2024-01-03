#ESSE É O CODIGO POO
class personagem:
    SkillPoints = 100

    def __init__(self, raça, idade, arma, comprando=False):
        self.raça = raça  
        self.idade = idade
        self.arma = arma
        self.comprando = comprando  #ação
    def comprar(self, comprando):
        if self.comprando:
            print(f'o {self.raça} comprou {self.comprando} hehe ')
            return
        
        print('\033[31msinto muito, você não pode mais comprar por hoje, tente novamente outra hora')
        self.comprando = True

    def parar_de_comprar(self):
        if not self.comprando:
            print(f'o ser {self.raça} não está comprando {self.comprando}')
            self.comprando = False
            return
        
    def ano_de_nascimento(self):
        print(self.SkillPoints - self.idade)
    
    @classmethod    
    def qtd_skill(cls, raça, ano_de_nascimento):
        idade = cls.SkillPoints - ano_de_nascimento
        return cls(raça, idade)
    

    
#AINDA FALTA TERMINAR DE MONTAR PELA AULA DE METODOS DE CLASSES
                



         
            
# p1 = personagem('humano', 29, 'graveto')

# p1.raça = "humano"
# p1.idade = 29
# p1.arma = "graveto"  

# p1.comprando = "maçãs"

# p2 = personagem("elfo", 234, "magia")

# p2.raça = "elfo"
# p2.idade = 234
# p2.arma = "graveto"
