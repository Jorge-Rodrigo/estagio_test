import random

def switch_lights(switches):
    
    rooms = {
        "Cozinha": False,
        "Quarto": False,
        "Sala de Estar": False
    }
    for i, switch in enumerate(switches):
        if switch:
            if i == 0:
                rooms["Cozinha"] = True
            elif i == 1:
                rooms["Quarto"] = True
            elif i == 2:
                rooms["Sala de Estar"] = True
    
    return rooms

def main():
    for _ in range(2):
        switches = [random.choice([True, False]) for _ in range(3)]
        for j, switch in enumerate(switches):
            if switch:
                print(f"Interruptor {j+1} ligado.")
        rooms = switch_lights(switches)
        print("Salas com lâmpadas acesas:")
        for room, state in rooms.items():
            if state:
                print(f"- {room}")

main()