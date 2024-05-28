# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"62270","system":"gprdproduct"},{"code":"41583","system":"gprdproduct"},{"code":"64470","system":"gprdproduct"},{"code":"45241","system":"gprdproduct"},{"code":"41574","system":"gprdproduct"},{"code":"28879","system":"gprdproduct"},{"code":"78362","system":"gprdproduct"},{"code":"35936","system":"gprdproduct"},{"code":"6025","system":"gprdproduct"},{"code":"3147","system":"gprdproduct"},{"code":"41629","system":"gprdproduct"},{"code":"4543","system":"gprdproduct"},{"code":"5294","system":"gprdproduct"},{"code":"41582","system":"gprdproduct"},{"code":"34928","system":"gprdproduct"},{"code":"1463","system":"gprdproduct"},{"code":"6516","system":"gprdproduct"},{"code":"8550","system":"gprdproduct"},{"code":"41581","system":"gprdproduct"},{"code":"77652","system":"gprdproduct"},{"code":"2122","system":"gprdproduct"},{"code":"41606","system":"gprdproduct"},{"code":"43438","system":"gprdproduct"},{"code":"79387","system":"gprdproduct"},{"code":"41988","system":"gprdproduct"},{"code":"74065","system":"gprdproduct"},{"code":"40386","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-chlordiazepoxide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-chlordiazepoxide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-chlordiazepoxide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
