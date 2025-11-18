import matplotlib.pyplot as plt

def make_plots(df):
    """
    Input: a DataFrame with columns "sex", "weight", "systolic_bp", and "smoker".
    Output: a figure with 3 subplots, side by side.
    """
    fig, ax = plt.subplots(1,3, figsize=(12,5)) # 3 plots i samma figur

    # Plot längst till vänster 
    # (histogram över blodtryck)
    ax[0].hist(df["systolic_bp"], bins=25, edgecolor="black",color="cyan")
    ax[0].set_title("Blodtryck: fördelning av värden")

    # Plot i mitten 
    # (boxplot, vikt per kön)
    gender_weights = [df[df['sex']=="M"]['weight'], df[df['sex']=="F"]['weight']] # lista med män's vikt och kvinnor's vikt
    ax[1].boxplot(gender_weights, tick_labels=['Male','Woman'])
    ax[1].set_title("Vikt per kön - fördelning")

    # Plot till höger 
    # (stapeldiagram: andelen rökare)
    quantity_smokers = df['smoker'].value_counts() # räknar hur många "Yes" och "No" i kolumnen 'smoker'
    ax[2].bar(quantity_smokers.index, quantity_smokers.values, edgecolor="black", color=["blue","red"])
    ax[2].set_title("Hur många som röker")

    plt.tight_layout()
    plt.show()

    return fig, ax