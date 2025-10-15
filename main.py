# slovar (dict), JSON
"""
slovar = {
    "ohio": "sigma",
    "vrednost": "ohio"
}
print(slovar["ohio"])

imenik = {
    "Ažbe": "51124124",
    "Primas": "241124124",
    "tilis": "643647545"
}
print(imenik["Primas"])
"""

import requests
#pip install requests
ime = str(input("VNESI IME: "))
nameUrl = f"https://api.genderize.io?name={ime}"
ageUrl = f"https://api.agify.io?name={ime}"
nationalizeUrl = f"https://api.nationalize.io?name={ime}"


nameCall = requests.get(nameUrl).json()
ageCall = requests.get(ageUrl).json()
nationalizeCall = requests.get(nationalizeUrl).json()

print(f"ime : {ime}")