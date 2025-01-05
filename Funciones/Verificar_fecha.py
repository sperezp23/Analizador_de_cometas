from datetime import datetime, date

def verificar_fecha(fecha_inicial):
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d").date()
    dias = (date.today() - fecha_inicial_dt).days

    if dias >= 0:
        return True
    
    else:
        print(f'🛑 La fecha ingresada: {fecha_inicial}, Sobrepasa la fecha actual.')
        return False

if __name__ == '__main__':
    verificar_fecha()