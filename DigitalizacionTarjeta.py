import questionary
from rich import print
from rich.console import Console
from rich.table import Table   
continuar = "y"

#definimos la table

table = Table(title="HISTORIAL")

table.add_column("Revisado", style="cyan", no_wrap=True)
table.add_column("Sustituído", style="magenta")
table.add_column("Parte", justify="center", style="green")
table.add_column("Proximo Cambio", justify="center")

console = Console()

partes = ["Aceite Motor", "Aceite caja cambios", "Aceite diferencial", "Líquido anticongelante",
          "Líquido de frenos", "líquido servodirección", "Filtro Aceite",
          "Filtro de aire", "Filtro de combustible", "Bujías",
          "Correas", "Pastillas de frenos", "Nivel batería", "Neumáticos"]

while (continuar == "y"):

    print("Dime la fecha (Formtato: dd-mm-aaaa):")
    fecha = str(input(">> "))

    print("¿Kilometraje?")
    kilometraje = int(input(">> "))

    print("¿Tipo de Aceite?")
    aceite = str(input(">> "))


    for parte in partes:
        print(parte)

        print("Revisado: (Cualquier tecla: Sí, Enter: No)")
        revisado = bool(input(">> "))
        print("Sustituido: (Cualquier tecla: Sí, Enter: No)")
        sustituido = bool(input(">> "))
        print("¿Cuántos kilómetros para el próximo cambio?")
        kil_prox_camb = int(input(">> "))

        console.print(f"FECHA: {fecha}, KILOMETRAJE: {kilometraje}", justify = "center")
        console.print(f"ACEITE DE MOTOR: {aceite}", justify= "center")
        table.add_row(f"{revisado}", f"{sustituido}", f"{parte}", f"{kil_prox_camb}")
        console.print(table, justify="center")    



    continuar = str(input("Continuar? y/n: "))
