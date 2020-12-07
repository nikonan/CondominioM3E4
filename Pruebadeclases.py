class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.cedula), self.nombre, 
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"

persona1 = Persona("13458796-K", "Leonardo", "Caballero", "M")
persona2 = Persona("23569874-1", "Ana", "Poleo", "F")


print (persona1.nombre, persona1.apellido)
print (persona1.getGenero(persona1.sexo))


print ("\n" + str(persona1) + "\n")

print ("")
print ("-------------------------------------------")
print("#### ---------------------------------- ####")
print ("-------------------------------------------")
print ("")

class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ', '.join(self.tareas)

supervisor1 = Supervisor("16987456-6", "Jen", "Paz", "D", "Chivo")

print ("\n" + str(supervisor1) + "\n")


print ("")
print ("-------------------------------------------")
print("#### ---------------------------------- ####")
print ("-------------------------------------------")
print ("")

print ("- Cedula de identidad: {0}.".format(supervisor1.cedula))
print ("- Nombre completo: {0} {1}.".format(
	supervisor1.nombre, supervisor1.apellido))
print ("- Genero: {0}.".format(
	supervisor1.getGenero(supervisor1.sexo)))
print ("- {0} {1} dijo: {2}".format(
	supervisor1.nombre, supervisor1.apellido, 
	supervisor1.hablar("A trabajar Leonardo!!!".upper())))

print ("- Rol: {0}.".format(supervisor1.rol))
print ("- N. Tareas: {0}.".format(supervisor1.consulta_tareas()))

print ("""\nHola, Soy el {0} {1} {2}, mi cédula es '{3}', 
mi genero '{4}', con el rol '{5}' y mis tareas
asignadas '{6}'.""".format(
    supervisor1.__doc__[26:37].lower(),
    supervisor1.nombre, supervisor1.apellido, supervisor1.cedula, 
    supervisor1.getGenero(supervisor1.sexo), supervisor1.rol,
    supervisor1.consulta_tareas()))