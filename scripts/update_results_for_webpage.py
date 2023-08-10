from scripts.sst_monthly_mean_anomalies import compute_monthly_anomalies
from scripts.trend_estimation import calc_trend
from scripts.plot_lightstation_temperature import run_plot

"""
This sample script updates the SST results that are presented on the webpage.
After running the update the plots should automatically show up on the webpage unless 
the names of the plot files changed.
Note that there are some numbers within the text of the webpage that will need to be
updated by hand, comparing the trends of the abridged and entire records for some stations.
"""

# # Calculate monthly mean anomalies from monthly mean observations using the climatologies for each
# # station for 1991-2020
# compute_monthly_anomalies(obs_data_suffix='MonthlyTemp.csv')
#
# # Calculate least-squares trends, Theil-Sen trends, and confidence intervals on the least-squares
# # trends using the Monte Carlo approach from Cummins & Masson (2014)
# calc_trend(
#     search_string="monthly_anom_from_monthly_mean.csv",
#     max_siml=500,  # As you increase the number of simulations to run, the longer it will take
#     ncores_to_use=None,  # Only an option for scikit-learn Theil-Sen method
#     sen_flag=0  # Use Patrick Cummins' code (translated from MatLab) to calculate the Theil-Sen trends
# )

# Make several different kinds of plots, which are presented on the github webpage
run_plot(
    plot_monthly_anom=True,
    plot_clim=True,
    plot_daily_anom=True,
    plot_daily_anom_window=21,  # unit=days
    plot_daily_stats=True,
    plot_availability=True
)
