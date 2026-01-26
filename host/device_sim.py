import random

def handle(cmd):
    cmd = cmd.strip()

    if cmd == "PING":
        return "OK"
    
    if cmd == "TOGGLE":
        latency = random.randint(30, 45)
        return f"LATENCY_US {latency}"
    

    return "ERR"