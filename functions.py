import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp

