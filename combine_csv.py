fout = open("contracts_all.csv", "a")

for line in open("./2010_Contractor_Listing.csv"):
    fout.write(line)
for num in range(2011,2018):
    f = open(str(num)+"_Contractor_Listing.csv")
    f.next()
    for line in f:
        fout.write(line)
    f.close()
fout.close()
