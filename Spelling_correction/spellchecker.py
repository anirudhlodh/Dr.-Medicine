from gingerit.gingerit import GingerIt

text = "ABILIFY 10mg aripiprazol 28 Tabletten"
lo_case = text.lower()

parser = GingerIt()
ct = parser.parse(lo_case)
x = ct['result']
print(x) 