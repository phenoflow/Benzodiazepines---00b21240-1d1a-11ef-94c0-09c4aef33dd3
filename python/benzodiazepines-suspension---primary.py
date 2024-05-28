# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"9045","system":"gprdproduct"},{"code":"23874","system":"gprdproduct"},{"code":"67192","system":"gprdproduct"},{"code":"67957","system":"gprdproduct"},{"code":"69783","system":"gprdproduct"},{"code":"75473","system":"gprdproduct"},{"code":"78306","system":"gprdproduct"},{"code":"73751","system":"gprdproduct"},{"code":"74755","system":"gprdproduct"},{"code":"77799","system":"gprdproduct"},{"code":"12849","system":"gprdproduct"},{"code":"51985","system":"gprdproduct"},{"code":"9430","system":"gprdproduct"},{"code":"67193","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-suspension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-suspension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-suspension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
