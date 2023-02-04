import os
import json

def xyz_to_json(folder_path):
    # Create a dictionary to store the structures
    structures = {}
    # Loop through all xyz files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".xyz"):
            # Get the structure name without the '.xyz' extension
            structure_name = filename[:-4]
            # Open the xyz file
            with open(os.path.join(folder_path, filename), 'r') as xyzfile:
                # Read the number of atoms from the first line
                num_atoms = int(xyzfile.readline().strip())
                # Read the comment line from the second line
                comment = xyzfile.readline().strip()
                # Create a list to store the atoms for this structure
                atoms = []
                # Loop through the remaining lines
                for i in range(num_atoms):
                    # Read the atom type and coordinates
                    line = xyzfile.readline().strip().split()
                    atom_type = line[0]
                    x = float(line[1])
                    y = float(line[2])
                    z = float(line[3])
                    # Add the atom to the list
                    atoms.append({'element': atom_type, 'x': x, 'y': y, 'z': z})
                # Add the structure to the dictionary
                structures[structure_name] = {'name': structure_name, 'atoms': atoms}
    # Write the structures to a JSON file
    with open('xyz_structures.json', 'w') as jsonfile:
        json.dump(structures, jsonfile, indent=4)

# Call the function and pass the folder path as an argument
xyz_to_json('YOUR_FOLDER_PATH')