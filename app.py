from tkinter import *
import pandas as pd

def removeDuplicates(list):
    # The list MUST be sorted
    i = 0
    lengthOfList = len(list)
    while i < lengthOfList - 1:
        if list[i] == list[i+1]:
            del list[i+1]
            lengthOfList -= 1
            i -= 1
        i += 1
    return list

def main():
    # Import Excel spreadsheet as dataframe
    heatCapacity_dataframe = pd.read_excel("heatCapacity.xlsx")
    # Create a non-duplicate components list (default OptionMenu list @index 0)
    component_options = ['Select a component'] + removeDuplicates(heatCapacity_dataframe['Component'].tolist())
    # Create a component state list corresponding to each row in the original dataframe
    component_states = heatCapacity_dataframe['State'].tolist()


if __name__ == "__main__":
    main()