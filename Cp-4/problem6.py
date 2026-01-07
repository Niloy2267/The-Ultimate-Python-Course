letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Niloy").replace("<|Date|", "24 September 2050"))

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("</Name/>", "Anny").replace("</Date/>","21 August 2026"))