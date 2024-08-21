from address import Address
from mailing import Mailing

# Создание экземпляра класса Address для to_address и from_address
to_address = Address("123456", "Москва", "Улица Пушкина", "10", "20")
from_address = Address("654321", "Санкт-Петербург", "Улица Лермонтова", "5", "15")

# Создание экземпляра класса Mailing
mailing_instance = Mailing(to_address, from_address, 500, "ABC123")

# Вывод информации о почтовом отправлении в заданном формате
print(f"Отправление {mailing_instance.track} из {mailing_instance.from_address.index}, {mailing_instance.from_address.city}, {mailing_instance.from_address.street}, {mailing_instance.from_address.house} - {mailing_instance.from_address.apartment} в {mailing_instance.to_address.index}, {mailing_instance.to_address.city}, {mailing_instance.to_address.street}, {mailing_instance.to_address.house} - {mailing_instance.to_address.apartment}. Стоимость {mailing_instance.cost} рублей.")
