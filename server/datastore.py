class DataStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value
        return "OK"
    
    def get(self, key):
        return self.store.get(key, "(nil)")
    
    def delete(self, key):
        if key in self.store:
            del self.store[key]
            return "OK"
        return "Key not found"