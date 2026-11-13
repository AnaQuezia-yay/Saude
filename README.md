# 🏥 medIA / SaúdeBot — Sistema de Guia Preventivo e Triagem de Saúde

O **medIA (SaúdeBot)** é uma aplicação web interativa desenvolvida com **Flask (Python)** e **Frontend Mobile-First** voltada para a pré-triagem de sintomas, orientação rápida ao usuário e encaminhamento hospitalar consciente.

O sistema atua como um assistente de primeiro contato, auxiliando o paciente a categorizar a gravidade dos seus sintomas, informando a intensidade e comorbidades, e apresentando recomendações inteligentes de unidades de saúde mais próximas ou com menor tempo de espera.

---

## 📱 Demonstração e Telas do Sistema

A interface foi projetada simulando uma aplicação mobile nativa, oferecendo um fluxo guiado e intuitivo:

1. **📍 Tela 1 — Localização**: Captura a localização ou endereço informado pelo usuário.
2. **🩺 Tela 2 — Seleção de Sintomas**: Primeiro nível de escolha do estado geral (Leve, Moderado, Grave) ou acesso direto ao **Chatbot**.
3. **📊 Tela 3 — Intensidade dos Sintomas**: Avaliação quantitativa da intensidade do quadro (*Leve: 10%–30%*, *Moderada: 40%–60%*, *Grave: 70%–100%*).
4. **📋 Tela 4 — Comorbidades**: Triagem sobre condições preexistentes (Diabetes, Hipertensão, etc.).
5. **🏥 Tela 5 — Recomendações Hospitalares**: Apresenta opções de unidades de atendimento categorizadas:
   - **Opção Equilibrada** (Distância vs. tempo de atendimento);
   - **Mais Próximo** (Menor deslocamento);
   - **Menor Espera** (Fila reduzida).
6. **🗺️ Tela 6 — Traçado de Rota**: Mapa interativo simulado em SVG com traçado visual, cálculo de distância (km), estimativa de tempo e status do GPS.
7. **🤖 Tela do Chatbot (SaúdeBot)**: Atendimento conversacional com classificação em tempo real dos sintomas digitados pelo usuário.

---

## ✨ Funcionalidades Principais

- **Triagem Conversacional Inteligente**: Processamento das mensagens no backend para identificação de gravidade com base em palavras-chave.
- **Classificação em 3 Níveis**:
  - 🔴 **Graves / Urgentes**: Falta de ar, dor no peito, desmaio, sangramento.
  - 🟡 **Moderados**: Febre, dor no corpo, diarreia, tontura, vômito.
  - 🟢 **Leves**: Dor de cabeça, enjoo, tosse, coriza, cansaço.
- **Interface Responsiva & Mobile-First**: Layout com frame de smartphone para desktop e tela cheia em dispositivos móveis.
- **Navegação SPA Simples (Single Page Application)**: Transições suaves entre etapas sem recarregamento de página.
- **Feedback Imediato**: Respostas em JSON consumidas de forma assíncrona pela Fetch API.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - [Python 3](https://www.python.org/)
  - [Flask](https://flask.palletsprojects.com/) (Roteamento web e API REST)
- **Frontend**:
  - HTML5 & CSS3
  - JavaScript moderno (ES6+, Fetch API assíncrona)
  - [Tailwind CSS](https://tailwindcss.com/) (Estilização via CDN)
  - [Lucide Icons](https://lucide.dev/) (Ícones da interface)

---

## 📂 Estrutura de Diretórios

```text
Saude/
├── app.py                  # Servidor Flask com rotas e lógica de classificação
├── static/
│   ├── chat.css            # Estilos dedicados ao chat
│   └── style.css           # Estilos visuais adicionais e animações
├── templates/
│   ├── index.html          # Protótipo completo da aplicação com fluxo guiado e chat
└── README.md               # Documentação geral do sistema
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.8+** e o **pip** instalados em sua máquina.

### 1. Clonar ou Acessar a Pasta do Projeto
Abra o terminal na pasta raiz do projeto:
```bash
cd Saude
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas recomendado)
- **No Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **No Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar as Dependências
Instale o Flask através do pip:
```bash
pip install flask
```

### 4. Iniciar o Servidor
Execute o script principal:
```bash
python app.py
```

### 5. Acessar a Aplicação
Abra seu navegador e acesse:
```
http://127.0.0.1:5000
```
ou
```
http://localhost:5000
```

---

## 🔌 Documentação da API

### `POST /api/chat`
Processa a mensagem enviada pelo usuário e retorna a classificação do sintoma.

- **URL**: `/api/chat`
- **Método**: `POST`
- **Cabeçalhos**: `Content-Type: application/json`

#### Exemplo de Requisição:
```json
{
  "mensagem": "estou sentindo muita falta de ar e dor no peito"
}
```

#### Exemplo de Resposta:
```json
{
  "resposta": "Entendi. Seu sintoma se configura na classificação: **Sintomas Graves / Urgentes**."
}
```

---

## 🧠 Base de Regras de Sintomas

| Gravidade | Termos e Sintomas Reconhecidos |
| :--- | :--- |
| **Graves / Urgentes** | `falta de ar`, `peito`, `desmaio`, `sangramento`, `sangue` |
| **Moderados** | `febre`, `corpo`, `diarreia`, `tontura`, `vômito`, `vomito` |
| **Leves** | `cabeça`, `enjoo`, `enjoada`, `tosse`, `coriza`, `cansaço` |
| **Indeterminado** | Resposta de orientação preventiva para buscar apoio profissional. |

---

## ⚠️ Aviso Legal / Disclaimer
Este sistema possui caráter **estritamente experimental, acadêmico e educacional**. As orientações e classificações automáticas **NÃO substituem uma consulta, diagnóstico ou atendimento médico profissional**. Em casos de dor súbita e intensa, sangramento grave, falta de ar severa ou risco à vida, procure imediatamente uma unidade de pronto atendimento ou acione o serviço de emergência (**SAMU 192**).
