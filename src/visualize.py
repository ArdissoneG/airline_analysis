import matplotlib.pyplot as plt


def plot_delays_by_airline(df):

    df.plot(
        kind="bar",
        x="AIRLINE",
        y="avg_delay",
        legend=False
    )

    plt.title("Average Arrival Delay by Airline")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/delays_by_airline.png")
    plt.show()
    

def plot_monthly_delay(df):

    df.plot(
        x="MONTH",
        y="avg_arrival_delay"
    )

    plt.title("Monthly Delay Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/monthly_delay.png")
    plt.show()