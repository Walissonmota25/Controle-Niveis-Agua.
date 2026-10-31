# 💧 Aqua Monitor

### Sistema Inteligente de Monitoramento de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-Terminal-06B6D4?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-22C55E?style=for-the-badge)
![ETEC](https://img.shields.io/badge/ETEC-Agenda_11-DC2626?style=for-the-badge)

---

## 🌊 Sobre o projeto

O **AquaMonitor** é um sistema simples de monitoramento de reservatórios de água, desenvolvido em Python como atividade da **Agenda 11 — Desenvolvimento de Sistemas I**.

A proposta é simular diferentes níveis de água em um reservatório e apresentar mensagens coloridas no terminal, facilitando a identificação de cada situação.

O projeto foi desenvolvido para colocar em prática conceitos de **listas, funções, estruturas condicionais, repetição e utilização de bibliotecas externas**.

## 🎯 Objetivo

Criar um programa capaz de:

- 💧 Simular cinco níveis de água de um reservatório.
- 🎨 Exibir mensagens com cores diferentes utilizando Colorama.
- ⚙️ Organizar o código por meio de funções.
- 📋 Armazenar as situações em uma lista.
- 🚨 Identificar níveis críticos e situações de alerta.
- 🔄 Restaurar a formatação padrão do terminal.

## 🚦 Níveis de monitoramento

| Nível | Situação | Cor | Indicador |
|:---:|---|---|:---:|
| 1 | Muito baixo (crítico) | Vermelho | 🔴 |
| 2 | Baixo | Amarelo | 🟡 |
| 3 | Médio | Verde | 🟢 |
| 4 | Alto | Ciano | 🔵 |
| 5 | Muito alto (alerta) | Azul | 🔵 |

> **Observação:** As cores seguem as orientações da atividade. O sistema é uma simulação educacional e não utiliza sensores reais.

## 💻 Prévia do sistema

Ao executar o programa, o terminal apresenta:

```text
=== CONTROLE DE NÍVEIS DE ÁGUA ===

Simulação dos níveis do reservatório:

Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)

=== SITUAÇÃO ATUAL ===
Nível 3: Médio
```

Na execução real, cada mensagem é exibida com sua cor correspondente.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| 🐍 Python | Linguagem principal do projeto |
| 🎨 Colorama | Exibição de mensagens coloridas |
| 💻 VS Code | Desenvolvimento e execução |
| 🌐 GitHub | Publicação e documentação |

## 📁 Estrutura do projeto

```text
Agenda11-Controle-Niveis-Agua/
│
├── app.py
├── requirements.txt
└── README.md
```

**app.py:** contém o código principal do sistema.

**requirements.txt:** informa a biblioteca externa necessária.

**README.md:** apresenta a documentação e as instruções do projeto.

## 🚀 Como executar

### 1. Baixe o projeto

Faça o download dos arquivos do repositório e abra a pasta no VS Code.

### 2. Instale as dependências

No terminal, execute:

```bash
python -m pip install -r requirements.txt
```

### 3. Execute o sistema

```bash
python app.py
```

Pronto! O programa apresentará a simulação dos cinco níveis e a situação atual do reservatório.

## 🧠 Como funciona o código?

O programa está organizado em partes para facilitar o entendimento e futuras melhorias.

**1. Lista de situações**

Armazena as cinco mensagens correspondentes aos níveis do reservatório.

**2. Função `definir_cor(nivel)`**

Utiliza estruturas condicionais para escolher a cor adequada a cada nível.

**3. Função `exibir_situacao(nivel)`**

Consulta a lista, identifica a mensagem, aplica a cor e apresenta o resultado no terminal.

**4. Simulação dos níveis**

Utiliza um laço `for` para apresentar os cinco níveis de monitoramento.

**5. Situação atual**

A variável `nivel_atual` determina qual situação será apresentada no final da execução.

**6. Restauração das cores**

O comando `Style.RESET_ALL` restaura o estilo padrão do terminal.

## 📚 O que aprendi com este projeto?

Durante o desenvolvimento do AquaMonitor, consegui entender melhor como diferentes conceitos de programação podem trabalhar juntos.

Pratiquei principalmente:

- Criação e utilização de listas.
- Desenvolvimento de funções com responsabilidades específicas.
- Estruturas de decisão `if`, `elif` e `else`.
- Estruturas de repetição com `for`.
- Importação e utilização de bibliotecas externas.
- Organização e documentação de um projeto no GitHub.

Também percebi como pequenos recursos visuais, como as cores, podem tornar as informações mais claras para o usuário.

## 🔮 Possíveis melhorias futuras

O AquaMonitor é um projeto inicial, mas pode evoluir com novas funcionalidades:

- [ ] Permitir a escolha do nível pelo usuário.
- [ ] Exibir a porcentagem de água do reservatório.
- [ ] Registrar o histórico dos níveis.
- [ ] Criar alertas automáticos para situações críticas.
- [ ] Desenvolver uma interface gráfica.
- [ ] Integrar o sistema a sensores reais.

## 👨‍💻 Desenvolvedor

**Walisson Mota**

🎓 Estudante do curso Técnico em Desenvolvimento de Sistemas

📘 Disciplina: Desenvolvimento de Sistemas I

🏫 Projeto acadêmico — Agenda 11

💡 *"Cada projeto é uma oportunidade de transformar conhecimento em prática e evoluir como desenvolvedor."*

---

**💧 AquaMonitor — Monitorando níveis, desenvolvendo conhecimento.**

*Desenvolvido com Python e dedicação aos estudos.*
