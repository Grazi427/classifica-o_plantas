from catalogo_exemplo import lista_plantas, angios, pteridos, gimnos, briofitas
from briofitas import Briofita
from pteridofitas import Pteridofita
from ginminospermas import Gimnosperma
from angiospermas import Angiosperma

def perguntar(msg):
    return input(f"{msg} (s/n): ").strip().lower() == 's'

def classificar_interativo():
    print("\n------- IDENTIFICADOR VISUAL DE PLANTAS -------")
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
    
    print(f"\n Resultado: A planta pertence ao grupo das {grupo_nome}s")
    print("\n" + "="*40)
    print("     Exemplos conhecidos no Ceará")
    print("="*40)
    for p in lista_plantas:
        if isinstance(p, mapeamento[grupo_nome]):
            print(p.ficha_tecnica())

def main():
    print(f">> Catálogo Cearense inicializado com {len(lista_plantas)} espécies! <<")
    while True:
        print("\n" + "="*40)
        print("        Guia de Botânica do Ceará")
        print("="*40)
        print("1. Identificar planta à minha frente")
        print("2. Listar plantas por categoria")
        print("3. Listar todas as plantas catalogadas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == '1': classificar_interativo()

        elif opcao == '2':
            categoria = input('\nQual categoria você deseja filtrar (angio, pteri, ginmi, brio): ')
            if categoria == 'angio':
                print("="*40)
                print("Plantas Angiospermas típicas do Ceará")
                print("="*40)
                for p in angios:
                    print(f"{p.ficha_tecnica()} | Tipo: {p.obter_tipo()}")

            elif categoria == 'pteri':
                print("\n" + "="*40)
                print("Plantas Pteridofitas típicas do Ceará")
                print("="*40)
                for p in pteridos:
                    print(f"{p.ficha_tecnica()} | Tipo: {p.obter_tipo()}")

            elif categoria == 'ginmi':
                print("\n" + "="*40)
                print("Plantas Ginminospermas típicas do Ceará")
                print("="*40)
                for p in gimnos:
                    print(f"{p.ficha_tecnica()} | Tipo: {p.obter_tipo()}")

            elif categoria == 'brio':
                print("\n" + "="*40)
                print("Plantas Briofitas típicas do Ceará")
                print("="*40)
                for p in briofitas:
                    print(f"{p.ficha_tecnica()} | Tipo: {p.obter_tipo()}")

            else:
                print("\nCategoria inválida!")

        elif opcao == '3':
            print("\n" + "="*40)
            print("Exemplos de plantas típicas do Ceará")
            print("="*40)
            for p in lista_plantas:
                print(f"{p.ficha_tecnica()} | Tipo: {p.obter_tipo()}")
        elif opcao == '0':
            break

if __name__ == "__main__":
    main()