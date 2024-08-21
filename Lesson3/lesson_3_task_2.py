from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Apple","iPhone X","+79856549874")),
catalog.append(Smartphone("Samsung","Galaxy A50","+79876543210")),
catalog.append(Smartphone("Xiaomi","12 Redmi Note","+79321654987")),
catalog.append(Smartphone("HUAWEI","Pura 70 Ultra","+79012365478")),
catalog.append(Smartphone("HONOR","Magic 6 Pro","+79322165498"))    
for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.subscriber_number}") 