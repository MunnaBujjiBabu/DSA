# #matching emails
import re

# test_email = "myemail@gamil.com"
# #test_email = "m@g.c"

# match_email_status = re.match(r"^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]+", test_email)

# print(match_email_status.group())



# match_str = "Prajwal Saaaa"
# name_match=re.match(r"^[A-Za-z]+\s[A-Za-z]", match_str)
# print(name_match.group())
# sample_str="19/02/2026"

# match_str = re.match(r"\d{2}/\d{2}/\d{4}", sample_str)


# print(match_str.group())


# phone_number = "+91 9090912345"

# match_str = re.match(r"\+\d{2}\s\d{10}", phone_number)
# print(match_str.group())



# phone_number = "the number is 123 456-7890 asdfasdf"

# match_my_num = re.search(r"\d{3}\s\d{3}-\d{4}", phone_number)
# print(match_my_num)



# text = "munna is my name "

# match_text = re.match(r"^munna", text)
# match_text_2 = re.search(r"munna", text)

# print(match_text.group())
# print(match_text_2.group())


# text = "Hello World! test 1234 2w345 345 "

# text_rep = re.sub(r"\s", "-", text)
# print(text_rep)





# text_web = "http://akamai.co.in/"
# text_1 = "http://akamai.in/"
# pattern= r"https?://[A-Za-z0-9]+\.?[A-Za-z]+?\.[A-Za-z]+/"

# matched_web = re.match(pattern, text_web)

# print(matched_web.group())


# text_2 = "http://akamai/"
# pattern = r"http://[A-Za-z./]+"

# matched_text = re.match(pattern, text_2)
# print(matched_text.group())


# text = "apple,\"banana\", cat, dog"
# pattern = r",\s*"

# matched  = re.split(pattern, text)
# print(matched)


# text = "I have 10 pen & 20 pencils & 5 notes 0 123"
# pattern = r"\d+"

# matched = re.findall(pattern, text)
# print(matched)

# find all words starting with A

# text = "Apple aand test Avacoda are good for health"
# pattern = r"\b[Aa]\w+"

# matched = re.findall(pattern, text)
# print(matched)






# At least 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one number
# At least one special character

# sample_pass = "user@123"

# pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%])[A-Za-z0-9!@#$%]{8,}"

# matched_pass = re.match(pattern, sample_pass)
# print(matched_pass)



# # Extract all words from sentence 

# sentence = "Python is fun! Let's learn regex"
# pattern = r"\b\w+\b"
# words = re.findall(pattern, sentence)
# print(words)


# # Extracting All Email Addresses from a Text
# text = "Contact us at support@example.com or sales@company.orag. @munna, test@test.com"
# pattern = r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{3}\b"
# email_address = re.findall(pattern, text) 
# print(email_address)


# #Extracting All Hashtags from a Tweet

# tweet = "Learning #Python and #Regex is fun! #Coding"
# pattern_hash = r"#\w+"
# match_hash = re.findall(pattern_hash, tweet)
# print(match_hash)



# #Extracting Sentences That End with a Question Mark
# text = "What is your name? Where do you live? I love Python!"

# pattern = r"[A-Za-z\s]+\?"
# # pattern = r"\w+\?"

# matched_question = re.findall(pattern, text)

# print(matched_question)


