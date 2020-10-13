# Nmae: Miss.Pinmanee Seesorn(Baifern)
# Date: 10/12/2020

# declare variables
numbers = ['0','1','2','3','4','5','6','7','8','9']         #numerical characters in an array for comparing with input characters
pre_Output = []                                             #an empty array only for numerical characters from the input
output = 0
zero = 0

# separate numerical characters from the input
def SeparateInt():
    for i in range(0, len(split_data)):                     #loop to check for every character in one input
       if split_data[i] in numbers:                         #check if there is any number in the input
          pre_Output.append(numbers.index(split_data[i]))   #add numbers in pre_output array

def ConcatInt(output):                                      #Concatenate each number together
    unit = len(pre_Output)
    for n in range(0, unit):                                #loop to check the amount of numerical character
        zero = 10**(unit-(n+1))                             #add '0' after each numerical character
        output = output + pre_Output[n]*zero                #combine each numbers together
    return output

input_data = input('Enter your input: ')                    #get an input
split_data = list(input_data)                               #split each character in the input

SeparateInt()
result = ConcatInt(output)
print(result)
print(type(result))

