# Change-printer

O Change-printer é um projeto de estudos desenvolvido em Python, que tem como objetivo ajudar as pessoas que usam alguns programas e necessitam da mudança da impressora de acordo com a janela ativa. É a primeira implementação de threads em uma aplicação desenvolvida pelo autor.

O programa é capaz de detectar a janela ativa do usuário e, com base nisso, selecionar a impressora apropriada para a impressão. O programa usa a API do Windows para detectar a janela ativa e, em seguida, seleciona a impressora associada a essa janela.

Este programa é a primeira versão e pode passar por mudanças. Apesar disso, aparentemente já está funcional.

# Funcionamento

O Change-printer é capaz de detectar a janela ativa do usuário e, com base nisso, selecionar a impressora apropriada para a impressão. O programa usa a API do Windows para detectar a janela ativa e, em seguida, seleciona a impressora associada a essa janela.

# Instalação

Para instalar o Change-printer, siga os seguintes passos:

Crie um ambiente virtual Python usando o venv. Para isso, abra o terminal na pasta do projeto e execute o seguinte comando:

```python
python -m venv .venv 
```

Ative o ambiente virtual. No Windows, execute o seguinte comando no terminal:

```bash
.venv\Scripts\activate.bat
```
No Linux ou Mac, execute o seguinte comando no terminal:

```bash
source .venv/bin/activate
```
Instale as dependências do projeto a partir do arquivo requirements.txt. Para isso, execute o seguinte comando no terminal:
```bash
pip install -r requirements.txt
```
Após seguir estes passos, o ambiente virtual estará configurado e as dependências do projeto serão instaladas.

# Uso

Para usar o Change-printer, execute o programa com o Python a partir do terminal. O programa exibirá uma tela com a lista de impressoras instaladas no sistema e uma caixa para informar o caminho do aplicativo a ser monitorado. A impressora selecionada se tornará padrão toda vez que o usuário abrir o programa escolhido.
Para o arquivo já compilado, baixe o conteúdo da pasta `dist`.

Na tela do programa, existem 4 botões:

    Salvar: permite salvar a configuração atual do programa.
    Carregar: permite carregar uma configuração salva anteriormente.
    Iniciar/Parar: inicia ou para o programa.
    Esconder: minimiza o programa na bandeja do sistema.

Na bandeja do sistema, também é possível acessar o ícone do programa clicando com o botão direito do mouse. Isso abrirá um menu com as opções:

    Iniciar/Parar: inicia ou para o programa.
    Mostrar/Esconder: mostra ou esconde o programa na tela.
    Sair: fecha o programa.

O programa é capaz de detectar a janela ativa do usuário e, com base nisso, selecionar a impressora apropriada para a impressão. O programa usa a API do Windows para detectar a janela ativa e, em seguida, seleciona a impressora associada a essa janela.
Contribuição

O Change-printer é um projeto de código aberto e estamos abertos a contribuições da comunidade. Se você deseja contribuir para o projeto, sinta-se à vontade para enviar pull requests com novos recursos, correções de bugs ou melhorias na documentação.

# Notas

Este programa é a primeira versão e pode passar por mudanças. Apesar disso, aparentemente já está funcional.
# Licença

Este programa é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
