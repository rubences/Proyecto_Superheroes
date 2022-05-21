from Superheroes import *
from organizaciones import Organizacion


firstNames = {"A":"Captain", "B":"Turbo", "C":"Galactic", "D":"The", "E":"Aqua", "F":"Fire",
"G":"Iron", "H":"Super", "I":"Green", "J":"Phantom", "K":"Dark", "L":"Ghost", "M":"Professor",
"N":"Atomic", "O":"Rock", "P":"Omega", "Q":"Rocket", "R":"Shadow", "S":"Agent", "T":"Silver",
"U":"Wild", "V":"Wolf", "W":"Ultra", "X":"Wonder", "Y":"Doctor", "Z":"Star"}

lastNames = {"A":"X", "B":"Shield", "C":"Machine", "D":"Justice", "E":"Beast", "F":"Wing",
"G":"Arrow", "H":"Skull","I":"Blade", "J":"Bolt", "K":"Cobra", "L":"Blaze",
"M":"Soldier", "N":"Strike", "O":"Falcon", "P":"Fang", "Q":"King", "R":"Surfer",
"S":"Bot", "T":"Guard", "U":"Thing", "V":"Claw", "W":"Brain", "X":"Master", "Y":"Power", "Z":"Storm"}

def main():

    #elegir escenario
    escenario = input("Elija un escenario de entre los siguientes: sanctum_sanctorum/ stark_tower/ xavier_school: ")

    escenario = Escenarios.from_str(escenario)

    #crear superheroes

    nombrelist = list(firstNames.values())
    apellidolist = list(lastNames.values())
    tipolist = ["HUMANO", "NOHUMANO"]
    superlist = []

    list_costes = []
    for i in range (0,80):
        x = random.randint(0, len(nombrelist)-1)
        y = random.randint(0, len(apellidolist)-1)
        a = tipolist[random.randint(0,1)]

        tipo = Superheroe_Type.from_str(a)
        nombre = nombrelist[x] + " " + apellidolist[y]

        superlist.append(Superheroes(nombre, nombre, tipo, escenario))
        list_costes.append(superlist[i].get_coste())

    # crear organizaciones

    nombre_org = ["A - Force", "Avengers", "Mercs for Money", "League of Realms", "Strange Academy", "X-Men"]
    organizaciones = []
    for i in range(0, len(nombre_org)):
        organizaciones.append(Organizacion(nombre_org[i], superlist[10*i:10*(i+1)]))
    organizaciones.append(Organizacion("Independientes", superlist[10*len(nombre_org):]))

    # mostrar superheroes

    print("Estos son los superheres a elegir y sus costes: ")
    for organizacion in organizaciones:
        print(organizacion.get_nombre() + ": ")
        print(organizacion.__str__())

    #elegirlos

    monedas = [escenario.get_monedas(),escenario.get_monedas()]
    sup_jug = []
    listsup_elejidos = []
    list_ident =[]

    print("Cada jugadore dispone de " + str(monedas) + " con las que poder comprar un maximo de " + str(escenario.get_miembros_ekip()) + " superheroes.")
    print(min(list_costes))

    for n in range(0,2):
        while len(sup_jug) < escenario.get_miembros_ekip() and monedas[n] >= min(list_costes):
            num = int(input("Jugador " + str(n+1) + " elija un superheore de la lista por su número: "))
            if num not in list_ident:
                sup_jug.append(superlist[num])
                list_ident.append(num)
                monedas[n] -= superlist[num].get_coste()
            else:
                print("Ese superheroe ya ha sido elejido")

        listsup_elejidos.append(sup_jug)

        print("Estos son los superheores elejidos ")

        for superheroe in sup_jug:
            print(str(
                superheroe.get_identificador()) + ". Alias: " + superheroe.get_alias() + ", Tipo:" + superheroe.get_tipo().name + ", Coste:" + str(
                superheroe.get_coste()) + ", Energia:" + str(superheroe.get_energia()) + "\n")

        sup_jug = []

    #elegir golpes

    mov_list = []

    mov_punetazo = Movimientos_General("puñetazo", Movimiento_Type.ATAQUE, random.randint(0,15))
    mov_list.append(mov_punetazo)
    mov_navajazo = Movimientos_General("navajazo", Movimiento_Type.ATAQUE, random.randint(0, 20))
    mov_list.append(mov_navajazo)
    mov_escudo = Movimientos_General("Escudo", Movimiento_Type.DEFENSA, random.randint(0, 5))
    mov_list.append(mov_escudo)
    mov_abrazo_del_oso = Movimientos_General("Abrazo del oso", Movimiento_Type.DEFENSA, random.randint(0, 12))
    mov_list.append(mov_abrazo_del_oso)

    for i in range(0,2):
        for superheroe in listsup_elejidos[i]:
            list_mov = [int(x) for x in input("Los movimientos son: [0. puñetazo| 1. navajazo| 2. escudo| 3. abrazo del oso]. Elija " + str(escenario.get_movimientos()) + " movimientos, en base a su ID y separados por comas, para el superheroe " + superheroe.get_alias() + " ").split(",")]
            # list_mov = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] -> codigo de prueba 
            list_mov_esp = [Movimientos_Especifico(mov_list[list_mov[i]].get_nombre(), mov_list[list_mov[i]].get_tipo(), mov_list[list_mov[i]].get_daño(), superheroe) for i in range(0, min(escenario.get_movimientos(), len(list_mov)))]
            superheroe.set_movimientos(list_mov_esp)
            for mov in list_mov_esp:
                print(mov.get_nombre() + " " + mov.get_tipo().name + " daño: " + str(mov.get_daño()) + "\n")

    #pelea hasta que uno muera -> elegir otro

    list_campobatalla = [None, None]
    list_organizaciones = [Organizacion("Jugador1", listsup_elejidos[0]), Organizacion("Jugador2", listsup_elejidos[1])]
    movement = 0
    while list_organizaciones[0].is_undefeated() and list_organizaciones[1].is_undefeated():
        for i in range(0,len(list_campobatalla)):
            if not list_campobatalla[i] or not list_campobatalla[i].is_vivo():
                print("Jugador " + str(i+1) + " su superheroe ha sido derrotado, estos son los que le quedan")
                undefeated = list_organizaciones[i].get_super_undefeated()
                for j in range(0, len(undefeated)):
                    print(str(j) + ". Alias: " + undefeated[j].get_alias() + "\n")
                suplente_sup = int(input("Elija un nuevo superheroe: "))
                list_campobatalla[i] = undefeated[suplente_sup]

        while list_campobatalla[0].is_vivo() and list_campobatalla[1].is_vivo():
            list_campobatalla[0].fight_attack(list_campobatalla[1], movement)
            list_campobatalla[1].fight_attack(list_campobatalla[0], movement)
            movement = 0 if movement == escenario.get_movimientos() - 1 else movement + 1
            print("Esta es la energia del jugador 1: "+str(list_campobatalla[0].get_energia())+ " y esta la del jugador 2: "+str(list_campobatalla[1].get_energia()))

    if list_organizaciones[0].is_undefeated():
        print("¡Ha ganado el jugador 1!")

    elif list_organizaciones[1].is_undefeated():
        print("¡Ha ganado el jugador 2!")

    else:
        print("Ha habido un empate")


if __name__ == "__main__":
    main()