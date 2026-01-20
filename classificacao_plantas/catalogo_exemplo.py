from briofitas import Briofita
from pteridofitas import Pteridofita
from ginminospermas import Gimnosperma
from angiospermas import Angiosperma

lista_plantas = []

def inicializar_dados():
    # --- ANGIOSPERMAS (10 Exemplos) ---
    # Foco: Caatinga, Litoral e Serras
    angios = [
        Angiosperma("Carnaúba", "Copernicia prunifera", "Várzeas e carnaubais do Sertão"),
        Angiosperma("Mandacaru", "Cereus jamacaru", "Caatinga (Semiárido)"),
        Angiosperma("Juazeiro", "Ziziphus joazeiro", "Sertão (Margens de rios)"),
        Angiosperma("Aroeira-do-sertão", "Myracrodruon urundeuva", "Mata Seca / Caatinga"),
        Angiosperma("Angico-branco", "Anadenanthera colubrina", "Mata Seca"),
        Angiosperma("Imburana-de-cheiro", "Amburana cearensis", "Caatinga"),
        Angiosperma("Ipê-Amarelo", "Handroanthus serratifolius", "Mata Atlântica das Serras"),
        Angiosperma("Cajueiro", "Anacardium occidentale", "Litoral e Tabuleiros"),
        Angiosperma("Jatobá", "Hymenaea courbaril", "Serras e Enclaves Úmidos"),
        Angiosperma("Mulungu", "Erythrina velutina", "Beiras de rios no Sertão")
    ]

    # --- PTERIDÓFITAS (10 Exemplos) ---
    # Foco: Serras úmidas (Ibiapaba, Baturité e Araripe)
    pteridos = [
        Pteridofita("Samambaia-açu", "Cyathea phalerata", "Serra de Ubajara"),
        Pteridofita("Avenca", "Adiantum petiolatum", "Maciço de Baturité"),
        Pteridofita("Selaginela-da-caatinga", "Selaginella convoluta", "Afloramentos rochosos no Sertão"),
        Pteridofita("Samambaia-paulista", "Nephrolepis brownii", "Zonas serranas"),
        Pteridofita("Samambaia-prateada", "Pityrogramma calomelanos", "Serra de Guaramiranga"),
        Pteridofita("Samambaia-de-metro", "Polypodium sp.", "Troncos de árvores na Serra"),
        Pteridofita("Avencão", "Pteris denticulata", "Mata de galeria na Ibiapaba"),
        Pteridofita("Samambaia-do-brejo", "Acrostichum aureum", "Manguezais litorâneos"),
        Pteridofita("Avenca-do-nordeste", "Anemia hirta", "Chapada do Araripe"),
        Pteridofita("Trepadeira-de-esporos", "Lygodium venustum", "Mata Atlântica cearense")
    ]

    # --- BRIÓFITAS (10 Exemplos) ---
    # Foco: Pequenas plantas de locais úmidos das Serras
    briofitas = [
        Briofita("Musgo-de-tronco", "Meteorium nigrescens", "Serra de Baturité"),
        Briofita("Musgo-verde-pendente", "Zelometeorium ambiguum", "Guaramiranga"),
        Briofita("Musgo-estrela", "Bryum sp.", "Solo úmido das serras"),
        Briofita("Musgo-fênix", "Fissidens sp.", "Rochas próximas a riachos"),
        Briofita("Hepática-em-fita", "Marchantia polymorpha", "Canteiros úmidos"),
        Briofita("Hepática-folhosa", "Lejeunea sp.", "Troncos na Mata Atlântica"),
        Briofita("Musgo-de-rocha", "Groutiella chimborazensis", "Serra da Ibiapaba"),
        Briofita("Musgo-tapete", "Stereophyllum radiculosum", "Rochas sombreadas"),
        Briofita("Musgo-aveludado", "Syrrhopodon sp.", "Zonas de alta umidade"),
        Briofita("Musgo-das-nuvens", "Frullania sp.", "Altitude elevada nas serras")
    ]

    # --- GIMNOSPERMAS (10 Exemplos) ---
    # Nota: No Ceará são predominantemente ornamentais ou cultivadas em serras frias
    gimnos = [
        Gimnosperma("Cica", "Cycas revoluta", "Jardins urbanos em Fortaleza"),
        Gimnosperma("Pinheiro-do-Paraná", "Araucaria angustifolia", "Cultivado em Guaramiranga"),
        Gimnosperma("Cipreste-italiano", "Cupressus sempervirens", "Zonas serranas frias"),
        Gimnosperma("Tuia-limão", "Cupressus macrocarpa", "Paisagismo serrano"),
        Gimnosperma("Pinheiro-de-Natal", "Araucaria heterophylla", "Jardins do Litoral"),
        Gimnosperma("Zamia", "Zamia furfuracea", "Paisagismo moderno"),
        Gimnosperma("Pinheiro-caribenho", "Pinus caribaea", "Reflorestamento em serras"),
        Gimnosperma("Pinheiro-budista", "Podocarpus macrophyllus", "Arborização urbana"),
        Gimnosperma("Zimbro", "Juniperus chinensis", "Vasos e jardins"),
        Gimnosperma("Tuia-da-igreja", "Thuja occidentalis", "Praças de cidades serranas")
    ]

    # Unificando na lista global do sistema
    lista_plantas.extend(angios + pteridos + briofitas + gimnos)
    print(f">> Catálogo Cearense inicializado com {len(lista_plantas)} espécies! <<")