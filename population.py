import pandas as pd

def main():
    # Data source: https://en.wikipedia.org/wiki/Demographic_history_of_New_York_City
    nyc_pop = {
        1900: 3437202,
        1910: 4766883,	
        1920: 5620048,	
        1930: 6930446,	
        1940: 7454995,	
        1950: 7891957,	
        1960: 7781984,
        1970: 7894862,
        1980: 7071639,
        1990: 7322564,
        2000: 8008278,
        2010: 8175133,
        2020: 8804190  
    }

    population_series = pd.Series(nyc_pop)
    growth_rate = population_series.pct_change().iloc[1:] * 100  

    avg_growth = growth_rate.mean()
    max_growth = growth_rate.max()
    min_growth = growth_rate.min()
    std_growth = growth_rate.std()

    population_change = population_series[2020] - population_series[1920]
    percent_change = (population_change / population_series[1920]) * 100

    mean_growth_rate = growth_rate.mean()
    predicted_2030 = population_series[2020] * (1 + mean_growth_rate / 100)
    predicted_2100 = predicted_2030 * (1 + mean_growth_rate / 100) ** 7  # 7 more decades

    print(f"Avg growth rate: {avg_growth:.2f}%")
    print(f"Max growth rate: {max_growth:.2f}%")
    print(f"Min growth rate: {min_growth:.2f}%")
    print(f"Std dev of growth rate: {std_growth:.2f}")
    print(f"Population in 2020: {population_series[2020]}")
    print(f"Population change (1920-2020): {population_change}")
    print(f"Percent change (1920-2020): {percent_change:.2f}%")
    print(f"Predicted population in 2030: {predicted_2030:.0f}")
    print(f"Predicted population in 2100: {predicted_2100:.0f}")

if __name__ == '__main__':
    main()
