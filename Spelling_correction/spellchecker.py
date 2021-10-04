from gingerit.gingerit import GingerIt

text = 'PARACETAMOI TABLETSIP Parasafe ANALGESIC.ANTIPYRETICTABLETS JStrassenburg'
lo_case = text.lower()

parser = GingerIt()
ct = parser.parse(lo_case)
print(ct['result']) 