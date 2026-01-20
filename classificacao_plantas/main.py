from catalogo_exemplo import inicializar_dados, lista_plantas
from briofitas import Briofita
from pteridofitas import Pteridofita
from ginminospermas import Gimnosperma
from angiospermas import Angiosperma

def perguntar(msg):
    return input(f"{msg} (s/n): ").strip().lower() == 's'

def classificar_interativo():
    print("\n--- IDENTIFICADOR VISUAL DE PLANTAS ---")
    print("Olhe para a planta à sua frente e responda:")

    # Pergunta 1: Presença de estrutura firme (Vasos Condutores)
    if not perguntar("A planta é muito pequena (parece um tapete verde) e não possui tronco ou caule firme?"):
        
        # Pergunta 2: Sementes
        if perguntar("Essa planta produz sementes (mesmo que você não veja flores)?"):
            
            # Pergunta 3: Flores/Frutos
            if perguntar("Você já viu essa planta produzir flores (mesmo que pequenas) ou algum tipo de fruto/vagem?"):
                grupo = "Angiosperma"
            else:
                grupo = "Gimnosperma"
        else:
            grupo = "Pteridofita"
    else:
        grupo = "Briofita"

    exibir_resultado(grupo)

def exibir_resultado(grupo_nome):
    mapeamento = {
        "Briofita": Briofita, "Pteridofita": Pteridofita,
        "Gimnosperma": Gimnosperma, "Angiosperma": Angiosperma
    }
    
    print(f"\n[ Resultado: A planta pertence ao grupo das {grupo_nome}s ]")
    print("Exemplos conhecidos no Ceará:")
    for p in lista_plantas:
        if isinstance(p, mapeamento[grupo_nome]):
            print(p.ficha_tecnica())

def main():
    inicializar_dados()
    while True:
        print("\n" + "="*40)
        print("        Guia de Botânica do Ceará")
        print("="*40)
        print("1. Identificar planta à minha frente")
        print("2. Listar todas as plantas catalogadas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == '1': classificar_interativo()
        elif opcao == '2':
            for p in lista_plantas:
                print(f"\n{p.ficha_tecnica()} | Tipo: {p.obter_tipo()}")
        elif opcao == '0': break

if __name__ == "__main__":
    main()