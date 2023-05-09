def list_students():
    lista_nomes = [
        'Bruna',
        'Keilany',
        'Izadora',
        'José',
        'Wandson',
    ]
    
    with open("index.html", 'a', encoding='utf-8') as file_html:
        file_html.write("    <ul>")
        
        for nome in lista_nomes:
            file_html.write(f"""\n              <li>{nome}</li>""") 
            
        file_html.write("\n           </ul>")
        file_html.write("""\n</body>
        \n</html>""")


    