import boto3
import pyarrow.parquet as pq
import pandas as pd
import json
#  We need to compare two json files wit both the files have same  json structure 
file_object = open('0200813_00006 (2).json') # your nested json file
compared_file = open('output (2).json') # Your file to be compared with another file
file1=json.load(file_object)
#print(file1)
file2=json.load(compared_file)
nested_json_keys=[]
nested_json_values=[]
dumped_list=[]
semi_json_keys=[]
semi_json_values=[]
final_output=[]
second_file_output=[]
second_dumped_list=[]
# for file 1
for keys , values in  file1.items():
    final_output.append(keys)


    if  not isinstance(values,str):
        dumped_list.append(values)
#print(dumped_list)
for values in dumped_list:
    if isinstance(values,list):
        for semi_items in values:
            for ke,ve in semi_items.items():
                #for ke,va in another_value.items():
                final_output.append(ke)

    else:
        for keys,value in values.items():
            if isinstance(value,list):
                for ki in value:
                    for k,v in ki.items():
                        final_output.append(k)
            final_output.append(keys) 

# for  output file

for keys , values in  file2.items():
    second_file_output.append(keys)
    if  not isinstance(values,str):
        second_dumped_list.append(values)
#print(dumped_list)
for values in second_dumped_list:
    if isinstance(values,list):
        for semi_items in values:
            for ke,ve in semi_items.items():
                
                #for ke,va in another_value.items():
                second_file_output.append(ke)

    else:
        for keys,value in values.items():
            
            if isinstance(value,list):
                for ki in value:
                    for k,v in ki.items():
                        second_file_output.append(k)
            else:
                second_file_output.append(keys) 
# keys from file 1
print(len(final_output))
#print("\n")  
# keys from file2
print(len(second_file_output))
rectify=[]
for values in final_output:
    if values in second_file_output:
        rectify.append(values)
# filtering out same keys
print(len(rectify))

