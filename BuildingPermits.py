import csv
with open('Issued_Construction_Permits.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    myDictionary = {}
    rowNumber = 0
    testList = {}
    def outputSum(myDict):

        with open("output.csv", "a") as output:
            writer = csv.writer(output)
            for i in myDict:
                final = sum(myDict[i])
                print(str(i) + " " + str(final))
                writer.writerow([i, final])
            output.close()

    def returnMax(myDict):

        for i in myDict:
            final = max(myDict[i])
            print(str(i) + " " + str(final))

    for row in reader:
        rowNumber += 1
        housing,year,work = row["Housing Units"], row["Calendar Year Issued"], row["Work Class"]
        complete,status,name = row["Completed Date"], row["Status Current"], row["Project Name"]
        permitType = row["Permit Type Desc"]
        if year != "":
            if not myDictionary.keys() >= {year}:
                myDictionary[year] = []
            if housing != "":
                housing = int(housing.replace(',', ''))
                # Handles a few... problematics
                if housing < 50000 and work == "New" and complete != "" and status == "Final" and permitType == "Building Permit":

                    if name == "5501 ROSS RD BLDG 6":
                        housing = 324
                    if name == "629 WEITZENBOCK LN":
                        housing = 134
                    if name == "521 AYINGER LN":
                        housing = 1
                    if name == "809 Dawlish Dr":
                        housing = 1

                    if not testList.keys() >= {name}:
                        testList[name] = []
                        myDictionary[year].append(housing)
        print(rowNumber)

    outputSum(myDictionary)