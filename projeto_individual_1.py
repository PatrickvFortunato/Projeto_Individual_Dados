candidatos = [
    {"nome": "Candidato 1", "resultado": {"e": 5, "t": 10, "p": 8, "s": 8}},
    {"nome": "Candidato 2", "resultado": {"e": 10, "t": 7, "p": 7, "s": 8}},
    {"nome": "Candidato 3", "resultado": {"e": 8, "t": 5, "p": 4, "s": 9}},
    {"nome": "Candidato 4", "resultado": {"e": 2, "t": 2, "p": 2, "s": 1}},
    {"nome": "Candidato 5", "resultado": {"e": 10, "t": 10, "p": 8, "s": 9}}
]

def buscarCandidatos(notaMinima):
    candidatosEncontrados = []
    for candidato in candidatos:
        notas = candidato['resultado']
        if all(notas[chave] >= notaMinima[indice] for indice, chave in enumerate(['e', 't', 'p', 's'])):
            candidatosEncontrados.append(candidato["nome"])
    return candidatosEncontrados

notasMinimas = [int(input(f"Informe a nota mínima de {etapa}: ")) for etapa in ["entrevista", "teste teórico", "teste prático", "soft skills"]]

candidatosEncontrados = buscarCandidatos(notasMinimas)

if candidatosEncontrados:
    print("Os seguintes candidatos atendem aos critérios:")
    for candidato in candidatosEncontrados:
        print(candidato)
else:
    print(f'''====================================================================
                    Nenhum candidato atende aos critérios especificados.
              ==================================================================== ''')