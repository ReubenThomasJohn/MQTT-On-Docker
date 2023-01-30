# import datetime 
# from datetime import timezone

# string = '2023-01-29 18:17:10.491136'
# string1 = '2023-01-30 00:54:53.325584'

# time_stamp = '2023-01-30 01:01:19.673061'

# # print(type(datetime.datetime.utcnow()))

# def convert_to_nanoseconds(time_string):
#     converted = datetime.datetime(int(time_string[:4]), int(time_string[6]), 
#             int(time_string[8:10]), int(time_string[11:13]),
#             int(time_string[14:16]), int(time_string[17:19]), int(time_string[20:]))
#     converted = converted.replace(tzinfo=timezone.utc)
#     return converted

# # print(convert_to_nanoseconds(string))


# from datetime import datetime   
# import pytz



# t2 = '2023-01-30 10:05:31.657632'
# t1 = '2023-1-30 9:58:42:716149'
# t3 = '2023-1-30 10:05:31.657632'

# local = pytz.timezone("Asia/Kolkata")
# naive = datetime.strptime(t3, "%Y-%m-%d %H:%M:%S.%f")
# local_dt = local.localize(naive, is_dst=True)
# utc_dt = local_dt.astimezone(pytz.utc)
# print(utc_dt.strftime("%Y-%m-%d %H:%M:%S.%f"))
# print(datetime.utcnow())


# # print(utc_dt)
# # ValueError: time data '2023-01-30 10:05:31.857632' does not match format '%Y-%m-%d %H:%M:%S:%f'




# # print(datetime.datetime(2022, 9, 20, 11, 27, 46).timestamp())

# # 'updated_at': datetime.datetime(2023, 1, 28, 17, 51, 11, 708867, tzinfo=tzlocal())}

# data_string = 'a 2023-01-30 11:31:00.903674 36 192 48 53 88'

# data = ['a 2023-01-30 11:56:12.894537 32 180 41 50 64', 
#         'a 2023-01-30 11:56:17.899441 35 183 42 55 70', 
#         'a 2023-01-30 11:56:22.903597 36 187 46 77 71', 
#         'a 2023-01-30 11:56:27.911373 35 189 42 54 75', 
#         'a 2023-01-30 11:56:32.915878 36 186 47 59 74', 
#         'a 2023-01-30 11:56:37.922391 33 185 45 75 79', 
#         'a 2023-01-30 11:56:42.928203 35 188 41 69 63']
# # ValueError: could not convert string to float: "64'"
# data_string = str(data)
# print(data_string[1:-1].split(','))

# print(data_string[1:-1].split(',')[0])
# print(data_string[-1])

t1 = '2023-01-30 12:13:00.903674'

import datetime
t1 = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S.%f")
t1.strftime("%Y-%m-%d %H:%M:%S.%f")

print(t1)