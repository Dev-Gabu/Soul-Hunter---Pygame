# 👻 Soul Hunter - Um Caçador de Almas em Pygame

Bem-vindo ao repositório do **Soul Hunter**, um jogo simples desenvolvido em Python utilizando a biblioteca Pygame. O objetivo é caçar fantasmas que aparecem aleatoriamente na tela, em um estilo clássico de "point-and-click" (tiro ao alvo), inspirado em jogos como Duck Hunt.

## ✨ Funcionalidades

* **Mecânica FPS/Duck Hunt:** Use o mouse para mirar e clicar nos fantasmas.
* **Sistema de Pontuação:** Colete almas (pontos) ao acertar os alvos.
* **Spawn Dinâmico:** Fantasmas aparecem e desaparecem após um tempo limitado.
* **Camadas Visuais:** Uso de múltiplas camadas (fundo, meio, frente) para criar um efeito de profundidade.
* **Mira Customizada:** Mira personalizada em sprite, ocultando o cursor padrão do sistema.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para clonar o repositório e executar o jogo localmente.

### 1. Clonar o Repositório
git clone https://github.com/Dev-Gabu/Soul-Hunter---Pygame.git
cd Soul-Hunter---Pygame

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente (Windows - PowerShell)
.\venv\Scripts\activate

# Ativa o ambiente (Linux/macOS - Bash)
source venv/bin/activate

# Instala dependências
pip install -r requirements.txt

# Inicia o jogo
python main.py

## Estrutura do Código
O projeto é modularizado para facilitar a manutenção:

main.py: Contém o Loop Principal do Jogo, tratamento de eventos, lógica de spawn e renderização.

settings.py: Armazena todas as constantes do projeto (tamanho da tela, FPS, cores e caminhos).

souls.py: Contém a classe Fantasma, responsável pela lógica de movimento e tempo de vida.

utils.py: Funções auxiliares, como o carregar_imagem com tratamento de erro.

## Contribuições
Sinta-se à vontade para sugerir melhorias, como novos tipos de fantasmas, efeitos sonoros ou aprimoramentos visuais.