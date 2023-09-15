def obtener_opcion():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Introducir puntos de evaluación y comentarios')
        print('2: Comprobar los resultados hasta ahora.')
        print('3: Terminar.')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            
            if 1 <= num <= 3:
                return num
            else:
                print('Por favor, introduzca una opción válida (1, 2 o 3)')
        else:
            print('Por favor, introduzca una opción válida (1, 2 o 3)')

def introducir_puntos_comentarios():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if 1 <= point <= 5:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{post}\n')
                file_pc.close()
                break
            else:
                print('Por favor, introduzca un valor entre 1 y 5')
        else:
            print('Introduzca los puntos de valoración como números')

def comprobar_resultados():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()

def main():
    while True:
        opcion = obtener_opcion()
        
        if opcion == 1:
            introducir_puntos_comentarios()
        elif opcion == 2:
            comprobar_resultados()
        elif opcion == 3:
            print('Terminación.')
            break

if __name__ == "__main__":
    main()
