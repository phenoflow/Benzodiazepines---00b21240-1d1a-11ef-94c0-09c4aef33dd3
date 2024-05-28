# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"36200","system":"gprdproduct"},{"code":"37745","system":"gprdproduct"},{"code":"37566","system":"gprdproduct"},{"code":"33086","system":"gprdproduct"},{"code":"1088","system":"gprdproduct"},{"code":"64729","system":"gprdproduct"},{"code":"57268","system":"gprdproduct"},{"code":"2091","system":"gprdproduct"},{"code":"45829","system":"gprdproduct"},{"code":"39284","system":"gprdproduct"},{"code":"64876","system":"gprdproduct"},{"code":"61450","system":"gprdproduct"},{"code":"41391","system":"gprdproduct"},{"code":"42814","system":"gprdproduct"},{"code":"61886","system":"gprdproduct"},{"code":"23002","system":"gprdproduct"},{"code":"67554","system":"gprdproduct"},{"code":"35932","system":"gprdproduct"},{"code":"56551","system":"gprdproduct"},{"code":"10409","system":"gprdproduct"},{"code":"78434","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-lorazepam---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-lorazepam---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-lorazepam---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
