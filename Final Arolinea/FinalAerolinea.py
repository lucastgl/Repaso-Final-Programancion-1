# Una aerolínea de bajo costo cobra un adicional sobre el precio del pasaje a quienes deseen elegir asiento. Quienes no lo abonen serán asignados al azar en los asientos que no hayan sido elegidos previamente. Esta información se almacena por cada vuelo en un archivo CSV donde cada registro puede tener dos formatos diferentes:

# Formato 1:
# Nombre del pasajero; fila; asiento

# Formato 2:
# Nombre del pasajero

# El formato 1 se aplica a quienes hayan abonado el adicional por seleccionar ubicación, mientras que el formato 2 se aplica a los demás viajeros.

# El nombre del pasajero se escribe como «Apellido, nombre». La fila oscila entre 1 y N, donde el valor de N depende del modelo de la aeronave. 
# El asiento va desde la A hasta la F en modelos regionales de hasta 32 filas de asientos y desde la A hasta la J en modelos de doble pasillo y 
# largo alcance con más de 32 filas de asientos.

# Se solicita desarrollar un programa que lea un archivo con las características mencionadas y distribuya los asientos respetando las reservas 
# realizadas y asignando al azar los asientos restantes entre los pasajeros que no abonaron el adicional. Mostrar un listado con las asignaciones 
# realizadas ordenado por fila y asiento, e imprimir otro listado con los asientos que hayan quedado libres ordenado por el mismo criterio. 
# También se deberá emitir un listado con las colisiones, si las hubiera. Una colisión ocurre cuando dos pasajeros distintos reservan el mismo asiento. 
# Estos eventos deben ser resueltos por personal de la aerolínea.

# Se suministra un archivo ejemplo llamado Vuelo447.txt. El archivo no está ordenado por ningún criterio particular. 
# El programa debe funcionar con éste o cualquier otro archivo que respete las características indicadas, detectando 
# automáticamente el modelo de avión (simple o doble pasillo) en función de la cantidad de filas de la aeronave y de los asientos reservados. 
# Es decir que si todas las reservas tienen una fila menor o igual a 32 y todos los asientos solo poseen letras de la A a la F, deberá 
# considerarse que se trata de un avión de un solo pasillo y alcance regional.

# final_aerolinea_example.py
import csv
import random
import re
from typing import List, Dict, Tuple

SEAT_LETTERS_SINGLE = ['A','B','C','D','E','F']
SEAT_LETTERS_DOUBLE = ['A','B','C','D','E','F','G','H','I','J']

def parse_line(line: str):
    # Split by ';' preferido, si no hay ';' probar con ','
    if ';' in line:
        parts = [p.strip() for p in line.strip().split(';')]
    else:
        parts = [p.strip() for p in line.strip().split(',')] if ',' in line else [line.strip()]
    # Determinar formato
    if len(parts) >= 3:
        name = parts[0]
        try:
            row = int(parts[1])
            seat = parts[2].upper()
            return ('reserved', name, row, seat)
        except:
            # caída al formato simple si fila/seat no parseable
            return ('unreserved', parts[0])
    else:
        return ('unreserved', parts[0])

def seat_key(row: int, seat: str) -> str:
    return f"{row}{seat}"

def detect_model_and_rows(reservations: List[Tuple[str,int,str]]):
    # reservations: list of tuples (name,row,seat)
    max_row = 0
    letters = set()
    for (_name,row,seat) in reservations:
        max_row = max(max_row, row)
        if seat:
            letters.add(seat.upper())
    # Decide single vs double
    if max_row <= 32 and all((s in SEAT_LETTERS_SINGLE) for s in letters):
        seat_letters = SEAT_LETTERS_SINGLE
    else:
        seat_letters = SEAT_LETTERS_DOUBLE
    # If there were no reservations, default to single-aisle 32 rows (o 1)
    if max_row == 0:
        max_row = 32  # elección razonable; puede cambiarse
    return seat_letters, max_row

def build_all_seats(n_rows: int, seat_letters: List[str]):
    seats = []
    for r in range(1, n_rows+1):
        for s in seat_letters:
            seats.append(seat_key(r,s))
    return seats

