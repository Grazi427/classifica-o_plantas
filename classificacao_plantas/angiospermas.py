from plantas import Planta

class Angiosperma(Planta):
    def obter_tipo(self):
        return "Angiosperma (Plantas com flores/frutos)"

    def descrever_biologia(self):
        # POLIMORFISMO: Cada classe responde de forma diferente a este método
        return "Planta complexa com vasos, sementes, flores e frutos."