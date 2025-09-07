# %% Librerías
# from Modulos import main

# %% Programa principal
# main()


#Librerías
try:
    from Modulos import main
    #Programa principal
    main()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    input("Presiona Enter para cerrar...")