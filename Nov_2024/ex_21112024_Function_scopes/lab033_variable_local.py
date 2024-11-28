#where ever there's same variable name, local has more preference
public_toilet = "PB"


def home():
    private_toilet = "PT"
    public_toilet = "LPB"  #variable value is LPB for this function
    print(private_toilet)
    print(public_toilet)


home()


def rail_station():
    print(public_toilet) #this will print global variable


rail_station()
