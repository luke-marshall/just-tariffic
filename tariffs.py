# This may be my last correspondence, as Peter Dutton may be PM by this afternoon and I will be officially moved to the socialist paradise that is New Zealand


# =====================================
#  THE INTERFACE
# =====================================


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
    
    # My suggestion is to extend the get_price() function to handle those extensions when they come up, but make all the additional variables optional.
    # So a 'voltage peak' tariff would have a function that looks like:
    #   def get_price(time, peak_voltage=0) 
    # A user could still use this function without having to know about peak voltage - importing the peak tariff wouldnt break anyones code. 



# =====================================
#  USING IT
# =====================================

# Here's a simple example
# Create a tariff object.
my_tariff = Tariff()
# Build a scenario - time and amount of energy needed.
time = datetime.datetime(1,2,2018,6)
kWh = 6
# Calculate the charge.
my_charge = kWh * my_tariff.get_price(time)

