import csv

PATH = "consumo.csv"

def read_csv():
    dict_id_val = {}

    with open(PATH, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            row_string = row[0]
            id_list = row_string.split(';', 2) 

            id = id_list[0] + id_list[1] + "0"

            dict_id_val.update({id: id_list[2]})
            

    return dict_id_val

def write_csv(dict_id_value):

    with open("new.csv", "w") as csvfile:
        #csvwrite = csv.writer(csvfile)

        dict_keys = dict_id_value.keys()
        dict_vals = dict_id_value.values()

        list_id_vals = list(zip(dict_keys, dict_vals))

        for pair in list_id_vals:
            #pair = [element for element in pair]
            #csvwrite.writerow(pair)
            csvfile.write(pair[0] + ", " + pair[1] + ", \n")





if __name__ == "__main__":
    dict_id_values = read_csv()

    write_csv(dict_id_values)
