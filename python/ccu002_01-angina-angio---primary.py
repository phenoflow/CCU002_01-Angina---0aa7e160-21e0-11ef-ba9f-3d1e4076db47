# Rochelle Knight, Venexia Walker, et al., 2024.

import sys, csv, re

codes = [{"code":"371808007","system":"snomedct"},{"code":"79280","system":"snomedct"},{"code":"7A6H4","system":"snomedct"},{"code":"7A6H3","system":"snomedct"},{"code":"7928z","system":"snomedct"},{"code":"793G.","system":"snomedct"},{"code":"79290","system":"snomedct"},{"code":"7A6G1","system":"snomedct"},{"code":"79283","system":"snomedct"},{"code":"79282","system":"snomedct"},{"code":"7A540","system":"snomedct"},{"code":"793G3","system":"snomedct"},{"code":"793Gz","system":"snomedct"},{"code":"7A564","system":"snomedct"},{"code":"7928y","system":"snomedct"},{"code":"79275","system":"snomedct"},{"code":"793Gy","system":"snomedct"},{"code":"7928","system":"snomedct"},{"code":"79281","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_01-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_01-angina-angio---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_01-angina-angio---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_01-angina-angio---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
