import csv

reads = ['SetupFiles/unionInfantry.csv', 'SetupFiles/confedInfantry.csv', 'SetupFiles/unionArtillery.csv', 'SetupFiles/confedArtillery.csv']
writes = ['SanitizedSetupFiles/unionInfantrySan.csv', 'SanitizedSetupFiles/confedInfantrySan.csv', 'SanitizedSetupFiles/unionArtillerySan.csv', 'SanitizedSetupFiles/confedArtillerySan.csv']

def sanitizer(readFileName, writeFileName): 
  readFile = open(readFileName, 'rb')
  reader = csv.reader(readFile)
  writeFile = open(writeFileName, 'w')
  writer = csv.writer(writeFile)

  i = 0
  for row in reader:
    if i != 0:
      del row[0]
      writer.writerow(row)
    i = i + 1

  readFile.close()
  writeFile.close()

k = 0
while k < len(reads):
  sanitizer(reads[k], writes[k])
  k = k + 1


