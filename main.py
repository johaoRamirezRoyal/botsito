from setup import inputFormIntersection
from data import devolver_correos

def main():
    numero_correos = 0
    correos = devolver_correos()

    for correo in correos:
        if numero_correos >= 1:
            print("Se han enviado 10 correos, deteniendo el bot.")
            break
        inputFormIntersection(correo)
        numero_correos += 1
        print(f"✅ Correo enviado: {correo} | Total enviados: {numero_correos}")

main()