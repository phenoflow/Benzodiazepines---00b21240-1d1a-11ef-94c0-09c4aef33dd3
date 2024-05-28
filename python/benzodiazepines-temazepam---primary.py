# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"30985","system":"gprdproduct"},{"code":"34406","system":"gprdproduct"},{"code":"77686","system":"gprdproduct"},{"code":"56811","system":"gprdproduct"},{"code":"38424","system":"gprdproduct"},{"code":"41653","system":"gprdproduct"},{"code":"62645","system":"gprdproduct"},{"code":"34331","system":"gprdproduct"},{"code":"74783","system":"gprdproduct"},{"code":"41718","system":"gprdproduct"},{"code":"41717","system":"gprdproduct"},{"code":"33648","system":"gprdproduct"},{"code":"36602","system":"gprdproduct"},{"code":"79487","system":"gprdproduct"},{"code":"15110","system":"gprdproduct"},{"code":"20","system":"gprdproduct"},{"code":"10430","system":"gprdproduct"},{"code":"1729","system":"gprdproduct"},{"code":"7567","system":"gprdproduct"},{"code":"38418","system":"gprdproduct"},{"code":"41516","system":"gprdproduct"},{"code":"46078","system":"gprdproduct"},{"code":"45283","system":"gprdproduct"},{"code":"60825","system":"gprdproduct"},{"code":"30779","system":"gprdproduct"},{"code":"34002","system":"gprdproduct"},{"code":"46939","system":"gprdproduct"},{"code":"45254","system":"gprdproduct"},{"code":"34508","system":"gprdproduct"},{"code":"70071","system":"gprdproduct"},{"code":"49589","system":"gprdproduct"},{"code":"921","system":"gprdproduct"},{"code":"75594","system":"gprdproduct"},{"code":"34572","system":"gprdproduct"},{"code":"7569","system":"gprdproduct"},{"code":"73483","system":"gprdproduct"},{"code":"41562","system":"gprdproduct"},{"code":"46964","system":"gprdproduct"},{"code":"56927","system":"gprdproduct"},{"code":"2403","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-temazepam---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-temazepam---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-temazepam---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
