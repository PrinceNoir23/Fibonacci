def verificar_letra_a(string):
    # Converte a string para minúsculas para facilitar a contagem
    string_lower = string.lower()
    
    # Conta quantas vezes a letra 'a' aparece na string
    quantidade_a = string_lower.count('a')
    
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

# Exemplo de uso
texto = input("Digite uma string: ")
verificar_letra_a(texto)
