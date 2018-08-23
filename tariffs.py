

# This is an interface
# It's a definition of how an object should be written, so that people can interact with it in a standard way.
# It features the names of functions, with no implementation (ie. it doesn't work, its jus the commands you'd use)
class Tariff():
    
    # In general, it's going to need to have the time to tell you what tariff is available at a given time. 
    # But in other implementations, we might need some additional ones
    # My suggestions for extensions: 
    #       -Volume kWh
    #       -Peak Voltage / Power
    #       -Quality
    def get_price(time):
        pass #this just lets you know the function does nothing right now.