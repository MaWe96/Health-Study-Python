import matplotlib.pyplot as plt

def bonus_plot_bp_age(df, ax):
    """
    Bonus graf från del 1: En scatterplot ålder vs blodtryck, med rullande medel, och könsfördelade punkter för extra nyans.
    Fick ändra på koden från ax.figure() till fig, ax = ax.subplots(), och lägga till ax som input argument.
    Returnerar fig, ax.
    """
    gendercolors = df.sex.map({"F":"lightpink", "M":"cyan"})
    ax.scatter(df['age'], df['systolic_bp'], c=gendercolors, alpha=0.6, label="Personer's värden")
    ax.set_title("Ålder per kön vs. Blodtryck")
    ax.set_xlabel("Ålder")
    ax.set_ylabel("Blodtryck")

    # Lägga till rullande medel
    sorted = df[['age','systolic_bp']].sort_values('age') # sortera åldrarna stigande.
    roll_mean = sorted['systolic_bp'].rolling(window=30).mean() # 30 första värden visar där rullande medel ska starta.

    ax.plot(sorted['age'], roll_mean, linewidth=3, color="lightgreen", label="Rullande medelvärde")


def bonus_plot_sick_healthy(df, ax):
    """
    Del2 (new)
    Beräknar rullande medel och plottar en stapelgraf av hur många som är friska och sjuka per kön.
    """

    # Först lite beräkningar.
    # Kollar antalet sjuka män & kvinnor.
    sick_men = len(df.loc[(df['sex']=="M") & (df["disease"]==1)])
    sick_women = len(df.loc[(df['sex']=="F") & (df["disease"]==1)])
    sick_count = sick_men + sick_women

    # Hur många som är friska
    healthy_men   = len(df.loc[df['sex']=="M"]) - sick_men
    healthy_women = len(df.loc[df['sex']=="F"]) - sick_women

    total_men = sick_men + healthy_men
    total_women = sick_women + healthy_women

    # Man kan göra en pandas DataFrame och ge som output, men grafen visar dessa siffror tillräckligt.
    # print("Antal män totalt: ", total_men, ", antal kvinnor totalt: ", total_women)
    # print("")
    # print("Antal sjuka män: ", sick_men,", antal sjuka kvinnor: ", sick_women)
    # print("")
    # print(f"Friska män: {healthy_men}, Friska kvinnor: {healthy_women}, Antal sjuka totalt: {sick_count}")
    # print("")

    # Göra graf
    ax.bar(['Män', 'Kvinnor'], [healthy_men, healthy_women], label='Friska', color='green', alpha=0.5)
    ax.bar(['Män', 'Kvinnor'], [sick_men, sick_women], bottom=[healthy_men, healthy_women], label='Sjuka', color='purple')
    #       bottom = argument varpå man kan stapla ytterligare värden, på tidigare plottade staplar. Jag staplar sjuka personerna ovanpå de friska.

    ax.set_ylabel('Antal personer')
    ax.set_title('Sjuka vs. friska')
    ax.legend(loc="center")