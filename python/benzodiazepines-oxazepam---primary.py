# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"36604","system":"gprdproduct"},{"code":"41411","system":"gprdproduct"},{"code":"41602","system":"gprdproduct"},{"code":"4140","system":"gprdproduct"},{"code":"41542","system":"gprdproduct"},{"code":"7652","system":"gprdproduct"},{"code":"8721","system":"gprdproduct"},{"code":"4141","system":"gprdproduct"},{"code":"41601","system":"gprdproduct"},{"code":"41531","system":"gprdproduct"},{"code":"41553","system":"gprdproduct"},{"code":"46946","system":"gprdproduct"},{"code":"4566","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-oxazepam---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-oxazepam---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-oxazepam---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
