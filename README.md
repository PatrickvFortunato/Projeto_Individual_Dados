<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
        }

        h2 {
            color: #444;
            margin-top: 20px;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }

        p {
            margin-bottom: 20px;
        }

        pre {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        code {
            color: #c7254e;
            background-color: #f9f2f4;
            padding: 0 3px;
            border-radius: 3px;
        }

        ul {
            margin-bottom: 20px;
        }

        li {
            margin-bottom: 5px;
        }

        .license {
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Projeto Individual - Avaliação de Candidatos</h1>
        <p>Este é um projeto individual desenvolvido para filtrar candidatos com base em critérios de pontuação em várias etapas de avaliação, como entrevista, teste teórico, teste prático e habilidades interpessoais (soft skills).</p>

        <h2>Funcionalidades</h2>
        <ul>
            <li><code>buscarCandidatos(notaMinima)</code>: Uma função que recebe uma lista de notas mínimas para cada etapa de avaliação e retorna os nomes dos candidatos que atendem a esses critérios.</li>
        </ul>

        <h2>Uso</h2>
        <ol>
            <li>Clone o repositório:</li>
            <pre><code>git clone https://github.com/PatrickvFortunato/Projeto_Individual_Dados.git</code></pre>
            <li>Execute o script Python:</li>
            <pre><code>python projeto_individual_1.py</code></pre>
            <li>Insira as notas mínimas para cada etapa conforme solicitado.</li>
            <li>Veja os resultados impressos no console.</li>
        </ol>

        <h2>Exemplo de Uso</h2>
        <pre><code>notasMinimas = [7, 5, 6, 7]  # Notas mínimas para [entrevista, teste teórico, teste prático, soft skills]

candidatosEncontrados = buscarCandidatos(notasMinimas)

if candidatosEncontrados:
    print(f'''
===============================================
Os seguintes candidatos atendem aos critérios:''')
    for candidato in candidatosEncontrados:
        print(candidato)
else:
    print(f'''
=============================================================
    Nenhum candidato atende aos critérios especificados.
=============================================================''')</code></pre>

        <h2>Contribuição</h2>
        <p>Contribuições são bem-vindas! Para contribuir com este projeto, siga estas etapas:</p>
        <ol>
            <li>Faça um fork do projeto.</li>
            <li>Crie sua feature branch (<code>git checkout -b feature/AmazingFeature</code>).</li>
            <li>Faça commit das suas alterações (<code>git commit -m 'Add some AmazingFeature'</code>).</li>
            <li>Envie para a branch principal (<code>git push origin feature/AmazingFeature</code>).</li>
            <li>Abra um pull request.</li>
        </ol>

        <h2>Licença</h2>
        <p class="license">Distribuído sob a licença MIT. Veja <code>LICENSE</code> para mais informações.</p>
    </div>
</body>
</html>
