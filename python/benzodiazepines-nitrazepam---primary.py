# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"34408","system":"gprdproduct"},{"code":"64775","system":"gprdproduct"},{"code":"71073","system":"gprdproduct"},{"code":"35","system":"gprdproduct"},{"code":"34555","system":"gprdproduct"},{"code":"3686","system":"gprdproduct"},{"code":"65135","system":"gprdproduct"},{"code":"61678","system":"gprdproduct"},{"code":"34770","system":"gprdproduct"},{"code":"34964","system":"gprdproduct"},{"code":"34686","system":"gprdproduct"},{"code":"9814","system":"gprdproduct"},{"code":"46953","system":"gprdproduct"},{"code":"73660","system":"gprdproduct"},{"code":"79375","system":"gprdproduct"},{"code":"14480","system":"gprdproduct"},{"code":"34806","system":"gprdproduct"},{"code":"2407","system":"gprdproduct"},{"code":"41385","system":"gprdproduct"},{"code":"7924","system":"gprdproduct"},{"code":"75197","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-nitrazepam---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-nitrazepam---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-nitrazepam---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
