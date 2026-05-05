import json



def reading_file (file_name):
    with open (file_name,'r', encoding = 'UTF-8' ) as my_file:
        file_contents = my_file.read() 
    file_contents = json.loads(file_contents)
    return(file_contents)


def writing_file (file_name,file_contents):
    with open (file_name,'w', encoding = 'UTF-8' ) as my_file:
        json.dump(file_contents, my_file,indent=4) 

def create_empty_file (file_name):
    with open (file_name,'w',encoding = 'UTF-8') as my_file:
        json.dump([], my_file ,indent=4)



