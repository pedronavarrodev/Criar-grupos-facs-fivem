# Gerador de Cargos de Facção para GTA Roleplay

Este script Python é utilizado para gerar automaticamente cargos e permissões para diferentes facções no contexto de GTA Roleplay.

## Como Usar

Para usar este script, você precisa ter o Python instalado em seu sistema. O script pode ser executado em um terminal ou prompt de comando.

### Execução

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde o script `faction_generator.py` está localizado.
3. Execute o script com o comando `python faction_generator.py`.
4. Quando solicitado, digite o nome da facção que você deseja criar cargos e permissões. Por exemplo, `Brasil`.
5. Após inserir cada nome de facção, os cargos e permissões correspondentes serão automaticamente gerados.
6. Para finalizar e salvar os resultados em um arquivo `.txt`, digite `sair`.
7. Os resultados serão salvos em um arquivo chamado `faction_roles.txt` no mesmo diretório.

## Compilando o Script em um Executável

Para compilar este script em um arquivo executável `.exe` para Windows, você precisará usar o PyInstaller.

### Pré-requisitos

- Python instalado em seu sistema.
- PyInstaller, que pode ser instalado via pip com o comando `pip install pyinstaller`.

### Compilação

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde o script `criarFacs.py` está localizado.
3. Execute o comando `pyinstaller --onefile criarFacs.py`. Isso criará uma pasta `dist` com o arquivo executável dentro.
4. Você pode encontrar o executável `criarFacs.exe` dentro da pasta `dist` com o ícone de um disquete.

## Notas

- O script e o executável gerado são compatíveis apenas com sistemas Windows.
- Certifique-se de ter permissão de escrita no diretório para salvar o arquivo `.txt`.

---

Desenvolvido pela ETSTORE para facilitar a criação de cargos e permissões em servidores de GTA Roleplay.
