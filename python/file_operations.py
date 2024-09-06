

def read_file(filename):

    with open(filename) as file:

        file = open(filename,"r")
        data = file.read()
        print(data)
        


def writefile(filename, data):

    with open(filename, 'w') as file:
        file.write(data)
        

    print("Data written successfully to file.")



def appenddata(filename, data):

    with open(filename, 'a') as file:
        file.write(data)

    print("Data appended successfully to file.")
