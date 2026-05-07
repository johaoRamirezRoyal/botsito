import keyboard
from setup import inputFormIntersection

def iniciar_bot():
    print("Inicializando el botsito... ")
    #Aquí debes poner la función o funciones no se

    keyboard.add_hotkey('ctrl+shift+b', inputFormIntersection("abiabuchaibe@royalschool.edu.co"))

    print("Bot listo! Presiona Ctrl+Shift+B para activar el bot.")

    keyboard.wait('esc')

iniciar_bot()