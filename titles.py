def titles():
    with open("index.html", 'a', encoding='utf-8') as file_html:

        titles = """<body>

            <h1> Título </h1>
            <h3>Turma: ADS 5º período</h3>
            <h3>Ano: 2021</h3>
            <h3>Alunos: </h3>
        """

        file_html.write(titles)