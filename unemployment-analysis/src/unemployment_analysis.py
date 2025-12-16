import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def analyze_unemployment(df):
    print("Average Unemployment Rate:", df['Estimated Unemployment Rate (%)'].mean())
    covid_period = df[df['Date'].dt.year == 2020]
    print("Covid Period Average Unemployment:", covid_period['Estimated Unemployment Rate (%)'].mean())

def visualize(df):
    plt.figure()
    plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate (%)")
    plt.title("Unemployment Trend Over Time")
    plt.show()

if __name__ == "__main__":
    df = load_data("data/Unemployment_in_India.csv")
    analyze_unemployment(df)
    visualize(df)
