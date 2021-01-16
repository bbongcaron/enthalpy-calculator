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

    root = Tk()
    component1 = 'none'
    component2 = 'none'
    # Creating Title Widget
    title = Label(root, text="Temperature vs. Mole Fraction Phase Diagram Generator")
    title.grid(row=0)
    # Creating the variables storing component names
    c1 = StringVar(root)
    c1.set(component_options[0])
    c2 = StringVar(root)
    c2.set(component_options[0])
        
    # Creating component1 OptionMenu
    component1_prompt = Label(root, text="Select component 1:")
    component1_menu = OptionMenu(root, c1, *component_options)
    component1_prompt.grid(row=2, column=0)
    component1_menu.grid(row=2,column=1)
    # Creating component2 OptionMenu
    component2_prompt = Label(root, text="Select component 2:")
    component2_menu = OptionMenu(root, c2, *component_options)
    component2_prompt.grid(row=3, column=0)
    component2_menu.grid(row=3,column=1)

    
    def submitComponents():
        component1 = c1.get()
        component2 = c2.get()
        component1_menu.destroy()
        component2_menu.destroy()
        submitComponents_button.destroy()
        component1_label = Label(root, text=component1)
        component2_label = Label(root, text=component2)
        component1_label.grid(row=2,column=1)
        component2_label.grid(row=3,column=1)
    
    # Submit component values button
    submitComponents_button = Button(root, text="Confirm Components", command=submitComponents)
    submitComponents_button.grid(row=4)

    root.mainloop()

if __name__ == "__main__":
    main()