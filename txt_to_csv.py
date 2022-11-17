import csv

txt_file = 'files/Enamine_BB_Vertex_July2022_data.txt'
csv_file = 'files/Enamine_BB_Vertex_July2022_data.tsv'

with open(txt_file, 'r') as infile, open(csv_file, 'w') as outfile:
    stripped = (line.strip() for line in infile)
    lines = (line.split(",") for line in stripped if line)
    writer = csv.writer(outfile)
    writer.writerows(lines)
