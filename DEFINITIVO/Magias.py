class magias:
    SkillPoints = 100
    fogo = 15
    raio = 45 
    invisibildade = 20 
    gravidade = 60

    def __init__(self, raça ,fogo, raio, invisibilidade, gravidade):
        self.fogo = 15
        self.raio = 45 
        self.invisibilidade = 20
        self.gravidade = 60
        self.raça = raça

    def magia_fogo(self):
            if "humano":
                print(f'{self.raça} lançou um ataque de fogo')
                print("quantidade de SkillPoints restantes: ")
                print(self.SkillPoints - self.fogo)
            elif "humano":
                print(f'{self.raça} lançou um ataque de fogo')
                print("quantidade de SkillPoints restantes: ")
                print(self.SkillPoints - self.fogo)
                
    def magia_raio(self):
            if "humanano":
                print(f'{self.raça} lançou um ataque de raio')
                print("quantidade de SkillPoints restantes: ")
                print(self.SkillPoints - self.raio)
                
            elif "demonio":
                print(f'{self.raça} lançou um ataque de raio')
                print("quantidade de SkillPoints restantes: ")
                print(self.SkillPoints - self.raio)
                

    def magia_invisibilidade(self):
            if "humano":
                    print(f'{self.raça} lançou um ataque de invisibilidade')
                    print("quantidade de SkillPoints restantes: ")
                    print(self.SkillPoints - self.invisibildade)
                    
            elif "demonio":
                    print(f'{self.raça} lançou um ataque de invisibilidade')
                    print("quantidade de SkillPoints restantes: ")
                    print(self.SkillPoints - self.magia_invisibilidade)
                    
    def magia_gravidade(self):
            if  "humano":
                print(f'{self.raça} lançou um ataque de gravidade')
                print("quantidade de SkillPoints restantes: ")
                print(self.SkillPoints - self.gravidade)
                
            elif "demonio":
                print(f'{self.raça} lançou um ataque de gravidade')
                print("quantidade de SkillPoints restantes: ")
                print(self.SkillPoints - self.magia_gravidade)
                
#p1=magias("humano","fogo","raio","invisibilidade","gravidade")
#p1.magia_fogo()
