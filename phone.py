import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier 
ch_nums = phonenumbers.parse(number,'CH')
ch_Data = phonenumbers.parse(number, 'RO')
print(geocoder.description_for_number(ch_nums,'en'))
print(carrier.name_for_number(ch_Data , 'en'))