nomes = ["Felipe", "Maria", "João"] # Lista de nomes, onde cada nome é um elemento da lista. As listas são mutáveis, ou seja, podemos adicionar, remover ou modificar os elementos da lista.

print("Nomes:", nomes) # Imprime a lista de nomes completa.

print(nomes[0]) # Imprime o primeiro elemento da lista, que é "Felipe".
print(nomes[1]) # Imprime o segundo elemento da lista, que é "Maria".
print(nomes[2]) # Imprime o terceiro elemento da lista, que é "João".

nomes.append("Ana") # Adiciona o nome "Ana" ao final da lista de nomes.

print(nomes) # Imprime a lista de nomes atualizada, que agora inclui "Ana" no final.
print(nomes[3]) # Imprime o quarto elemento da lista, que é "Ana", pois foi adicionado no final da lista.

nomes.remove("Maria") # Remove o nome "Maria" da lista de nomes. Agora a lista contém "Felipe", "João" e "Ana".

print(nomes) # Imprime a lista de nomes atualizada, que agora não inclui mais "Maria". A lista contém "Felipe", "João" e "Ana".
print(nomes[1]) # Imprime o segundo elemento da lista, que agora é "João", pois "Maria" foi removida e os elementos foram realinhados.

#Agora vamos utilizar o FOR para mostrar os nome da lista um por um:

for nome in nomes: # O loop FOR percorre cada elemento da lista "nomes" e atribui o valor do elemento atual à variável "i" em cada iteração.
    print(nome) # Imprime o valor de "i" em cada iteração do loop, que corresponde a cada nome na lista "nomes".
