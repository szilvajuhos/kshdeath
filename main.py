import click
import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--csv', '-c', type=str, help='CSV file from https://www.ksh.hu/stadat_files/nep/en/nep0065.html in CSV format', required=True)

def do_plotting(csv):

    df = read_csv(csv, parse_dates=['date'])
    dates = df["date"]
    df = df.drop(columns=["date"])
    age_intervals = list(df.columns)

    normalized_df = (df-df.mean())#/df.std()
    # we are assuming dates are ordered
    plt.pcolormesh(normalized_df.T,cmap=plt.cm.get_cmap('gnuplot'))
    c = np.arange(1,len(dates)+1,52)
    x_dates = dates[c]
    plt.xticks(c, x_dates.dt.strftime("%Y"), rotation='vertical')
    plt.yticks(np.arange(0.5, len(age_intervals), 1), age_intervals)
    plt.colorbar()
    plt.savefig("image.png")
    plt.show()



if __name__ == "__main__":
    do_plotting()
