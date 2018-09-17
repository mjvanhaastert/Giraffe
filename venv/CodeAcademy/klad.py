#function genaamd host_cost met als value nights
def hotel_cost(nights):
    #als er een getal in nights word ingevoerd dan moet dan maal 140
    return 140 * nights

#function plan_ride_cost die een aantal opties heeft
def plane_ride_cost(city):
    #we kunnen een aantal keuzes maken hier, die we dan checken met een string voor welke stad
    if city == "Charlotte":
        #return voor de verschillende steden een andere koste
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    cost = days *40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


print(rental_car_cost(3))