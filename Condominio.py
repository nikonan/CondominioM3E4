class Condominio(object):
    def __init__(self, direccion, lista_administrador, lista_guardias,
                num_unidades_habitacionales, lista_unidades, cuenta_corriente, Parque_automotriz, 
                Zonas_comunes, Mantenimiento, Gastos_administrativos):
        self.direccion = direccion
        self.lista_administrador = lista_administrador
        self.lista_guardias = lista_guardias
        self.num_unidades_habitacionales = num_unidades_habitacionales
        self.lista_unidades = lista_unidades
        self.cuenta_corriente = cuenta_corriente
        self.Parque_automotriz = Parque_automotriz
        self.Zonas_comunes = Zonas_comunes
        self.Mantenimiento = Mantenimiento
        self.Gastos_administrativos = Gastos_administrativos

    def get_direccion (self):
        print (self.direccion)

    def set_direccion (self):
        print (self.direccion)
    
    def set_administrador (self):
        print (self.lista_administrador)
    
    def get_administrador (self):
        print (self.lista_administrador)

    def add_guardia (self):
        print  (self.lista_guardias)
    
    def del_guardia (self):
        print (self.lista_guardias)

    def get_guardia (self):
        print (self.lista_guardias)
    
    def get_unidades ( self):
        print (self.lista_unidades)

    print ("")
    print ("-------------------------------------------")
    print("#### Hasta aca estan los metodos pedidos ####")
    print ("-------------------------------------------")
    print ("")

    def rotacion_guardias (self):
        print (self.lista_guardias)
    
    def cobro_administracion (self):
        print (self.lista_unidades)

    def control_entrada (self):
        print (self.lista_guardias)

    def corte_prado (self):
        print (self.Mantenimiento)

condominio1= Condominio ("k20", "1", "qqq", "eeee","ggg","hhhh","jjjj", "cccc", "bbb", "nnnn")
condominio1.get_direccion()


print ("")
print ("-------------------------------------------")
print("#### Hasta aca esta la clase Condominio ####")
print ("-------------------------------------------")
print ("")



class Guardias(Condominio):
    def Responsabilidades(self):
        
       print (("Patrullar:"), (self.Zonas_comunes),
       ('\nUsando'), (self.Parque_automotriz), ('\nReportar Novedades a'),(self.lista_administrador))

SeguridadABC = Guardias ('', 'Administrador de Turno', '', '', '', '', "4 Motos, 2 Camionetas", ("Perimetro",
"Entrada", "Cenderos", "Zonas Recreativas", "Parqueaderos"), ' ', ' ')
SeguridadABC.Responsabilidades()


print ("")
print ("-------------------------------------------")
print ("#### Hasta aca llega la clase Guardias ####")
print ("-------------------------------------------")
print ("")

class UnidadHabitacional(Condominio):
    def UnidadesCondominio(self):
        print (("Condominio Los Alamos Cuenta con"),(self,Zonas_comunes), ("Seguridad 24 horas"), 
        ("Nos ubicamos en"), (self.direccion), ("Zona privilegiada para su tranquilidad"))


