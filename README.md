# 🧮 Calculadora Modular Python com Histórico JSON

Uma calculadora simples desenvolvida em Python que utiliza uma arquitetura modular para realizar operações aritméticas fundamentais. O projeto destaca o uso de manipulação de arquivos **(JSON)**, **tratamento de exceções e organização de pacotes.**

---

## 📌 Funcionalidades

- **➕ Operações Matemáticas:** Soma, Subtração, Multiplicação (com múltiplos números) e Divisão.

- **🗃️ Persistência de Dados:** Armazenamento automático de todas as operações realizadas em um arquivo .json.

- **📄 Gestão de Histórico:** Funções dedicadas para visualizar e limpar o histórico de cálculos.

- **✅ Validação Robusta:** Tratamento de erros para entradas inválidas (letras onde deveriam ser números) e prevenção de divisão por zero.

- **💻 Interface CLI:** Menu interativo amigável via terminal.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3

- **Persistência:** JSON (JavaScript Object Notation)

- **Módulos Internos:** `os`, `json`, `sys`

---

## 📁 Estrutura do Projeto

```bash
calculadora/
│
├── cfgcalculadora/
│   ├── __init__.py
│   ├── gerenciar_arquivos.py
│   ├── operacoes.py
│   ├── uteis.py
│   └── validadores.py
│
├── historico/
│   └── operacoes_salvas.json
│
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

---

## 🚀 Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/kauasantos-dev/calculadora.git
```

2. **Acesse a pasta do projeto:**

```bash
cd calculadora
```

3. **Execute a aplicação:**

```bash
python main.py
```

**⚠️ IMPORTANTE:**  

Este projeto é uma aplicação **CLI** e deve ser executado em um terminal local,
como **Prompt de Comando** ou **PowerShell**.

---

## 📝 Exemplo de Uso

Ao selecionar a operação de Soma (Opção 1), o programa solicitará os números. Você pode inserir quantos desejar e digitar qualquer letra para finalizar e obter o resultado. O log será salvo automaticamente no formato:

```json
{
  "10 + 20 + 5": 35
}
```

---

## 🛡️ Tratamento de Erros

O sistema está preparado para lidar com:

- `ZeroDivisionError`: Impede falhas ao tentar dividir por zero.

- `ValueError`: Captura entradas de texto quando números são esperados.

- `FileNotFoundError`: Gerencia a criação automática do diretório de histórico caso ele não exista.

---

## 🧠 Aprendizados

O desenvolvimento deste projeto contribuiu para o **aprendizado** e **aprofundamento** de conceitos importantes, sendo eles:

### ✔️ Organização Modular

- Aprimorei a prática de estruturar projetos em **pacotes** e **módulos correspondentes as suas responsabilidades**.

### ✔️ Boas Práticas de Desenvolvimento

- Nomeei de forma clara e objetiva **variáveis, funções, módulos e pacotes** para **maior compreensão** e **simplicidade** do sistema.

- Evitei **repetição de código** criando **funções reutilizáveis**.

- Desenvolvi a aplicação utilizando conceitos de **fácil entendimento**, mantendo a **lógica simples**, **eficiente** e sem **complexidade desnecessária**.

### ✔️ Manipulação De Arquivos

- Aprofundei o conhecimento em **manipulação de arquivos** `.json` e persistência de dados.

- Implementei **caminhos absolutos** e **dinâmicos** utilizando a biblioteca `os` do python para garantir **maior compatibilidade** com **sistemas operacionais**.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma **issue** ou enviar um **pull request** para melhorar o projeto.

---

## ⚖️ Licença

Este programa está licenciado sob a **licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Kauã Santos | Estudante de Análise e Desenvolvimento de Sistemas (ADS) - IFRN**  

**📞 Contato:**  

📧 **E-mail:** [kavillykaua@gmail.com](mailto:kavillykaua@gmail.com)  
💻 **GitHub:** [github.com/kauasantos-dev](https://github.com/kauasantos-dev)  
🌐 **LinkedIn:** [www.linkedin.com/in/kauasantos1](https://www.linkedin.com/in/kauasantos1)