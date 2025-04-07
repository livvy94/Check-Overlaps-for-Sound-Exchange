import pandas

# Put your file here!
filename = ""

df = pandas.read_csv(filename, sep='\t', parse_dates=['Start Time', 'End Time'])

for i in range(len(df) - 1):
    current_end_time = df.iloc[i]['End Time']
    next_start_time = df.iloc[i + 1]['Start Time']

    if current_end_time >= next_start_time:
        overlap_duration = round((current_end_time - next_start_time).total_seconds())
        print(f"Overlap detected between '{df.iloc[i]['Title']}' and '{df.iloc[i + 1]['Title']}' ({overlap_duration} sec)")
