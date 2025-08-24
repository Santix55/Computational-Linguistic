import re

def main():
    with open('entrada_tokenizador_2023.txt', 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        tokens = tokenizar(texto)

        with open('ejemplo_salida_tokenizador_2023.txt', 'w', encoding='utf-8') as archivo_salida:
            for token in tokens:
                archivo_salida.write(token + '\n')
                print(token)
        

def tokenizar(texto):

    patron = re.compile(r"""
        \w\w?[ ]de[ ]               # Fecha formato hablado               
            (?:enero
                |febrero
                |marzo
                |mayo
                |junio
                |julio
                |agosto
                |septiembre
                |octubre
                |noviembre
                |diciembre
            )(?:[ ]de[ ]\w+)?
        |[A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]+  # Nombre    # nombre
            [ ][A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]+        # apellido1
            [A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]+           # apellido2
        |https?://(?:\w+\.)+\w\w+   # Link      # protocolo y dominio
            (?:[\w\.-/?%&=])*                   # recurso
        |\w+@(?:\w+\.)+\w\w?        # Correos
        |[#@]\w+                    # Hashtags y menciones de Twitter
        |(?:[A-ZÑ][A-ZÑ]?\.)+       # Sigla     # una o dos mayúsculas repetidas acabadas es un punto
            (?:[A-ZÑ][A-ZÑ]?)?\.?               # una o dos mayúsculas acabadas que pueden acabar en punto
        |Sr\.|Sra\.|Dr\.|Dra.|Dª|Dº # Tratamientos
        |\d?\d[/-]\d?\d[/-]\d+      # Fechas
        |\d?\d[:]\d\d               # Horas
        |\d+(?:[\.,]\d+)?           # Números con decimales
        |[()\.,‘“?¿!¡…;:]           # Símbolos de puntuación
        |\w+                        # Palabras
        |[\U0001F600-\U0001F64F]    # Emoticonos
        |[\U0001F300-\U0001F5FF]    # Símbolos y pictogramas
        |[\U0001F680-\U0001F6FF]    # Transporte y símbolos de mapas
        |[\U0001F1E0-\U0001F1FF]    # Banderas
    """, re.VERBOSE | re.UNICODE)
    tokens = re.findall(patron, texto)

    return tokens


if __name__ == "__main__":
    main()
