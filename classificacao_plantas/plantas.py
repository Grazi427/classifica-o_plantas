class Planta():
    def __init__(self, nome_comum, nome_cientifico, habitat_ceara):
        # ENCAPSULAMENTO: Atributos protegidos com '_'
        self._nome_comum = nome_comum
        self._nome_cientifico = nome_cientifico
        self._habitat = habitat_ceara

    def obter_tipo(self):
        pass

    def ficha_tecnica(self):
        return f"- Nome: {self._nome_comum} | Nome científico: ({self._nome_cientifico}) | Local de ocorrência: {self._habitat}"

    # ABSTRAÇÃO: Método que deve ser implementado obrigatoriamente pelas subclasses
    def descrever_biologia(self):
        pass