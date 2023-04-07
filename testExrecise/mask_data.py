import re

##processdata:

def get_csv_data(filepath: str, file_name: str):
    try:
        dict_customer_data={}
        with open(filepath+file_name,'r') as custdata:
            customer_data_fields = custdata.readline().rstrip('\n').split(',')
            if len(customer_data_fields)<1:
                raise Exception("No header fields in given file")
            list_customer_data = []
            for each in custdata.readlines()[0:]:
                list_customer_data.append(each.rstrip('\n').split(','))
            
            for each in list_customer_data:
                for index in range(len(customer_data_fields)):
                    dict_customer_data.setdefault(customer_data_fields[index], []).append(each[index])
        return dict_customer_data

    except Exception as exc:
        return exc

def get_list_avg(list_values : list, list_len : int):

    print(list_values)
    if len(list_values)<1:
        raise Exception(f'Atleas one value reuired for average {list_values}')


    sum_list = sum(float(num) for num in list_values)
    avg_of_list = sum_list/list_len
    return avg_of_list

def substitute_alphanum(value: str):

    #sub_list_values = [re.sub('[0-9a-zA-Z]', 'X', value) for value in list_values]
    #return sub_list_values
    sub_with = 'X'
    sub_value = re.sub('[0-9a-zA-Z]', sub_with, value)
    return sub_value

def create_masked_data(dict_customer_data: dict):
    mask_dict_customer_data = {}
    for key, valueses in dict_customer_data.items():
        #if all(value.isdigit() || value.isalnum    for value in values):
        values = [each for each in valueses if each.strip()] #removing empty value
        #print(values)
        if all([value.replace('.','').isdigit() for value in values]):
            #calculating len of original list including space/empty
            average_value = get_list_avg(values, len(valueses))
            #print(average_value)
            mask_dict_customer_data[key] = [average_value for each in valueses]
        else:
            #dict_customer_data[key] = [re.sub('[0-9a-zA-Z]', 'X', value) for value in valueses]
            mask_dict_customer_data[key] = list(map(substitute_alphanum, valueses))
    return mask_dict_customer_data



##Output formatting:
def process_masked_data(dict_customer_data: dict):
    listlist = list(each for each in dict_customer_data.values())
    print(listlist)
    x = list(zip(*listlist))
    return x

##Writing data:
def write_masked_tofile(filepath,out_file_name, dict_customer_data: dict):
    masked_data_list = process_masked_data(dict_customer_data)
    with open(filepath+out_file_name,'w') as wr_custdata:
        for each in masked_data_list:
            #print(",".join(str(val) for val in each))
            wr_custdata.write(",".join(str(key) for key in dict_customer_data.keys())+'\n')
            wr_custdata.write(",".join(str(val) for val in each)+'\n')

#Reporting task:

def minmax_avg_report(list_value: list):
    #remove empty
    values = [each for each in list_value if each.strip()]

    if len(values)<2:
        raise Exception("Invalid list: At least two values required for calculating Mx, Min and Avg")

    if all([value.replace('.','').isdigit() for value in values]):
        num_values = [float(num) for num in values]

    else:
        num_values = [len(each) for each in list_value]
    

    min_len_value = min(num_values)
    max_len_value = max(num_values)
    avg_len_value = sum(num_values)/len(list_value)
    return f'Max. {max_len_value}, Min. {min_len_value}, Avg. {avg_len_value}'


if __name__ == "__main__":
    try:
        #I can use config ini or dotenv to store config parameter.
        filepath = "D:\\"
        inp_file_name = "customers.csv"
        out_file_name = "masked_client.csv"

        #dict_customer_data = {}
        dict_customer_data = get_csv_data(filepath, inp_file_name)

        if dict_customer_data:
            print(dict_customer_data)
            masked_dict_customer_data = create_masked_data(dict_customer_data)
        #print(masked_dict_customer_data)

        write_masked_tofile(filepath, out_file_name, masked_dict_customer_data)

        #print report:
        #For name:
        field_name = 'Name'
        if dict_customer_data:
            minmax_avg = minmax_avg_report(dict_customer_data[field_name])
            print(f'{field_name}: {minmax_avg}')
            #For Biiling
            field_name = 'Billing'
            minmax_avg = minmax_avg_report(dict_customer_data[field_name])
            print(f'{field_name}: {minmax_avg}')
        else:
            raise Exception(f'File data is not expected {dict_customer_data[field_name]}')
    
    except Exception as exc:
        print(exc)






