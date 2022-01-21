from gingerit.gingerit import GingerIt

text = "ABILIFY10mg aripiprazol 28Tabletten A"
lo_case = text.lower()

parser = GingerIt()
ct = parser.parse(lo_case)
x = ct['result']
print(x) 