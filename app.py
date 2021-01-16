import enum
from tkinter import *
from tkinter import messagebox
import pandas as pd

def removeDuplicates(og_list):
    list = []
    for item in og_list:
        list.append(item)
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

def getPossibleStates(components, states, target):
    possibleStates = []
    for index, c in enumerate(components):
        if c == target:
            if str.lower(states[index]) == 'solid':
                possibleStates.append(0)
            elif str.lower(states[index]) == 'liquid':
                possibleStates.append(1)
            elif str.lower(states[index]) == 'gas':
                possibleStates.append(2)
            else:
                raise Exception(f'Dataframe error. {states[index]} is an invalid state.')
    return possibleStates

def main():
    # Import Excel spreadsheet as dataframe
    heatCapacity_dataframe = pd.read_excel("heatCapacity.xlsx")
    # List of all components, including duplicates
    all_components = heatCapacity_dataframe['Component'].tolist()
    # Create a non-duplicate components list (default OptionMenu list @index 0)
    component_options = ['Select a component'] + removeDuplicates(all_components)
    # Create a component state list corresponding to each row in the original dataframe
    component_states = heatCapacity_dataframe['State'].tolist()

    root = Tk()
    # Creating Title Widget
    title = Label(root, text="Enthalpy Calculator - Heat of Capacity")
    title.grid(row=0, columnspan=5)
    # Creating the variables storing component names
    component1 = StringVar(root)
    component1.set(component_options[0])
    component2 = StringVar(root)
    component2.set(component_options[0])

    # Creating component1 OptionMenu
    component1_prompt = Label(root, text="Select component 1:")
    component1_menu = OptionMenu(root, component1, *component_options)
    component1_prompt.grid(row=1, column=0)
    component1_menu.grid(row=1, column=1)
    # Creating component2 OptionMenu
    component2_prompt = Label(root, text="Select component 2:")
    component2_menu = OptionMenu(root, component2, *component_options)
    component2_prompt.grid(row=1, column=3)
    component2_menu.grid(row=1, column=4)

    # Select state variables
    state1 = IntVar(root)
    state2 = IntVar(root)
    state_buttons1 = []
    state_buttons2 = []
    # Create all possible state Radiobuttons
    state_buttons1.append(Radiobutton(root, text="solid", variable=state1, value="0"))
    state_buttons1.append(Radiobutton(root, text="liquid", variable=state1, value="1"))
    state_buttons1.append(Radiobutton(root, text="gas", variable=state1, value="2"))
    state_buttons2.append(Radiobutton(root, text="solid", variable=state2, value="0"))
    state_buttons2.append(Radiobutton(root, text="liquid", variable=state2, value="1"))
    state_buttons2.append(Radiobutton(root, text="gas", variable=state2, value="2"))

    def submitStates():
        for button in state_buttons1 + state_buttons2:
            button.config(state = DISABLED)

    # Select state button and Radiobutton list
    submitStates_button = Button(root, text="Confirm States", command=submitStates)

    def createStatesForm():
        # Get a list of all possible states components 1 and 2 can be in
        possible_states1 = getPossibleStates(all_components, component_states, component1.get())
        possible_states2 = getPossibleStates(all_components, component_states, component2.get())
        # Set the default state for each Radiobutton list
        state1.set(possible_states1[0])
        state2.set(possible_states2[0])
        # Component 1 state wdigets
        currentRow = 2
        state1_prompt = Label(root, text=f'Select the state for {component1.get()}:')
        state1_prompt.grid(row=currentRow, column=0)
        for i in range(len(possible_states1)):
            state_buttons1[possible_states1[i]].grid(row=currentRow,column=1)
            currentRow += 1
        # Component 2 state widgets
        currentRow = 2
        state2_prompt = Label(root, text=f'Select the state for {component2.get()}:')
        state2_prompt.grid(row=currentRow, column=3)
        for i in range(len(possible_states2)):
            state_buttons2[possible_states2[i]].grid(row=currentRow, column=4)
            currentRow += 1
        # Grid submit component states button
        submitStates_button.grid(row=max(len(possible_states1),len(possible_states2))+2, column=2)

    def submitComponents():
        if component1.get() == 'Select a component' or component2.get() == 'Select a component':
            messagebox.showerror(title="Error", message="One or more components have not been selected. Try again.")
            return
        component1_menu.destroy()
        component2_menu.destroy()
        submitComponents_button.destroy()
        component1_label = Label(root, text=component1.get())
        component2_label = Label(root, text=component2.get())
        component1_label.grid(row=1, column=1)
        component2_label.grid(row=1, column=4)
        createStatesForm()

    # Submit component values button
    submitComponents_button = Button(root, text="Confirm Components", command=submitComponents)
    submitComponents_button.grid(row=2, column=2)

    # Set default row and column size
    col_count, row_count = root.grid_size()
    for col in range(col_count):
        root.grid_columnconfigure(col, minsize=100)
    for row in range(row_count):
        root.grid_rowconfigure(row, minsize=10)

    root.mainloop()

if __name__ == "__main__":
    main()