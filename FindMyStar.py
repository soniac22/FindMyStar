import ephem

def get_object_position(object_name, latitude, longitude):
    observer = ephem.Observer()

    observer.lat = str(latitude)
    observer.lon = str(longitude)

    try:
        celestial_object = getattr(ephem, object_name)()
    except AttributeError:
        print(f"Object '{object_name}' not found.")
        return None, None

    # Compute the position of the object
    celestial_object.compute(observer)

    # Get the altitude and azimuth of the object
    altitude = float(celestial_object.alt) * 180 / ephem.pi  # Convert altitude to degrees
    azimuth = float(celestial_object.az) * 180 / ephem.pi    # Convert azimuth to degrees

    return altitude, azimuth


def get_star_position(star_name, latitude, longitude):
    # Create an observer object
    observer = ephem.Observer()

    # Set the observer's location
    observer.lat = str(latitude)
    observer.lon = str(longitude)

    # Create the star object based on its name
    star = ephem.star(star_name)

    # Compute the position of the star
    star.compute(observer)

    # Get the altitude and azimuth of the star
    altitude = float(star.alt) * 180 / ephem.pi  # Convert altitude to degrees
    azimuth = float(star.az) * 180 / ephem.pi    # Convert azimuth to degrees

    return altitude, azimuth

def get_star_constellation(star_name):
    # Create the star object based on its name
    star = ephem.star(star_name)

    star.compute()

    # Get the constellation of the star
    constellation = ephem.constellation(star)

    return constellation[1]  # Return the name of the constellation

def get_constellation(object_name, latitude, longitude):
    # Create an observer object
    observer = ephem.Observer()

    # Set the observer's location
    observer.lat = str(latitude)
    observer.lon = str(longitude)

    # Create the object based on its name
    try:
        celestial_object = getattr(ephem, object_name)()
    except AttributeError:
        print(f"Object '{object_name}' not found.")
        return None

    # Compute the position of the object
    celestial_object.compute(observer)

    # Get the constellation of the object
    constellation = ephem.constellation(celestial_object)

    return constellation




print("To begin please find your longitude and laditute:")


latitude = input("What is your latitude? ")
longitude = input("What is your longitute? ")  


StarOrObject = input("Are you looking for a Star or an Object? ")

print("To begin your search start by facing due north. You will then turn right by the degrees given by the Azimuth, and look up at the angle given by the Altitiude. (If the Altitiute is negative, you will not be able to find your Star/Object)")


if StarOrObject.lower() == "star":
    star_name = input("Enter your Star: ")
    altitude, azimuth = get_star_position(star_name, latitude, longitude)
    if altitude is not None and azimuth is not None:
        print(f"{star_name} Position:")
        print("Altitude:", altitude, "degrees")
        print("Azimuth:", azimuth, "degrees")

    constellation = get_star_constellation(star_name)
    print(f"The star {star_name} is in the constellation {constellation}.")


elif StarOrObject.lower() == "object":
    object_name = input("Enter your Object: ") 
    altitude, azimuth = get_object_position(object_name, latitude, longitude)
    if altitude is not None and azimuth is not None:
        print(f"{object_name} Position:")
        print("Altitude:", altitude, "degrees")
        print("Azimuth:", azimuth, "degrees")
    constellation = get_constellation(object_name, latitude, longitude)
    print(f"The celestial object {object_name} is in the constellation {constellation[1]}.")

else:
    print("Invalid input. Please enter 'Star' or 'Object'.")



