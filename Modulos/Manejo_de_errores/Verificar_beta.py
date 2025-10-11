def verificar_beta(beta):
    try:
        beta = float(beta)
        return beta, True

    except ValueError:
        print('🛑 El valor de β debe ser un número. Intente de nuevo.')
        return 'menu', False

if __name__ == '__main__':
    verificar_beta()