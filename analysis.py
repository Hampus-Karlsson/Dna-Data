import matplotlib.pyplot as plt

# Funktions to read DNA-secuence from file
def läs_dna_filen(filnamn):
    dna_data = {}  # Dictionary to read from
    with open(filnamn, "r") as fil:
        current_id = None
        current_sequence = ""

        for row in fil:
            row = row.strip()
            if row.startswith(">"):  # If the row starts with ">" it's an ID
                if current_id:  
                    dna_data[current_id] = current_sequence.lower()
                current_id = row[1:]  # remove ">" to get the ID
                current_sequence = ""  # restore sequense
            else:
                current_sequence += row  # Add DNA-sequense

        if current_id:  # save last 
            dna_data[current_id] = current_sequence.lower()

    return dna_data

# Count A, T, C, G 
def Read_base(sequens):
    return {
        "A": sequens.count("a"),
        "T": sequens.count("t"),
        "C": sequens.count("c"),
        "G": sequens.count("g"),
    }

# Plot frequens
def plot_frequens(dna_dict):
    for seq_id, sequence in dna_dict.items():
        bas_frekvens = Read_base(sequence)

        # Diagram
        plt.figure(figsize=(6, 4))
        plt.bar(bas_frekvens.keys(), bas_frekvens.values(), color=["yellow", "red", "blue", "green"], edgecolor="black")

        # Names
        plt.xlabel("Bas")
        plt.ylabel("Frequens")
        plt.title(f"Frequens of DNA-base ({seq_id})")
        plt.grid(axis='y', linestyle="--", alpha=0.7)

        # print graph
        plt.show()

# Mainprogram
filename = "dna_raw.txt" 
dna_dict = läs_dna_filen(filename)
plot_frequens(dna_dict)
