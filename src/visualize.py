import matplotlib.pyplot as plt
import pandas as pd

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

def plot_delay_distribution(df):

    df["ARRIVAL_DELAY"].hist(bins=50)

    plt.title("Distribution of Arrival Delays")
    plt.xlabel("Delay (minutes)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig("outputs/delay_distribution.png")

    plt.show()

def plot_top_delayed_airports(df):

    plt.figure(figsize=(12,6))

    df["label"] = df["AIRPORT"] + " (" + df["STATE"] + ")"

    df.plot(
        kind="bar",
        x="label",
        y="avg_delay",
        legend=False
    )

    plt.title("Top Airports by Departure Delay")
    plt.xlabel("Airport")
    plt.ylabel("Average Delay (minutes)")

    plt.xticks(rotation=30, ha="right")

    plt.tight_layout()

    plt.savefig("outputs/top_delayed_airports.png")

    plt.show()

def plot_cancellation_rate(df):

    df.plot(
        kind="bar",
        x="AIRLINE",
        y="cancellation_rate",
        legend=False
    )

    plt.title("Cancellation Rate by Airline")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("outputs/cancellation_rate.png")

    plt.show()

def plot_delay_map(df):

    plt.figure(figsize=(10,6))

    scatter = plt.scatter(
        df["LONGITUDE"],
        df["LATITUDE"],
        s=df["flight_count"] / 50,
        c=df["avg_delay"],
        cmap="coolwarm",
        alpha=0.7
    )

    plt.colorbar(scatter, label="Average Delay (minutes)")

    plt.title("Airport Delays Across the United States")

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.tight_layout()

    plt.savefig("outputs/delay_map_airports.png")

    plt.show()

def plot_delay_heatmap(df):

    pivot = df.pivot(
        index="DAY_OF_WEEK",
        columns="MONTH",
        values="avg_delay"
    )

    plt.figure(figsize=(10,6))

    plt.imshow(pivot, aspect="auto")

    plt.colorbar(label="Average Delay (minutes)")

    plt.xticks(range(12), range(1,13))
    plt.yticks(range(7), range(1,8))

    plt.xlabel("Month")
    plt.ylabel("Day of Week")

    plt.title("Average Flight Delay Heatmap")

    plt.tight_layout()

    plt.savefig("outputs/delay_heatmap.png")

    plt.show()