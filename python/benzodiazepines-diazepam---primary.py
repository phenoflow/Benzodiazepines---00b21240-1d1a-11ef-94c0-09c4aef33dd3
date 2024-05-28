# Matthew J Carr, Sarah Steeg, Roger T Webb, Nav Kapur, Carolyn A Chew-Graham, Kathryn M Abel, Holly Hope, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"73526","system":"gprdproduct"},{"code":"34340","system":"gprdproduct"},{"code":"41607","system":"gprdproduct"},{"code":"34615","system":"gprdproduct"},{"code":"62541","system":"gprdproduct"},{"code":"63238","system":"gprdproduct"},{"code":"1400","system":"gprdproduct"},{"code":"45313","system":"gprdproduct"},{"code":"45244","system":"gprdproduct"},{"code":"63694","system":"gprdproduct"},{"code":"69810","system":"gprdproduct"},{"code":"59407","system":"gprdproduct"},{"code":"71336","system":"gprdproduct"},{"code":"34482","system":"gprdproduct"},{"code":"32296","system":"gprdproduct"},{"code":"73815","system":"gprdproduct"},{"code":"34335","system":"gprdproduct"},{"code":"45135","system":"gprdproduct"},{"code":"3205","system":"gprdproduct"},{"code":"28347","system":"gprdproduct"},{"code":"57838","system":"gprdproduct"},{"code":"46","system":"gprdproduct"},{"code":"47","system":"gprdproduct"},{"code":"34677","system":"gprdproduct"},{"code":"33672","system":"gprdproduct"},{"code":"64200","system":"gprdproduct"},{"code":"67451","system":"gprdproduct"},{"code":"46966","system":"gprdproduct"},{"code":"34876","system":"gprdproduct"},{"code":"29945","system":"gprdproduct"},{"code":"45218","system":"gprdproduct"},{"code":"34681","system":"gprdproduct"},{"code":"67785","system":"gprdproduct"},{"code":"46913","system":"gprdproduct"},{"code":"57749","system":"gprdproduct"},{"code":"34338","system":"gprdproduct"},{"code":"60936","system":"gprdproduct"},{"code":"71245","system":"gprdproduct"},{"code":"34892","system":"gprdproduct"},{"code":"56236","system":"gprdproduct"},{"code":"54695","system":"gprdproduct"},{"code":"34635","system":"gprdproduct"},{"code":"41632","system":"gprdproduct"},{"code":"78738","system":"gprdproduct"},{"code":"34807","system":"gprdproduct"},{"code":"34524","system":"gprdproduct"},{"code":"62216","system":"gprdproduct"},{"code":"34293","system":"gprdproduct"},{"code":"34561","system":"gprdproduct"},{"code":"74342","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benzodiazepines-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benzodiazepines-diazepam---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benzodiazepines-diazepam---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benzodiazepines-diazepam---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
