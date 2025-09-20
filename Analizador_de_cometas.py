# %% Librerías
# from Modulos import main

# %% Programa principal
# main()

import traceback
from Modulos import main

#Librerías
try:
    main()

except Exception as e:

    print(f"Error: {e}")
    traceback.print_exc()
    input("Presiona Enter para cerrar...")