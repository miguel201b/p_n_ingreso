def hora_a_minutos(hora_str):
    """Convierte una cadena de hora en minutos totales."""
    horas, minutos = map(int, hora_str.split(":"))
    return horas * 60 + minutos

def generar_horario(letra):
    letra = letra.lower()

    horario = {
        "7:00": ["", "", "", "", "", "", ""],
        "7:30": ["", "", "", "", "", "", ""],
        "8:00": ["", "", "", "", "", "", ""],
        "8:30": ["", "", "", "", "", "", ""],
        "9:00": ["", "", "", "", "", "", ""],
        "9:30": ["", "", "", "", "", "", ""],
        "10:00": ["", "", "", "", "", "", ""],
        "10:30": ["", "", "", "", "", "", ""],
        "11:00": ["", "", "", "", "", "", ""],
        "11:30": ["", "", "", "", "", "", ""],
        "12:00": ["", "", "", "", "", "", ""],
        "12:30": ["", "", "", "", "", "", ""],
        "13:00": ["", "", "", "", "", "", ""],
        "13:30": ["", "", "", "", "", "", ""],
        "14:00": ["", "", "", "", "", "", ""],
        "14:30": ["", "", "", "", "", "", ""],
        "15:00": ["", "", "", "", "", "", ""],
        "15:30": ["", "", "", "", "", "", ""],
        "16:00": ["", "", "", "", "", "", ""],
        "16:30": ["", "", "", "", "", "", ""],
        "17:00": ["", "", "", "", "", "", ""],
        "17:30": ["", "", "", "", "", "", ""],
        "18:00": ["", "", "", "", "", "", ""],
        "18:30": ["", "", "", "", "", "", ""],
    }

    # Bienvenida
    if letra in "abc":
        horario["10:00"][0] = "CEREMONIA DE BIENVENIDA"
    elif letra in "defg":
        horario["12:00"][0] = "CEREMONIA DE BIENVENIDA"
    elif letra in "hijkl":
        horario["14:00"][0] = "CEREMONIA DE BIENVENIDA"
    elif letra in "mno":
        horario["10:00"][1] = "CEREMONIA DE BIENVENIDA"
    elif letra in "pqr":
        horario["12:00"][1] = "CEREMONIA DE BIENVENIDA"
    else:
        horario["14:00"][1] = "CEREMONIA DE BIENVENIDA"
    
    # EMA
    if letra in "ab":
        horario["12:00"][4] = "EMA"
    elif letra == "c":
        horario["9:00"][4] = "EMA"
    elif letra in "def":
        horario["16:30"][4] = "EMA"
    elif letra == "g":
        horario["12:00"][5] = "EMA"
    elif letra in "hijkl":
        horario["9:00"][5] = "EMA"
    elif letra == "m":
        horario["16:30"][5] = "EMA"
    elif letra in "nopq":
        horario["12:00"][6] = "EMA"
    elif letra == "r":
        horario["9:00"][6] = "EMA"
    else:
        horario["16:30"][6] = "EMA"

    # INSCRIPCION
    if letra in "ab":
        horario["10:30"][4] = "INSCRIPCION"
    elif letra == "c":
        horario["12:00"][4] = "INSCRIPCION"
    elif letra in "def":
        horario["15:00"][4] = "INSCRIPCION"
    elif letra == "g":
        horario["10:30"][5] = "INSCRIPCION"
    elif letra in "hijkl":
        horario["12:00"][5] = "INSCRIPCION"
    elif letra in "m":
        horario["15:00"][5] = "INSCRIPCION"
    elif letra in "nopq":
        horario["10:30"][6] = "INSCRIPCION"
    elif letra == "r":
        horario["12:00"][6] = "INSCRIPCION"
    else:
        horario["15:00"][6] = "INSCRIPCION"

    # EDI
    if letra in "abcdef":
        horario["13:00"][5] = "EDI"
        
    elif letra in "ghijklm":
        horario["15:00"][6] = "EDI"
        
    else:
        horario["7:00"][5] = "EDI"
        

    # CURSO DE GÉNERO
    if letra in "abcdef":
        horario["9:00"][2] = "CURSO DE GÉNERO"
        horario["9:00"][3] = "CURSO DE GÉNERO"
        horario["9:00"][5] = "CURSO DE GÉNERO"
        horario["9:00"][6] = "CURSO DE GÉNERO"
    elif letra in "ghijklm":
        horario["11:00"][2] = "CURSO DE GÉNERO"
        horario["11:00"][3] = "CURSO DE GÉNERO"
        horario["11:00"][4] = "CURSO DE GÉNERO"
        horario["11:00"][6] = "CURSO DE GÉNERO"
    elif letra in "nopqrstuvwxyz":
        horario["13:00"][2] = "CURSO DE GÉNERO"
        horario["13:00"][3] = "CURSO DE GÉNERO"
        horario["13:00"][4] = "CURSO DE GÉNERO"
        horario["13:00"][5] = "CURSO DE GÉNERO"

    # RECORRIDOS
    if letra in "abc":
        horario["11:00"][2] = "RECORRIDO"
    elif letra in "def":
        horario["11:00"][3] = "RECORRIDO"
    elif letra == "g":
        horario["13:00"][2] = "RECORRIDO"
    elif letra in "hijklm":
        horario["13:00"][3] = "RECORRIDO"
    elif letra in "nopqr":
        horario["15:00"][2] = "RECORRIDO"
    elif letra in "nopqrstuvwxyz":
        horario["15:00"][3] = "RECORRIDO"
    return horario

def primera_hora_activa(horario):
    for hora, actividades in horario.items():
        if any(act for act in actividades if act):
            return hora
    return None

def quitar_horas_anteriores(horario, hora_inicio):
    horas_a_eliminar = []
    for hora in horario:
        if hora_a_minutos(hora) < hora_a_minutos(hora_inicio):
            horas_a_eliminar.append(hora)
    for hora in horas_a_eliminar:
        del horario[hora]

    return horario

def obtener_horario(letra):
    horario = generar_horario(letra)
    hora_inicio = primera_hora_activa(horario)
    horario = quitar_horas_anteriores(horario, hora_inicio)
    return horario,hora_inicio
