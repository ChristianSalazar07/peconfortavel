# Pé Confortável Ltda.

Este é um projeto criado com o framework Django.


## Instalação

Para instalar o projeto, utilize o MS Visual Studio Code e siga os seguintes passos:

1. Clonar o projeto usando 'git clone \<url-github-projeto>'.
2. Criar um ambiente (environment) Python.
3. Instalar no ambiente os respectivos pacotes envolvidos no projeto.
> [!NOTE]
> O ambiente virtual (environment) permite que você utilize diferentes versões do Python e/ou de módulos Python, permitindo, por exemplo, avaliar o comportamento de projeto nas versões instaladas.

> [!NOTE]
> Os pacotes envolvidos no projeto podem ser encontrados no arquivo "*requirements.txt*".

## Criando um ambiente (environment) para o projeto

### Pela linha de comando do terminal, digite:
```
python -m venv .venv
```

### Pelo Visual Code

1. Instalar as extensões do Python
2. Selecionar a paleta de comandos (`Ctrl` + `Shift` + `P`)
3. Digite Python: Create Environment...
4. Selecionar a versão do Python
5. Digite `.venv` como nome do Environment
6. Aguarde a criação da pasta `.venv` em seu projeto 

## Ativando o ambiente virtual

Para ativar o ambiente virtual, digite o comando abaixo no terminal do VS Code:

```
.\.venv\Scripts\activate
```

## Instalando o Django no ambiente virtual

Para instalar a versão mais recente do Django no \*ambiente virtual\*, digite o comando abaixo:
```
pip install Django
````

> Se quiser instalar uma versão específica do Django, utilize pip `pip install Django[==<versão do Django>]`.  
> Por exemplo: `pip install Django==4.2.18`.

## Desativando o ambiente

Para desativar o ambiente (environment), digite o comando abaixo no terminal do VS Code.

```
deactivate
```

## Licença

Por enquanto, não há uma licença definida para o projeto.
