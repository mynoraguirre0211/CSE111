def main():

    stodo = float(input("Please enter the starting odometer value in miles: "))
    enodo = float(input("Please enter the ending odometer value in miles: "))
    fuel = float(input("Amount of fuel gallons: "))

    gallons_miles = miles_per_gallon(stodo, enodo, fuel)
    litters = lp100k_from_mpg(gallons_miles)

    print(f"the gallons per miles are of: {gallons_miles:.2f}")
    print(f"the kilometers per gallon are: {litters:.2f}")

def miles_per_gallon(stodo, enodo, fuel):
    #here we are going to define the fomula of miles per gallon

    gallons_miles = (enodo - stodo) / fuel

    return gallons_miles

def lp100k_from_mpg (gallons_miles):
    #here we are going to convert the miles to kilometeres

    litters = 235.215 / gallons_miles

    return litters

main()