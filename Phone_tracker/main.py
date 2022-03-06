from phonenumbers import geocoder, carrier
import phonenumbers

mobile_numbers = ["9571236499","9784799278","8306062254","7427868230","8769730443","9660010238","9829204279"]

def get_details(number):
    ch_nmber = phonenumbers.parse(number, "CH")

    region = geocoder.description_for_number(ch_nmber, 'en')

    # getting service provider

    service_nmber = phonenumbers.parse(number, "RO")
    service = carrier.name_for_number(service_nmber, "en")

    print(service_nmber)
    print(service)
    print(region)

for no in mobile_numbers:
    get_details(f"+91{no}")