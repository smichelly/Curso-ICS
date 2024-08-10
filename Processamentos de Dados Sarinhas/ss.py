dados = [
    {"tipo": "Estudante", "nome": "Alice", "idade": 20, "curso": "Engenharia"},
    {"tipo": "Professor", "nome": "Dr. Bob", "idade": 45, "departamento": "Física"},
    {"tipo": "Estudante", "nome": "Carlos", "idade": 22, "curso": "Matemática"},
    {"tipo": "Professor", "nome": "Dr. Diana", "idade": 50, "departamento": "Química"}
]

class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
    
class Estudante(Pessoa):
    def __init__(self, nome, idade,curso) -> None:
        super().__init__(nome, idade)
        self.curso = curso
    def apresentar(self):
        return{
            'Meu nome é': self.nome,
            'tenho':self.idade,
            'anos e Estudo': self.curso

        }
class Professor(Pessoa):
    def __init__(self, nome, idade, departamento) -> None:
        super().__init__(nome, idade)
        self.departamento = departamento

    def apresentar(self):    
        return{
            'Meu nome é': self.nome,
            'tenho': self.idade,
            ' anos e sou professor(a) no departamento de': self.departamento
        }
    
def processar_dados(dados):
    return dados
        
        
        
estudante = Estudante('Alice',20,'Engenharia')
estudante2 = Estudante('Carlos',22,'Matemática')
professor = Professor('Dr.Bob',45,'física')
professor2 = Professor('Dr.Doana',50,'Química')

lista = [estudante,estudante2,professor,professor2]
for pessoa in lista:
    print(pessoa.apresentar())