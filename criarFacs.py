print("\n Criado com ♥ pela ETSTORE. https://discord.gg/FwKCDYWWFT\n")
def create_faction_roles(faction_name):
    """
    A FAZER
    Criar uma representacao em string dos cargos de faccao para uma faccao especifica.
    Os cargos criados serao Lider, Gerente e Membro, com as permissoes apropriadas.

    Args:
    faction_name (str): O nome da faccao.

    Retornos:
    str: Uma representacao em string dos cargos da faccao no formato especificado.
    """
    # Converte o nome da faccao e gera o titulo apropriado
    
    faction_title = ' '.join([word.capitalize() for word in faction_name.split()])
    faction_key = faction_name.capitalize()

    # Template para cada cargo
    role_template = '''["{role_key}"] = {{
    _config = {{
        title = "{role_title}",
        gtype = "job"
    }},
    {permissions}
}},\n'''

    # Define os cargos e suas permissoes
    roles = {
        "Lider" + faction_key: ["lider" + faction_name.lower() + ".permissao",
                                "gerente" + faction_name.lower() + ".permissao",
                                faction_name.lower() + ".permissao",
                                "ilegal.permissao"],
        "Gerente" + faction_key: ["gerente" + faction_name.lower() + ".permissao",
                                  faction_name.lower() + ".permissao",
                                  "ilegal.permissao"],
        faction_key: [faction_name.lower() + ".permissao",
                      "ilegal.permissao"]
    }

    # Gera a string final
    result = ""
    for role, permissions in roles.items():
        # Junta as permissoes em uma string
        permissions_str = ',\n    "'.join(permissions)
        # Formata e adiciona o cargo ao resultado
        result += role_template.format(role_key=role, role_title=role if role != faction_key else faction_title, permissions='"' + permissions_str + '"')

    return result

import time

def main():
    all_roles = ""
    while True:
        faction_name = input("Digite o nome da faccao (ou 'sair' para finalizar): ")
        if faction_name.lower() == 'sair':
            break
        elif faction_name.strip():
            all_roles += create_faction_roles(faction_name) + "\n"
            print(f"'{faction_name}' salvo.")
        else:
            print("Por favor, digite um nome de faccao.")

    with open("faccoesCriadas.txt", "w") as file:
        file.write(all_roles)
    print("Cargos e permissoes salvos em 'faccoesCriadas.txt'. O programa sera encerrado em 5 segundos.\n\n")
    print("Criado com ♥ pela ETSTORE. https://discord.gg/FwKCDYWWFT")
    time.sleep(5)

if __name__ == "__main__":
    main()
