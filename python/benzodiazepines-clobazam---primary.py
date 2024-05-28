# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"3111","system":"gprdproduct"},{"code":"51425","system":"gprdproduct"},{"code":"41303","system":"gprdproduct"},{"code":"62926","system":"gprdproduct"},{"code":"52056","system":"gprdproduct"},{"code":"3110","system":"gprdproduct"},{"code":"46796","system":"gprdproduct"},{"code":"71813","system":"gprdproduct"},{"code":"52680","system":"gprdproduct"},{"code":"60320","system":"gprdproduct"},{"code":"73661","system":"gprdproduct"},{"code":"48010","system":"gprdproduct"},{"code":"15429","system":"gprdproduct"},{"code":"52052","system":"gprdproduct"},{"code":"37696","system":"gprdproduct"},{"code":"3109","system":"gprdproduct"},{"code":"17054","system":"gprdproduct"},{"code":"52093","system":"gprdproduct"},{"code":"72832","system":"gprdproduct"},{"code":"29806","system":"gprdproduct"},{"code":"70981","system":"gprdproduct"},{"code":"20966","system":"gprdproduct"},{"code":"69976","system":"gprdproduct"},{"code":"50389","system":"gprdproduct"},{"code":"46850","system":"gprdproduct"},{"code":"70255","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-clobazam---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-clobazam---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-clobazam---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
