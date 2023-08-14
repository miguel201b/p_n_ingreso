def generate_schedule(apellido):
    letra = apellido[0].lower()

    horario = {
        "Bienvenida": "",
        "EMA": "",
        "INSCRIPCION": "",
        "EDI": "",
        "CURSO DE GÉNERO": "",
        "RECORRIDOS": ""
    }

    # Bienvenida
    if letra in "abc":
        horario["Bienvenida"] = "Sábado a las 10"
    elif letra in "defg":
        horario["Bienvenida"] = "Sábado a las 12"
    elif letra in "hijkl":
        horario["Bienvenida"] = "Sábado a las 14"
    elif letra in "mnop":
        horario["Bienvenida"] = "Domingo a las 10"
    elif letra in "qr":
        horario["Bienvenida"] = "Domingo a las 12"
    else:  # s-z
        horario["Bienvenida"] = "Domingo a las 14"

    # EMA
    if letra in "ab":
        horario["EMA"] = "Miércoles a las 12"
    elif letra == "c":
        horario["EMA"] = "Miércoles a las 9"
    elif letra in "def":
        horario["EMA"] = "Miércoles a las 16:30"
    elif letra == "g":
        horario["EMA"] = "Jueves a las 12"
    elif letra in "hijkl":
        horario["EMA"] = "Jueves a las 9"
    elif letra == "m":
        horario["EMA"] = "Jueves a las 16:30"
    elif letra in "npqr":
        horario["EMA"] = "Viernes a las 12"
    elif letra == "r":
        horario["EMA"] = "Viernes a las 9"
    else:  # s-z
        horario["EMA"] = "Viernes a las 16:30"

    # INSCRIPCION
    if letra in "ab":
        horario["INSCRIPCION"] = "Miércoles a las 10:30"
    elif letra == "c":
        horario["INSCRIPCION"] = "Miércoles a las 12"
    elif letra in "def":
        horario["INSCRIPCION"] = "Miércoles a las 15"
    elif letra == "g":
        horario["INSCRIPCION"] = "Jueves a las 10:30"
    elif letra in "hijklm":
        horario["INSCRIPCION"] = "Jueves a las 12"
    elif letra == "m":
        horario["INSCRIPCION"] = "Jueves a las 15"
    elif letra in "npqr":
        horario["INSCRIPCION"] = "Viernes a las 10:30"
    elif letra == "r":
        horario["INSCRIPCION"] = "Viernes a las 12"
    else:  # s-z
        horario["INSCRIPCION"] = "Viernes a las 15"

    # EDI
    if letra in "abcdef":
        horario["EDI"] = "Jueves 13-17"
    elif letra in "ghijklm":
        horario["EDI"] = "Viernes 15-19"
    else:  # n-z
        horario["EDI"] = "Jueves 7-11"

    # CURSO DE GÉNERO
    if letra in "abcdef":
        horario["CURSO DE GÉNERO"] = "Lunes, Martes, Jueves y Viernes a las 9"
    elif letra in "ghijklm":
        horario["CURSO DE GÉNERO"] = "Lunes, Martes, Miércoles y Viernes a las 11"
    else:  # n-z
        horario["CURSO DE GÉNERO"] = "Lunes, Martes, Miércoles y Jueves a las 13"

    # RECORRIDOS
    if letra in "abc":
        horario["RECORRIDOS"] = "Lunes a las 11"
    elif letra in "def":
        horario["RECORRIDOS"] = "Martes a las 11"
    elif letra == "g":
        horario["RECORRIDOS"] = "Lunes a las 13"
    elif letra in "hijkm":
        horario["RECORRIDOS"] = "Martes a las 13"
    elif letra in "nopqr":
        horario["RECORRIDOS"] = "Lunes a las 15"
    else:  # s-z
        horario["RECORRIDOS"] = "Martes a las 15"

    # Generar horario en formato HTML
    html_schedule = """
    <table border="1">
        <thead>
            <tr>
                <th>Actividad</th>
                <th>Horario</th>
            </tr>
        </thead>
        <tbody>
    """

    for actividad, hora in horario.items():
        html_schedule += f"""
            <tr>
                <td>{actividad}</td>
                <td>{hora}</td>
            </tr>
        """

    html_schedule += """
        </tbody>
    </table>
    """

    return html_schedule

