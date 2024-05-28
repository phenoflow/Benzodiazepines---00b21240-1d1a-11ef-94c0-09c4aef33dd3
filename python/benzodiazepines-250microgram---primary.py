# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"46896","system":"gprdproduct"},{"code":"58482","system":"gprdproduct"},{"code":"48544","system":"gprdproduct"},{"code":"76218","system":"gprdproduct"},{"code":"78323","system":"gprdproduct"},{"code":"34361","system":"gprdproduct"},{"code":"74865","system":"gprdproduct"},{"code":"76592","system":"gprdproduct"},{"code":"17637","system":"gprdproduct"},{"code":"34292","system":"gprdproduct"},{"code":"14743","system":"gprdproduct"},{"code":"47066","system":"gprdproduct"},{"code":"45077","system":"gprdproduct"},{"code":"74219","system":"gprdproduct"},{"code":"1559","system":"gprdproduct"},{"code":"61626","system":"gprdproduct"},{"code":"53311","system":"gprdproduct"},{"code":"75571","system":"gprdproduct"},{"code":"34642","system":"gprdproduct"},{"code":"13279","system":"gprdproduct"},{"code":"3687","system":"gprdproduct"},{"code":"59396","system":"gprdproduct"},{"code":"61015","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-250microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-250microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-250microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
