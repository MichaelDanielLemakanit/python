name = " JoHn"
name=name.strip().lower()

print(name)

sentence_one="The Dog Breed is German Shepherd"
sentence_one = sentence_one[0:0] + "Breed is German"

print(sentence_one)

sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
start = sentence_two.find("Clinton")
end = start + len("Clinton forces")

print(sentence_two[start:end])

sentence_three="The lazy dog; ran so fast; it hit the wall."
split_result = sentence_three.split(";")
print("Question 3: Result is {split_result}, Length is {len(split_result)}")

first_name = "  Joh.n"
last_name = "  Do,e"

clean_first = first_name.strip().replace(".", "")
clean_last = last_name.strip().replace(",", "")
full_name = "{clean_first} {clean_last}"
print("Question 4: {full_name}")

r = '["E","W","C"]'
clean_r = r.replace("[", "").replace("]", "").replace('"', "").replace(",", "")
print("Question 5: {clean_r}")

