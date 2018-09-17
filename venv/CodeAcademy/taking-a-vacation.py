#function genaamd host_cost met als value nights
def hotel_cost(nights):
    #als er een getal in nights word ingevoerd dan moet dan maal 140
    return 140 * (nights)

#function plan_ride_cost die een aantal opties heeft
def plane_ride_cost(city):
    #we kunnen een aantal keuzes maken hier, die we dan checken met een string voor welke stad
    if city == "Charlotte":
        #return voor de verschillende steden een andere koste plaatje
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

#funtion voor rent_car_cost.
def rental_car_cost(days):
    #omdat we hier optie hebben voor een bepaalde waarde nemen we een extra variable cost(totaal)
    cost = days *40
    #hier is de keuze als er 7 of meer dagen word gekozen dan totaal - 50
    if days >= 7:
        cost -= 50
        #hier is de keuze 3 of meer
    elif days >= 3:
        cost -= 20
    return cost

#hier combineren we alle functions aan elkaar met een aanpassing in de hotel dagen. dan doen we omdat we
#de hotel per nacht rekent en wij hotel en auto kosten aan elkaar koppelen. we halen er gewoon een dag af
#hiermee lossen we het probleem op
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city) + spending_money


print(trip_cost("Los Angeles",5,600))