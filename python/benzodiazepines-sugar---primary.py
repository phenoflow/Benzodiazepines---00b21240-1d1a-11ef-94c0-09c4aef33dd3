# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"20968","system":"gprdproduct"},{"code":"50108","system":"gprdproduct"},{"code":"70682","system":"gprdproduct"},{"code":"32847","system":"gprdproduct"},{"code":"74984","system":"gprdproduct"},{"code":"53461","system":"gprdproduct"},{"code":"74584","system":"gprdproduct"},{"code":"77999","system":"gprdproduct"},{"code":"27367","system":"gprdproduct"},{"code":"10274","system":"gprdproduct"},{"code":"68414","system":"gprdproduct"},{"code":"64879","system":"gprdproduct"},{"code":"13200","system":"gprdproduct"},{"code":"34491","system":"gprdproduct"},{"code":"55836","system":"gprdproduct"},{"code":"54759","system":"gprdproduct"},{"code":"55481","system":"gprdproduct"},{"code":"780","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-sugar---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-sugar---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-sugar---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
