import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

print("..#....#..\n..##..##..\n..#.##.#..", end = " ") #m
print("\n..#....#..\n..#....#..\n\n") 
print("..######..\n..#....#..\n..######..", end = " ") #p
print("\n..#.......\n..#.......\n\n")
print("..######..\n..#....#..\n..#.##...", end = " ") #r
print("\n..#...#...\n..#....#..\n\n")
print('THE FAUCETER\n')

print('you can get a details of Location & ISP of a Phone Number')
print('enter your phone number with country code(ie: +91xxxxxxxxxx) without space')
phone_number = phonenumbers.parse(input('type :'))


if phonenumbers.is_valid_number(phone_number) :

    print('you entered a valid number of',phone_number)
    print('Location :' ,geocoder.description_for_number(phone_number,'en'))
    print('ISP name :' ,carrier.name_for_number(phone_number,'en'))
    #print('zone :' , timezone(phone_number,'en'))

else :
    print('you entered a invalid number!')
    