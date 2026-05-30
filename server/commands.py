from datastore import DataStore

datastore = DataStore()


def execute(command):
    parts = command.strip().split()

    if not parts:
        return "Invalid command"
    
    cmd = parts[0].upper()

    if cmd == "PING":
        return "PONG"
    
    elif cmd == "SET":
        if len(parts) < 3:
            return "Usage: SET key value"
        
        key = parts[1]
        value = " ".join(parts[2:])

        return datastore.set(key, value)
    
    elif cmd == "GET":
        if len(parts) != 2:
            return "Usage: GET key"
        
        return datastore.get(parts[1])
    
    elif cmd == "DEL":
        if len(parts) != 2:
            return "Usage: DEL key"
        
        return datastore.delete(parts[1])
    
    return "Unknown command"