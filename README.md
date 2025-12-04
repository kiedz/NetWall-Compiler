# NetWall: Domain-Specific Language (DSL) para Firewalls

Projeto da disciplina de **Compiladores** - Engenharia da Computação.
Uma linguagem de domínio específico projetada para simplificar a criação de regras de firewall, compilando uma sintaxe legível e estruturada para scripts de `iptables` (Linux).

## 👨‍💻 Equipe
* **Nome:** Ronaldo Lucas de Souza Silva
* **Professor:** Luis Carlos Menezes

---

## 🚀 Motivação
A administração de redes Linux frequentemente depende do utilitário `iptables`. Embora poderoso, o `iptables` possui uma sintaxe verbosa, repetitiva e difícil de auditar visualmente. Um erro simples em uma flag pode comprometer a segurança do servidor.

A **NetWall** resolve essa "tarefa tediosa" permitindo que o administrador declare suas intenções de segurança de forma declarativa e organizada. O compilador se encarrega de gerar os comandos de terminal corretos e livres de erros de sintaxe.

**Diferenciais da Linguagem:**
1.  **Legibilidade:** Uso de palavras-chave naturais (`allow`, `block`, `from`, `to`).
2.  **Organização:** Introdução de **Grupos de Escopo** (`group Name { ... }`), permitindo agrupar regras logicamente (ex: regras de Database, regras Web), algo que não existe nativamente no iptables linear.

---

## 🛠️ Detalhes Técnicos da Implementação
O projeto foi desenvolvido seguindo a estrutura de um compilador clássico:

* **Ferramenta:** Python 3 + ANTLR4.
* **Análise Léxica e Sintática:** Definida formalmente na gramática `src/NetWall.g4`.
* **Geração de Código:** Utiliza o padrão de projeto **Visitor** para percorrer a Árvore Sintática Abstrata (AST) e traduzir as instruções.
* **Ambiente:** O projeto contém uma configuração completa de `.devcontainer`, garantindo execução reprodutível em qualquer máquina via Docker ou GitHub Codespaces.

---

## 📖 Guia de Como Executar

### Opção 1: Via GitHub Codespaces (Recomendado ⭐)
Esta opção garante que o ambiente seja idêntico ao de desenvolvimento, sem necessidade de instalações locais.

1.  No repositório do GitHub, clique no botão verde **<> Code**.
2.  Selecione a aba **Codespaces** e clique em **Create codespace on main**.
3.  Aguarde o ambiente carregar. As dependências (Java, ANTLR Runtime, Python) serão instaladas automaticamente.
4.  No terminal do Codespaces, execute:
    ```bash
    python src/main.py testes/exemplo.nw
    ```

### Opção 2: Execução Local
Pré-requisitos: Python 3.x e Java (necessário apenas para regenerar a gramática do ANTLR, se houver alterações).

1.  Clone o repositório.
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o compilador:
    ```bash
    python src/main.py testes/exemplo.nw
    ```