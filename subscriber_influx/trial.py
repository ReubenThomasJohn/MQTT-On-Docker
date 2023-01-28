from datetime import datetime


string = '2022-09-20 11:27:46'

def convert_to_nanoseconds(time_string):
    converted = datetime(int(string[:4]), int(string[6]), 
            int(string[8:10]), int(string[11:13]),
            int(string[14:16]), int(string[17:19])).timestamp()
    return converted

print(convert_to_nanoseconds(string))



# print(datetime.datetime(2022, 9, 20, 11, 27, 46).timestamp())

# 'updated_at': datetime.datetime(2023, 1, 28, 17, 51, 11, 708867, tzinfo=tzlocal())}