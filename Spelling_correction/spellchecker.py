from gingerit.gingerit import GingerIt

text = '10010 TABLETS PARACETAMOL TABLETS BP 500 mg Dolo MICRO'
lo_case = text.lower()

parser = GingerIt()
ct = parser.parse(lo_case)
print(ct['result']) 