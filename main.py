import sys


class Cliente:
    
    intentos_ingreso= 5
    
    def __init__(self,id_cliente,nombre,pais,ciudad,tipo):
        self.id_cliente=id_cliente
        self.nombre=nombre
        self.pais=pais
        self.ciudad=ciudad
        self.tipo=tipo
        
    def __login__(self):
        for _ in range(Cliente.intentos_ingreso):
            if input("Ingrese su codigo de cliente: ") == self.id_cliente:
                return (f"Bienvenido : {self.nombre}") 
                break
            else:
                print ("El codigo no es correcto")

    def __ubicacion__(self, id_cliente, pais):
        for _ in range (paises):
            if pais=="Argentina" and ciudad=="Buenos Aires":
                print ("Cliente CABA")
            elif pais=="Argentina" and ciudad!="Buenos Aires":
                print ("Cliente Provincias")
            else:
                print ("Cliente resto_del_mundo")
            

class CABA (Cliente):
    
    def __envio__(self):
        print ("El envio es gratuito en CABA")
    
class Provincias (Cliente):
    
    def __contacto__(self):
        print ("Contactenos por nuestra oficina en Cordoba")

class resto_del_mundo (Cliente):
    
    def __aduanas__(self):
        print("Entienda de que cada pais tiene sus propios Drechos de Importacion")
        


cliente_uno= ("000001", "Empresa_1", "Argentina","Buenos Aires","Empresa")
cliente_dos= ("000002", "Indiv_1", "Argentina","Cordoba","Individual")
cliente_tres= ("000003", "ONG_1", "Francia","Paris","ONG")
cliente_cuatro= ("000004", "Empresa_2", "USA","Washington","Empresa")