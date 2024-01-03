
class Bonecos:
    SkillPoints = 100
    def __init__(self, raça, idade):
        self.raça = raça 
        self.idade = idade

    def qtd_skills(self):
        if "humano":
            print(f'{self.raça}, aqui estão suas SkillPoints')
            print(self.SkillPoints * self.idade)
        elif "demonio":
            print("demonio aqui estao suas SkillPoints")
            print(self.SkillPoints * self.idade)
pass