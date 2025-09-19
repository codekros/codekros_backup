import pandas as pd

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

def check_stock_codes_in_excel():
    try:
        # Read the Excel file
        print("Reading concatenated_stock_data_v1.xlsx...")
        df = pd.read_excel('concatenated_stock_data_v1.xlsx')
        
        print(f"Excel file loaded successfully!")
        print(f"Shape of the data: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Check if there's a column that might contain stock codes
        # Based on the codebase, it should be 'stock_code'
        possible_columns = ['stock_code', 'Symbol', 'SYMBOL', 'symbol', 'Stock', 'STOCK', 'stock', 'Code', 'CODE', 'code']
        
        stock_column = None
        for col in possible_columns:
            if col in df.columns:
                stock_column = col
                break
        
        if stock_column is None:
            # If no obvious column found, show first few rows to help identify
            print("\nNo obvious stock code column found. First few rows:")
            print(df.head())
            print("\nPlease check the column names above and update the script accordingly.")
            return
        
        print(f"\nUsing column: {stock_column}")
        
        # Get unique stock codes from the Excel file
        excel_stocks = set(df[stock_column].unique())
        print(f"Total unique stocks in Excel: {len(excel_stocks)}")
        
        # Check which stocks from your list are in the Excel file
        found_stocks = []
        missing_stocks = []
        
        for stock in stock_codes:
            if stock in excel_stocks:
                found_stocks.append(stock)
            else:
                missing_stocks.append(stock)
        
        print(f"\n=== RESULTS ===")
        print(f"Stocks FOUND in Excel: {len(found_stocks)}")
        print(f"Stocks MISSING from Excel: {len(missing_stocks)}")
        
        print(f"\n=== FOUND STOCKS ({len(found_stocks)}) ===")
        for stock in sorted(found_stocks):
            print(stock)
            
        print(f"\n=== MISSING STOCKS ({len(missing_stocks)}) ===")
        for stock in sorted(missing_stocks):
            print(stock)
            
        # Show some sample data from the Excel file
        print(f"\n=== SAMPLE DATA FROM EXCEL ===")
        print(df.head(10))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_stock_codes_in_excel()
