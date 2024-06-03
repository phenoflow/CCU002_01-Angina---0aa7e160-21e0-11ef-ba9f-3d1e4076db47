# Rochelle Knight, Venexia Walker, et al., 2024.

import sys, csv, re

codes = [{"code":"46109009","system":"snomedct"},{"code":"712866001","system":"snomedct"},{"code":"414795007","system":"snomedct"},{"code":"10971000087107","system":"snomedct"},{"code":"413844008","system":"snomedct"},{"code":"697976003","system":"snomedct"},{"code":"413444003","system":"snomedct"},{"code":"322..","system":"snomedct"},{"code":"3222","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_01-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_01-angina-ischaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_01-angina-ischaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_01-angina-ischaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
