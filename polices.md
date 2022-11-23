# Políticas de Trabalho e Manutenção

| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 22/11/2022 | 1.0 | Criação do documento de Politicas  | [Jonathan Araujo](https://github.com/Jonathanst1) e [Gabriel Freitas](https://github.com/gabrielfreitass1)|

# Issues

* As Issues devem seguir o nome com a atividade a ser realizada

* Use a Descrição da Issue para detalhar todas as atividades que estão sendo realizada

**Exemplo:**
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

# Branches

As branches devem seguir o seguinte padrão:

* O nome da *branch* deve seguir o nome da issue criada

<b>Exemplo:</b>

```
CriarUsuario
```
* Sempre criar uma branch a partir da main usando o seguinte comando, para isso basta entrar na branch main e depois inserrir o seguinte comando sem as chaves

```
git checkout -b <nome_da_branch>
```
# Commits

```
git status
git add <arquivo ou . para adicionar todos os arquivos alterados>
git commit -m "mensagem do que foi feito"
git push -u <nome_da_branch>
```
* Para que uma pessoa seja inclusa como contribuinte no gráfico de *commits* do GitHub, basta incluir a instrução ```Co-authored-By:``` na mensagem:
**Exemplo:**
```
Co-authored-By: Gabriel Freitas <gabriel.fbalbino@gmail.com>
```
# Pull Requests

* O conteúdo do pull request deve conter todas as atividades feitas e se estão funcionando completamente.

```
Neste pull request se realizou: 
  * Criação de usuario
  * Telas
  * Correção de bug ao...
```
