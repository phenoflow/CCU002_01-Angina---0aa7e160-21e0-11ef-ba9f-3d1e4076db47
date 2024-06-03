# Rochelle Knight, Venexia Walker, et al., 2024.

import sys, csv, re

codes = [{"code":"19057007","system":"snomedct"},{"code":"21470009","system":"snomedct"},{"code":"7921z","system":"snomedct"},{"code":"G33z.","system":"snomedct"},{"code":"7926z","system":"snomedct"},{"code":"662Kz","system":"snomedct"},{"code":"7922z","system":"snomedct"},{"code":"G33z2","system":"snomedct"},{"code":"7923z","system":"snomedct"},{"code":"7925z","system":"snomedct"},{"code":"G33zz","system":"snomedct"},{"code":"792Dz","system":"snomedct"},{"code":"G330z","system":"snomedct"},{"code":"792Cz","system":"snomedct"},{"code":"7920z","system":"snomedct"},{"code":"322Z.","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_01-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_01-angina-anginosa---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_01-angina-anginosa---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_01-angina-anginosa---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
