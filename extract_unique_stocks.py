import pandas as pd

def extract_unique_stock_codes():
    try:
        # Read the Excel file
        print("Reading concatenated_stock_data_v1.xlsx...")
        df = pd.read_excel('concatenated_stock_data_v1.xlsx')
        
        print(f"Excel file loaded successfully!")
        print(f"Shape of the data: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Look for stock code column
        possible_columns = ['stock_code', 'Symbol', 'SYMBOL', 'symbol', 'Stock', 'STOCK', 'stock', 'Code', 'CODE', 'code']
        
        stock_column = None
        for col in possible_columns:
            if col in df.columns:
                stock_column = col
                break
        
        if stock_column is None:
            print("\nNo stock code column found. Available columns:")
            for i, col in enumerate(df.columns):
                print(f"{i+1}. {col}")
            return
        
        print(f"\nUsing column: {stock_column}")
        
        # Get unique stock codes
        unique_stocks = sorted(df[stock_column].unique())
        
        print(f"\n=== UNIQUE STOCK CODES ({len(unique_stocks)}) ===")
        for i, stock in enumerate(unique_stocks, 1):
            print(f"{i:3d}. {stock}")
        
        # Save to text file
        with open('unique_stock_codes.txt', 'w') as f:
            f.write("Unique Stock Codes from concatenated_stock_data_v1.xlsx\n")
            f.write("=" * 50 + "\n\n")
            for i, stock in enumerate(unique_stocks, 1):
                f.write(f"{i:3d}. {stock}\n")
        
        print(f"\n✅ Unique stock codes saved to 'unique_stock_codes.txt'")
        
        # Create SQL query for missing stocks
        print(f"\n=== SQL QUERY TO CHECK MISSING STOCKS ===")
        print("-- Replace 'your_table_name' with your actual table name")
        print("-- This query will show which stocks from your list are missing in the database")
        print()
        
        sql_query = f"""
-- Check which stocks from your list are missing in the database
WITH expected_stocks AS (
"""
        
        # Add your stock codes to the SQL query
        for stock in stock_codes:
            sql_query += f"    SELECT '{stock}' as stock_code UNION ALL\n"
        
        # Remove the last UNION ALL and close the CTE
        sql_query = sql_query.rstrip(" UNION ALL\n") + "\n)\n"
        
        sql_query += """SELECT es.stock_code, 
       CASE WHEN db.stock_code IS NULL THEN 'MISSING' ELSE 'FOUND' END as status
FROM expected_stocks es
LEFT JOIN (
    SELECT DISTINCT stock_code 
    FROM your_table_name
) db ON es.stock_code = db.stock_code
ORDER BY es.stock_code;
"""
        
        print(sql_query)
        
        # Save SQL query to file
        with open('check_missing_stocks.sql', 'w') as f:
            f.write(sql_query)
        
        print(f"✅ SQL query saved to 'check_missing_stocks.sql'")
        
        # Show comparison with your original list
        print(f"\n=== COMPARISON WITH YOUR LIST ===")
        your_list_set = set(stock_codes)
        excel_set = set(unique_stocks)
        
        found_in_excel = your_list_set.intersection(excel_set)
        missing_from_excel = your_list_set - excel_set
        extra_in_excel = excel_set - your_list_set
        
        print(f"Stocks in your list: {len(your_list_set)}")
        print(f"Stocks found in Excel: {len(found_in_excel)}")
        print(f"Stocks missing from Excel: {len(missing_from_excel)}")
        print(f"Extra stocks in Excel: {len(extra_in_excel)}")
        
        if missing_from_excel:
            print(f"\n=== MISSING FROM EXCEL ===")
            for stock in sorted(missing_from_excel):
                print(f"❌ {stock}")
        
        if extra_in_excel:
            print(f"\n=== EXTRA IN EXCEL (first 20) ===")
            for stock in sorted(list(extra_in_excel)[:20]:
                print(f"➕ {stock}")
            if len(extra_in_excel) > 20:
                print(f"... and {len(extra_in_excel) - 20} more")
        
    except Exception as e:
        print(f"Error: {e}")

# Stock codes from your list
stock_codes = [
    'CNXBAN', 'NIFFIN', 'NIFNEX', 'NIFSEL', 'NIFTY', 'AARIND', 'ABB', 'ACC', 'ADAENT', 'ADAGAS', 'ADAGRE', 'ADAPOR',
    'ADATRA', 'ADICAP', 'ADIFAS', 'ALKLAB', 'AMBCE', 'ANGBRO', 'APLAPO', 'APOHOS', 'APOTYR', 'ASHLEY', 'ASIPAI',
    'ASTPOL', 'AURPHA', 'AUSMA', 'AVESUP', 'AXIBAN', 'BAAUTO', 'BAFINS', 'BAJFI', 'BALIND', 'BANBAN', 'BANBAR',
    'BANIND', 'BERPAI', 'BHAAIR', 'BHAELE', 'BHAFOR', 'BHAINF', 'BHAPET', 'BHEL', 'BIOCON', 'BOSLIM', 'BRIIND', 'BSE',
    'CADHEA', 'CANBAN', 'CDSL', 'CESC', 'CHAFER', 'CHOINV', 'CIPLA', 'COALIN', 'COLPAL', 'COMAGE', 'CONCOR', 'CROGR',
    'CROGRE', 'CUMIND', 'CYILIM', 'DABIND', 'DEENIT', 'DELLIM', 'DIVLAB', 'DIXTEC', 'DLFLIM', 'DRREDD', 'EICMOT',
    'ESCORT', 'EXIIND', 'FEDBAN', 'FSNECO', 'GAIL', 'GLEPHA', 'GMRINF', 'GODCON', 'GODPRO', 'GRANUL', 'GRASIM',
    'HAVIND', 'HCLTEC', 'HDFAMC', 'HDFBAN', 'HDFSTA', 'HERHON', 'HIMFUT', 'HINAER', 'HINCOP', 'HINDAL', 'HINLEV',
    'HINPET', 'HINZIN', 'HUDCO', 'ICIBAN', 'ICILOM', 'ICIPRU', 'IDECEL', 'IDFBAN', 'IIFHOL', 'INDBA', 'INDEN',
    'INDGAS', 'INDHOT', 'INDIBA', 'INDOIL', 'INDR', 'INDRAI', 'INDREN', 'INFEDG', 'INFTEC', 'INOWIN', 'INTAVI',
    'IRBINF', 'ITC', 'JINSP', 'JINSTA', 'JIOFIN', 'JSWENE', 'JSWSTE', 'JUBFOO', 'KALJEW', 'KEIIND', 'KOTMAH',
    'KPITE', 'KPITEC', 'LARTOU', 'LAULAB', 'LIC', 'LICHF', 'LTFINA', 'LTINFO', 'LUPIN', 'MACDEV', 'MAGFI',
    'MAHFIN', 'MAHGAS', 'MAHMAH', 'MANAFI', 'MARLIM', 'MARUTI', 'MAXFIN', 'MAXHEA', 'MCX', 'MOTSUM', 'MPHLIM',
    'MRFTYR', 'MUTFIN', 'NAGCON', 'NATALU', 'NATMIN', 'NBCC', 'NESIND', 'NHPC', 'NIITEC', 'NTPC', 'OBEREA',
    'ODICEM', 'OILIND', 'ONE97', 'ONGC', 'ORAFIN', 'PAGIND', 'PBFINT', 'PERSYS', 'PETLNG', 'PHOMIL', 'PIDIND',
    'PIIND', 'PIRENT', 'PNBHOU', 'POLI', 'POWFIN', 'POWGRI', 'PREEST', 'PUNBAN', 'RAMCEM', 'RBLBAN', 'RELIND',
    'RUCSOY', 'RURELE', 'SAIL', 'SBICAR', 'SBILIF', 'SHRCEM', 'SHRTRA', 'SIEMEN', 'SJVLIM', 'SOLIN', 'SONBLW',
    'SRF', 'STABAN', 'SUNPHA', 'SUPIND', 'SYNINT', 'TATCHE', 'TATCOM', 'TATELX', 'TATGLO', 'TATMOT', 'TATPOW',
    'TATSTE', 'TATTEC', 'TCS', 'TECMAH', 'TITIND', 'TITWAG', 'TORPHA', 'TORPOW', 'TRENT', 'TUBIN', 'TVSMOT',
    'ULTCEM', 'UNIBAN', 'UNIP', 'UNISPI', 'VARBEV', 'VEDLIM', 'VOLTAS', 'WIPRO', 'YESBAN', 'ZOMLIM'
]

if __name__ == "__main__":
    extract_unique_stock_codes()

