# Пользователь вводит текст. слова разделены пробелами (возможно не одним) и знаками пунктуации.
# Посчитать количество слов в тексте
input_string = """The last few years have shown us the value of connecting with consumers 
                in a holistic way especially when in-person efforts and marketing plans aren’t possible. 
                Metaverse platforms give that ‘physical world feel’ from afar and allow their customers 
                to be whomever they want to be in that space."""
input_string = input_string.lower()
input_string = input_string.replace('.', ' ')
input_string = list(input_string.split())
input_string_set = set(input_string)
print(input_string_set)
print(len(input_string_set))
