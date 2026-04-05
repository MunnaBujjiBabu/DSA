# # re is used - search, matching, manipulating 

# import re
# sample_text = "prepraing for python coding "


# match_status = re.search("python", sample_text)
# print(match_status.group())

# match_status_2 = re.search("java", sample_text)
# print(match_status_2)






























import re

# # string_1 = "Hello World     1===2345"
# # # string_2 = ["one", 1, "Hello", True]
# # matched = re.search("Hello", string_1)

# # print(matched.group())
# # print(matched.endpos)
# # print(matched.span())



# string_3 = "000 00000 hello 111 2222 33333 5555"
# matched_string_3 = re.search(r"\d*", string_3)

# print(matched_string_3.group())


string_1 = "Hello World     1===2345"

matched_string_1 = re.search(r"[A-Za-z\sA-Za-z]+", string_1)
print(matched_string_1.group())




















# my_string = "I scored 99"
# print(re.search("100", my_string))

