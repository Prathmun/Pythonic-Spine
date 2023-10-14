#In House lIbraries
from pathandblocks import grossdisciplines

#Libraries
#Data management
import pickle
import pandas as pd
import re
#Visualization
import seaborn as sns
import matplotlib.pyplot as plt


def extract_block_data(grossdisciplines):
    data = []  # A list to store the extracted data
    
    for discipline in grossdisciplines:
        for path in discipline.paths:
            for block in path.blocks:
                try:
                    # Load block's activation history
                    blockmemory = pickle.load(open(("Blocks/" + block.name + ".py"), "rb"))
                    for activation_time in blockmemory:
                        data.append([block.name, activation_time, path.name, discipline.name])
                except IOError:
                    # Continue if the block file does not exist
                    continue
                    
    # Convert the list into a DataFrame
    df = pd.DataFrame(data, columns=["Block Name", "Activation Time", "Path Association", "Disc Association"])
    
    return df

df = extract_block_data(grossdisciplines)
print(df)
df['Disc Association'] = df['Disc Association'].astype(str)
df['Path Association'] = df['Path Association'].astype(str)


# Current time
current_time = pd.Timestamp.now()

# Time three months ago from current time
three_months_ago = current_time - pd.DateOffset(months=3)

# Filter the DataFrame to only recent
df = df[df["Activation Time"] > three_months_ago]


#Set resolution to daily
df['Activation Time'] = df['Activation Time'].dt.date

print(df.isna().sum())
print(df.dtypes)


#cause clint messses with the legend
def strip_ansi_codes(s):
    return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', s)

df['Disc Association'] = df['Disc Association'].apply(strip_ansi_codes)

def show_plots():
    # Set up the matplotlib figure and aesthetics
    sns.set_theme(style="darkgrid")

    # Create a scatter plot of activations
    plt.figure(figsize=(15, 10))
    plot = sns.scatterplot(data=df, x="Activation Time", y="Block Name", hue="Disc Association", legend="full")
    plt.title("Block Activations Over Time")

    # Adjust the y-axis labels for better readability
    plot.set_yticklabels(plot.get_yticklabels(), size=10)
    plot.legend(loc='upper left', bbox_to_anchor=(0, 1))

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

show_plots()