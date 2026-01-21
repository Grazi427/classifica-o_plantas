
---

# 🌿 Guia de Botânica do Ceará - Identificador de Plantas

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em Python que permite catalogar e identificar diferentes grupos botânicos (Briófitas, Pteridófitas, Gimnospermas e Angiospermas) presentes na região do Ceará. O sistema utiliza conceitos de **Programação Orientada a Objetos (POO)** para organizar as características biológicas de cada espécie.

## 🚀 Funcionalidades

O programa oferece três modos principais de interação:

1. **Identificador Interativo**: Através de uma árvore de decisão (perguntas de sim ou não), o programa ajuda o usuário a descobrir a qual grupo botânico uma planta pertence com base em características visíveis, como tamanho, presença de sementes, flores ou frutos.
2. **Listagem por Categoria**: Permite filtrar e visualizar apenas as espécies de um grupo específico (ex: apenas Angiospermas ou apenas Briófitas).
3. **Catálogo Completo**: Exibe todas as 40 espécies cadastradas no banco de dados exemplo, incluindo nome comum, nome científico e o local de ocorrência no Ceará (serras, sertão, litoral, etc.).

## 🛠️ Estrutura do Código e Conceitos de POO

O projeto foi construído utilizando pilares da POO:

* **Herança**: A classe base `Planta` (em `plantas.py`) define os atributos comuns como `nome_comum` e `habitat_ceara`. As classes específicas (`Briofita`, `Pteridofita`, etc.) herdam esses comportamentos.
* **Polimorfismo**: O método `obter_tipo` é implementado em cada subclasse para retornar uma descrição específica do grupo, permitindo que o sistema trate diferentes objetos de forma genérica durante a listagem.
* **Encapsulamento**: Os dados das plantas são protegidos dentro dos objetos, sendo acessados através de métodos como `ficha_tecnica()`.

### Organização de Arquivos:

* `main.py`: Ponto de entrada do programa com o menu e lógica de identificação.
* `catalogo_exemplo.py`: Contém a base de dados com as instâncias das plantas do Ceará.
* `plantas.py`: Define a classe pai.
* `angiospermas.py`, `briofitas.py`, `ginminospermas.py`, `pteridofitas.py`: Definem as regras específicas de cada grupo.

## 📂 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Mantenha todos os arquivos na mesma pasta (ou respeite a estrutura de pacotes).
3. Execute o comando:
```bash
python main.py

```



## 📸 Prints da Execução

Nesta seção, você pode adicionar as capturas de tela do programa em funcionamento:

### Menu Principal

<img width="1103" height="241" alt="image" src="https://github.com/user-attachments/assets/ee381ea0-c387-4424-8603-28074a40d2ec" />


### Processo de Identificação

<img width="1113" height="517" alt="image" src="https://github.com/user-attachments/assets/2140e762-8e15-4cd7-ae34-761b38a8bb10" />



### Listagem de Espécies

<img width="1105" height="516" alt="image" src="https://github.com/user-attachments/assets/86e22b80-668c-4163-a554-47e34023e267" />


---

**Nota:** Este projeto foi desenvolvido para fins educacionais, unindo conhecimentos de Botânica e Desenvolvimento de Software.
