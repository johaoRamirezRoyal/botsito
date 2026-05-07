from setup import inputFormIntersection
from data import devolver_correos, eliminar_correos_enviados

def main():
    numero_correos = 0
    correos = devolver_correos()
    correos_enviado = []
    for correo in correos:
        if numero_correos >= 10:
            print("Se han enviado 10 correos, deteniendo el bot.")
            break
        inputFormIntersection(correo)
        correos_enviado.append(correo)
        numero_correos += 1
        print(f"✅ Correo enviado: {correo} | Total enviados: {numero_correos}")
        correos_restantes = eliminar_correos_enviados(correos_enviado)
        print(f"Correos restantes por enviar: {len(correos_restantes)}")
main()