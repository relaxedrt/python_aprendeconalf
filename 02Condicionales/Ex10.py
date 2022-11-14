#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
veg = ["Pimiento", "Tofu"]
nonveg = ["Peperoni", "Jamon", "Salmon"]
elec = input("Como va a querer usted su pizza (Vegetariana/Carnivora)")
if elec == "Vegetariana":
    print(f"----------------INGREDIENTES----------------")
    print(f"1.{veg[0]}................................1€")
    print(f"2.{veg[1]}....................................1€")
    print(f"--Tu pizza llevara tambien tomate y queso.--")
    print(f"El precio base es de 5 euros + ingredientes.")
    ing = int(input("Que ingredientes vas a querer?(1, 2 o 12 si son los dos): "))
    if ing == 1:
        print(f"Ha comprado usted una pizza con tomate, mozzarella y pimiento por 6 euros")
    else:
        if ing == 2:
            print(f"Ha comprado usted una pizza con tomate, mozzarella y tofu por 6 euros")
        else:
            if ing == 12:
                print(f"Ha comprado usted una pizza con tomate, mozzarella, tofu y pimiento por 7 euros")
if elec == "Carnivora":
    print(f"------------------INGREDIENTES------------------")
    print(f"1.{nonveg[0]}....................................1€")
    print(f"2.{nonveg[1]}.......................................1€")
    print(f"3.{nonveg[2]}......................................1€")
    print(f"----Tu pizza llevara tambien tomate y queso.----")
    print(f"--El precio base es de 5 euros + ingredientes.--")
    ing = int(input("Que ingredientes vas a querer?(1, 2, 3, 12, 13, 23, 123): "))
    if ing == 1:
        print(f"Ha comprado usted una pizza con tomate, mozzarella y peperoni por 6 euros")
    else:
        if ing == 2:
            print(f"Ha comprado usted una pizza con tomate, mozzarella y jamon por 6 euros")
        else:
            if ing == 3:
                print(f"Ha comprado usted una pizza con tomate, mozzarella, salmon por 6 euros")
            else:
                if ing == 12:
                    print(f"Ha comprado usted una pizza con tomate, mozzarella, peperoni y jamon por 7 euros")
                else:
                    if ing == 13:
                        print(f"Ha comprado usted una pizza con tomate, mozzarella, peperoni y salmon por 7 euros")
                    else:
                        if ing == 23:
                            print(f"Ha comprado usted una pizza con tomate, mozzarella, jamon y salmon por 7 euros")
                        else:
                            if ing == 123:
                                print(f"Ha comprado usted una pizza con tomate, mozzarella, peperoni, jamon y salmon por 8 euros")


        

