import csv
import os

PATH = "consumo.csv"
PATH_CSVS = "D:\Programming\Python\CSV Data Handling\Electricity Bills Handling\CSVs\consejemplo.csv"
DIR_LIST = []

def get_dir_list(mother_folder_path):
    return os.listdir(mother_folder_path)

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

        dict_keys = dict_id_value.keys()
        dict_vals = dict_id_value.values()

        list_id_vals = list(zip(dict_keys, dict_vals))

        for pair in list_id_vals:
            csvfile.write(pair[0] + ", " + pair[1] + ", \n")

def read_and_find_occurences(dict_id_val):

    for file in get_dir_list("CSVs"):
        file = "CSVs/" + file
    
        if os.path.isfile(file):
            with open(file, "r+") as csvfile:
                print("File found")

                #to 6th row
                next(csvfile)
                next(csvfile)
                next(csvfile)
                next(csvfile)
                next(csvfile)

                with open(file[:-4] + "_overwritten.csv", "w") as csvow:

                    for row in csvfile:
                        split_list = row.split(',')
                        value = ""
                        try:
                            value = dict_id_val[split_list[0]]
                            split_list[-3] = value
                            
                            list_toStr = ""
                            for el in split_list:
                                list_toStr = list_toStr + el + ","

                            list_toStr = list_toStr[:-1]

                            csvow.write(list_toStr)
                            print("found")

                        except KeyError:
                            pass

                    

        else:
            print("File not found")

            



if __name__ == "__main__":
    dict_id_values = read_csv()

    print(len(dict_id_values))


    read_and_find_occurences(dict_id_values)
