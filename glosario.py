"""
IF009 - Laboratorio de Programación y Lenguajes (UNTDF)
TP 0: Git & GitHub Flow
Script base para el Glosario Colaborativo
"""


def mostrar_bienvenida():
    print("=" * 40)
    print("  GLOSARIO COLABORATIVO - LPyL")
    print("=" * 40)
    print("Semanas 1-2: Introducción a Git, HTML, CSS y Python")
    print("-" * 40)


def glosario_inicial():
    """
    Diccionario con términos base.
    Los alumnos deben agregar nuevas funciones para extender este glosario.
    """
    terminos = {
        "HTML": "Lenguaje de marcado para la creación de páginas web.",
        "CSS": "Lenguaje de hojas de estilo para describir la presentación de un documento HTML.",
        "Python": "Lenguaje de programación de alto nivel, interpretado y multiparadigma.",
        "Git": "Sistema de control de versiones distribuido, diseñado para manejar proyectos pequeños a muy grandes con rapidez y eficiencia.",
        "GitHub": "Plataforma de alojamiento para proyectos de desarrollo de software que utiliza Git.",
    }

    for termino, definicion in terminos.items():
        print(f"-> {termino}: {definicion}")


# --- TAREA PARA EL ALUMNO ---
# Instrucciones:
# 1. Crea una rama 'feature-tu-termino'
# 2. Crea una función nueva siguiendo el ejemplo de abajo
# 3. Llámala dentro del bloque 'if __name__ == "__main__":'


def agregar_definicion_alumno():
    """
    EJEMPLO: El alumno debe renombrar esta función y completar su término.
    """
    termino = "ORM"  # Reemplazar con el término asignado o elegido
    definicion = "Object-Relational Mapping. Técnica para convertir datos entre sistemas incompatibles usando OOP."
    print(f"[NUEVO] {termino}: {definicion}")

def definicion_orm_django():
    # 2. Definimos el término técnico
    termino = "ORM (Object-Relational Mapping)"
    explicacion = "Es una técnica que permite interactuar con la base de datos usando objetos de Python en lugar de escribir SQL crudo."
    
    print(f"--- {termino} ---")
    print(explicacion)


if __name__ == "__main__":
    mostrar_bienvenida()
    glosario_inicial()
    definicion_orm_django()

    # El alumno debe agregar la llamada a su función aquí:
    # agregar_definicion_alumno()