def assign_seats(lines: List[str], random_seed: int = None):
    if random_seed is not None:
        random.seed(random_seed)

    reserved_entries = []   # tuples (name,row,seat)
    unpaid = []             # list of names

    for raw in lines:
        raw = raw.strip()
        if not raw: continue
        parsed = parse_line(raw)
        if parsed[0] == 'reserved':
            _, name, row, seat = parsed
            reserved_entries.append((name, row, seat))
        else:
            _, name = parsed
            unpaid.append(name)

    seat_letters, n_rows = detect_model_and_rows(reserved_entries)

    all_seats = set(build_all_seats(n_rows, seat_letters))

    # Build reservation map
    reserved_map: Dict[str, List[str]] = {}  # seat_str -> [names]
    for name,row,seat in reserved_entries:
        key = seat_key(row, seat.upper())
        reserved_map.setdefault(key, []).append(name)

    # detect collisions and definitive reserved single-owner seats
    collisions = {seat: names for seat,names in reserved_map.items() if len(names) > 1}
    reserved_single = {seat: names[0] for seat,names in reserved_map.items() if len(names) == 1}

    # seats unavailable for automatic assignment: reserved_single + collisions
    taken_seats = set(reserved_single.keys())
    collided_seats = set(collisions.keys())

    available_for_assignment = sorted(list(all_seats - taken_seats - collided_seats),
                                      key=lambda s: (int(re.match(r'(\d+)', s).group(1)),
                                                     s[len(re.match(r'(\d+)', s).group(1)):]))
    # Randomly assign to unpaid passengers
    random.shuffle(available_for_assignment)
    assignments = {}  # seat -> name
    assigned_passengers = []
    for i, person in enumerate(unpaid):
        if i >= len(available_for_assignment):
            break
        seat = available_for_assignment[i]
        assignments[seat] = person
        assigned_passengers.append(person)

    # Build final mapping seat->name including reserved_single and automatic assignments
    final_assignments = dict(reserved_single)
    final_assignments.update(assignments)

    # Compute free seats after assignment (exclude seats used, and exclude collided seats)
    used_seats = set(final_assignments.keys())
    free_seats = sorted(list(all_seats - used_seats - collided_seats),
                        key=lambda s: (int(re.match(r'(\d+)', s).group(1)),
                                       s[len(re.match(r'(\d+)', s).group(1)):]))

    # For sorted output of final assignments, create tuples (row,int,seat_letter)
    def sort_key(seat_str):
        m = re.match(r'(\d+)([A-Z]+)', seat_str)
        return (int(m.group(1)), m.group(2))

    sorted_final = sorted(final_assignments.items(), key=lambda kv: sort_key(kv[0]))
    sorted_free = free_seats
    sorted_collisions = sorted(collisions.items(), key=lambda kv: sort_key(kv[0]))

    # passengers who couldn't be assigned due to falta de asientos
    unassigned_passengers = unpaid[len(available_for_assignment):] if len(unpaid) > len(available_for_assignment) else []

    return {
        'assignments': sorted_final,         # list of (seat_str, name)
        'free_seats': sorted_free,           # list of seat_str
        'collisions': sorted_collisions,     # list of (seat_str, [names])
        'unassigned_passengers': unassigned_passengers,
        'model': ('single' if seat_letters == SEAT_LETTERS_SINGLE else 'double'),
        'n_rows': n_rows
    }

# Ejemplo de uso con el contenido del ejemplo:
if __name__ == "__main__":
    sample_lines = [
        "Apellido1, Juan;1;A",
        "Apellido2, Ana",
        "Apellido3, Luis;2;B",
        "Apellido4, Carla",
        "Apellido5, Pedro;1;A",
        "Apellido6, Marta",
        "Apellido7, Jose;3;C",
    ]
    result = assign_seats(sample_lines, random_seed=42)  # semilla para reproducibilidad
    print("Modelo avión:", result['model'], " filas:", result['n_rows'])
    print("\nAsignaciones (fila+letra ; nombre):")
    for seat,name in result['assignments']:
        # seat is like '1A' -> separar fila y letra para imprimir si se desea
        print(f"{seat} ; {name}")
    print("\nAsientos libres:")
    print(", ".join(result['free_seats']))
    print("\nColisiones:")
    for seat,names in result['collisions']:
        print(f"{seat} : {', '.join(names)}")
    if result['unassigned_passengers']:
        print("\nPasajeros sin asiento asignado (no hay asientos suficientes):")
        print(", ".join(result['unassigned_passengers']))