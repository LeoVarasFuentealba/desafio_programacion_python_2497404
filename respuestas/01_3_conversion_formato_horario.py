def hour_format_conversor(hora):
    horas = hora[0] + hora[1]
    minutos = hora[3] + hora[4]
    horario = hora[-2:].upper()

    if horario == 'PM':
        if horas != '12':
            horas = str(int(horas) + 12)
    else:
        if horas == '12':
            horas = '00'
    
    horas = horas + ':' + minutos
    
    return horas
    
print(hour_format_conversor('01:40PM'))
