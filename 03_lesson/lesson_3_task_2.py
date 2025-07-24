from smartphone import Smartphone
catalog = [
    Smartphone("IPhone", "16Pro", "+71234556677"),
    Smartphone("IPhone", "16ProMa[", "+71234556688"),
    Smartphone("Sumsung", "23S", "+71234556699"),
    Smartphone("Sumsung", "24SE", "+71234558877"),
    Smartphone("Sumsung", "20FE", "+71234552233"),
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
