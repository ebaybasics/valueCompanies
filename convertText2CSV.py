def text_to_csv_table(text_table):
    # split the text table into rows
    rows = text_table.strip().split('\n')

    # split the first row (header) into columns
    columns = rows[0].split('\t')

    # initialize the csv table with the header
    csv_table = ','.join(columns) + '\n'

    # iterate over the remaining rows
    for row in rows[1:]:
        # split the row into columns
        values = row.split('\t')

        # replace empty values with "NA" and remove dollar signs
        for i in range(len(values)):
            if not values[i].strip():
                values[i] = "NA"
            else:
                values[i] = values[i].replace('$', '')
                values[i] = values[i].replace('%', '')

        # add the row to the csv table
        csv_table += ','.join(values) + '\n'

    return csv_table


