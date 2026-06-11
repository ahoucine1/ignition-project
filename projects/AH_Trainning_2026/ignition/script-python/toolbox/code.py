def read_csv_to_pydataset():
    import csv
    
    # Open file chooser
    path = system.file.openFile("csv")
    
    # Check if user cancelled
    if path is None:
        print("No file selected")
        return None
    
    data = []
    headers = []
    
    try:
        # Use context manager for proper file handling
        with open(path, 'r') as file:
            csvData = csv.reader(file)
            headers = next(csvData)  # Get headers from first row
            
            # Read data rows
            for row in csvData:
                data.append(row)
        
        # Convert to Ignition dataset
        ds = system.dataset.toDataSet(headers, data)
        pds = system.dataset.toPyDataSet(ds)
        
        print("Successfully loaded {len(data)} rows from CSV")
        return pds
        
    except Exception as e:
        print("Error reading CSV file: {str(e)}")
        return None
    finally:
        # Ensure file is closed (though 'with' statement handles this)
        pass
    
def populate_dbtable_from_pydataset(pds, dbTable, dbConn, maxRecs):
    cols = pds.getColumnCount()
    rows = pds.getRowCount()

    # clear DB table each time
    queryStr = "TRUNCATE TABLE {:s}".format(dbTable)
    system.db.runUpdateQuery(queryStr, dbConn)

    # no inserts if no data
    if (rows > 0):

        # set up insert query string with proper placeholders
        pholders = ",".join(["?"] * cols)  # Creates "?,?,?" based on column count
        queryStr = "INSERT INTO {:s} VALUES ({:s})".format(dbTable, pholders)
    
        # indices for first N records
        minIdx = 0
        maxIdx = min(maxRecs, rows)
    
        # DB inserts in batches of N
        while minIdx < rows:
            queryData = []
            
            # Collect all rows in this batch with proper type conversion
            for row in pds[minIdx:maxIdx]:
                # Convert each row to a list of values with proper types
                rowData = []
                for col in range(cols):
                    value = row[col]
                    # Convert first column (ID) to integer if it's the ID column
                    if col == 0:  # Assuming first column is ID
                        try:
                            value = int(value)
                        except (ValueError, TypeError):
                            pass
                    rowData.append(value)
                queryData.extend(rowData)
            
            # Create placeholders for this batch
            batch_placeholders = ",".join(["(" + pholders + ")"] * len(pds[minIdx:maxIdx]))
            batch_query = "INSERT INTO {:s} VALUES {:s}".format(dbTable, batch_placeholders)
            
            # Insert batch into DB
            if queryData:
                system.db.runPrepUpdate(batch_query, queryData, dbConn)
            
            # advance indices for next batch
            minIdx = maxIdx
            maxIdx = min(maxIdx + maxRecs, rows)