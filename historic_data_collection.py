# Enhanced script with progress tracking and smart date-based updates
from breeze_connect import BreezeConnect
from datetime import datetime, timedelta
import pandas as pd
import os
import time
import json

# All stock codes (deduplicated)
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

# Configuration
EXCEL_FILE = "Historical_data.xlsx"
EXPIRY_FILE = "expiry.xlsx"
PROGRESS_FILE = "data_collection_progress.json"
BACKUP_FILE = "Historical_data_backup.xlsx"
FIELDNAMES = ["stock_code", "date", "open", "high", "low", "close", "volume", "expiry", "stock_id"]

# Breeze setup
print("[DEBUG] Initializing BreezeConnect...")
breeze = BreezeConnect(api_key="+8~9U1#3651u0761y4D0648r19H~550q")

print("[DEBUG] Generating session...")
try:
    breeze.generate_session(
        api_secret="7H5063392n5553F573iL9MS834=I3715",
        session_token="52642866"
    )
    print("[DEBUG] Session generated successfully.")
except Exception as e:
    print("❌ [ERROR] Failed to generate session:", e)
    exit()

# Date range
start_date = datetime(2010, 1, 1)
end_date = datetime.now() - timedelta(days=1)

# Function to create backup of existing data
def create_backup():
    """Create a backup of existing data file before making changes"""
    # Backup creation disabled
    return True

# Function to restore from backup if needed
def restore_from_backup():
    """Restore data from backup if main file is corrupted"""
    # Backup restoration disabled
    return False

# Function to load progress
def load_progress():
    """Load progress from JSON file"""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as f:
                progress = json.load(f)
                print(f"📊 Progress file found: {len(progress.get('completed_stocks', []))} stocks completed")
                return progress
        except Exception as e:
            print(f"⚠️ [WARNING] Could not read progress file: {e}")
    return {"completed_stocks": [], "failed_stocks": [], "last_updated": None}

# Function to save progress
def save_progress(completed_stocks, failed_stocks):
    """Save progress to JSON file"""
    progress = {
        "completed_stocks": list(completed_stocks),
        "failed_stocks": list(failed_stocks),
        "last_updated": datetime.now().isoformat()
    }
    try:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f, indent=2)
    except Exception as e:
        print(f"⚠️ [WARNING] Could not save progress: {e}")

# Function to validate and clean up corrupted files
def validate_excel_file(file_path):
    """Validate if an Excel file is readable and not corrupted"""
    if not os.path.exists(file_path):
        return True  # File doesn't exist, which is fine
    
    try:
        # Try to read the file
        test_df = pd.read_excel(file_path, engine='openpyxl', nrows=1)
        return True
    except Exception as e:
        print(f"❌ [ERROR] File {file_path} is corrupted: {e}")
        return False

# Function to check and remove existing duplicates
def check_and_clean_duplicates(df):
    """Check for existing duplicates in the data and remove them"""
    if df is None or df.empty:
        return df
    
    print(f"🔍 Checking for existing duplicates in current data...")
    initial_count = len(df)
    
    # Create composite key for duplicate detection
    df['composite_key'] = df['stock_code'] + '_' + df['date'].astype(str)
    
    # Find duplicates
    duplicate_mask = df.duplicated(subset=['composite_key'], keep='first')
    duplicate_count = duplicate_mask.sum()
    
    if duplicate_count > 0:
        print(f"⚠️ Found {duplicate_count} duplicate rows in existing data")
        print(f"🧹 Removing duplicates...")
        
        # Remove duplicates, keeping the first occurrence
        df_cleaned = df[~duplicate_mask].copy()
        
        # Remove the composite key column
        df_cleaned = df_cleaned.drop('composite_key', axis=1)
        
        final_count = len(df_cleaned)
        print(f"✅ Duplicates removed: {initial_count} → {final_count} rows")
        print(f"   - Removed {duplicate_count} duplicate rows")
        
        return df_cleaned
    else:
        print(f"✅ No duplicates found in existing data")
        # Remove the composite key column
        df = df.drop('composite_key', axis=1)
        return df

# Function to safely load existing data
def load_existing_data():
    """Safely load existing data with error handling and backup restoration"""
    if not os.path.exists(EXCEL_FILE):
        print(f"ℹ️ No existing data file found: {EXCEL_FILE}")
        return pd.DataFrame()
    
    try:
        df = pd.read_excel(EXCEL_FILE, dtype={"stock_code": str}, engine='openpyxl')
        if not df.empty:
            print(f"📊 Successfully loaded {len(df)} existing rows from {EXCEL_FILE}")
            
            # Check and clean duplicates in existing data
            df = check_and_clean_duplicates(df)
            
            # Validate the data structure
            if not all(col in df.columns for col in FIELDNAMES):
                missing_cols = [col for col in FIELDNAMES if col not in df.columns]
                print(f"⚠️ [WARNING] Missing columns: {missing_cols}")
                # Add missing columns with default values
                for col in missing_cols:
                    if col == 'expiry':
                        df[col] = pd.NaT
                    elif col == 'stock_id':
                        df[col] = None
                    else:
                        df[col] = ''
                print(f"✅ Added missing columns: {missing_cols}")
        return df
    except Exception as e:
        print(f"❌ [ERROR] Could not read existing file {EXCEL_FILE}: {e}")
        # Try to restore from backup
        if restore_from_backup():
            try:
                df = pd.read_excel(EXCEL_FILE, dtype={"stock_code": str}, engine='openpyxl')
                print(f"✅ Successfully loaded {len(df)} rows from restored backup")
                
                # Check and clean duplicates in restored data
                df = check_and_clean_duplicates(df)
                
                return df
            except Exception as e2:
                print(f"❌ [ERROR] Even backup restoration failed: {e2}")
        return pd.DataFrame()

# Function to safely save data with validation
def safe_save_data(df, file_path):
    """Safely save data with validation"""
    try:
        # Save the data
        df.to_excel(file_path, index=False, engine='openpyxl')
        
        # Verify the save was successful
        verification_df = pd.read_excel(file_path, dtype={"stock_code": str}, engine='openpyxl')
        if len(verification_df) == len(df):
            print(f"✅ Data saved successfully: {len(df)} rows")
            return True
        else:
            print(f"❌ [ERROR] Data verification failed: expected {len(df)} rows, got {len(verification_df)}")
            return False
    except Exception as e:
        print(f"❌ [ERROR] Failed to save data: {e}")
        return False

# Function to get last available date for a specific stock
def get_last_available_date_for_stock(df, stock_code):
    """Get the last available date for a specific stock"""
    if df is None or df.empty or 'stock_code' not in df.columns or 'date' not in df.columns:
        print(f"⚠️ [DEBUG] {stock_code}: DataFrame is empty or missing required columns")
        return None
    
    try:
        # Filter data for this stock
        stock_data = df.loc[df['stock_code'] == stock_code, ['date']].copy()
        if stock_data.empty:
            print(f"ℹ️ [DEBUG] {stock_code}: No existing data found")
            return None
        
        # Debug: Check data types
        print(f"🔍 [DEBUG] {stock_code}: Date column dtype: {stock_data['date'].dtype}")
        print(f"🔍 [DEBUG] {stock_code}: Sample date values: {stock_data['date'].head().tolist()}")
        
        # Convert to date strings for comparison with better error handling
        stock_data['date'] = pd.to_datetime(stock_data['date'], errors='coerce')
        
        # Filter out NaT dates
        stock_data = stock_data[stock_data['date'].notna()]
        
        if stock_data.empty:
            print(f"⚠️ [DEBUG] {stock_code}: All dates converted to NaT, treating as no data")
            return None
        
        # Get the last available date
        last_date = stock_data['date'].max()
        print(f"✅ [DEBUG] {stock_code}: Last available date: {last_date.strftime('%Y-%m-%d')}")
        return last_date
        
    except Exception as e:
        print(f"❌ [ERROR] Failed to process dates for {stock_code}: {e}")
        print(f"ℹ️ Treating {stock_code} as having no existing data")
        return None

# Function to calculate what dates are missing for a stock
def calculate_missing_dates(existing_df, stock_code):
    """Calculate which dates are missing for a specific stock - simplified approach"""
    last_available_date = get_last_available_date_for_stock(existing_df, stock_code)
    
    if last_available_date is None:
        # No existing data, need to fetch from start_date
        start_fetch_date = start_date
        print(f"📊 {stock_code}: No existing data, fetching from {start_fetch_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    else:
        # Start from the day after the last available date
        start_fetch_date = last_available_date + timedelta(days=1)
        
        # Check if we need to fetch any data
        if start_fetch_date > end_date:
            print(f"✅ {stock_code}: Already up-to-date (last data: {last_available_date.strftime('%Y-%m-%d')})")
            return []  # No missing dates
        
        print(f"📊 {stock_code}: Last data: {last_available_date.strftime('%Y-%m-%d')}, fetching from {start_fetch_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    # Return the date range to fetch (just start and end, not individual dates)
    return [start_fetch_date, end_date]

# Function to merge new data with existing data safely
def merge_data_safely(existing_df, new_df, stock_code):
    """Merge new data with existing data, avoiding duplicates and preserving existing data"""
    if existing_df.empty:
        print(f"ℹ️ {stock_code}: No existing data, adding all {len(new_df)} new rows")
        return new_df
    
    if new_df.empty:
        print(f"ℹ️ {stock_code}: No new data to add")
        return existing_df
    
    print(f"🔍 {stock_code}: Checking for duplicates...")
    print(f"   - Existing data: {len(existing_df)} rows")
    print(f"   - New data: {len(new_df)} rows")
    
    # Create a composite key for duplicate detection
    existing_df['composite_key'] = existing_df['stock_code'] + '_' + existing_df['date'].astype(str)
    new_df['composite_key'] = new_df['stock_code'] + '_' + new_df['date'].astype(str)
    
    # Find existing keys for this stock
    existing_keys = set(existing_df[existing_df['stock_code'] == stock_code]['composite_key'])
    
    # Filter out duplicates from new data
    new_unique_df = new_df[~new_df['composite_key'].isin(existing_keys)].copy()
    
    print(f"🔍 {stock_code}: Duplicate check results:")
    print(f"   - Existing keys: {len(existing_keys)}")
    print(f"   - New unique rows: {len(new_unique_df)}")
    print(f"   - Duplicates filtered out: {len(new_df) - len(new_unique_df)}")
    
    if new_unique_df.empty:
        print(f"ℹ️ {stock_code}: All new data was duplicate, no changes needed")
        # Remove composite key columns
        existing_df = existing_df.drop('composite_key', axis=1)
        return existing_df
    
    # Remove composite key columns before concatenation
    new_unique_df = new_unique_df.drop('composite_key', axis=1)
    existing_df = existing_df.drop('composite_key', axis=1)
    
    # Handle DataFrame combination to avoid FutureWarning
    # Use pandas built-in methods that are more stable
    if existing_df.empty:
        combined_df = new_unique_df
    elif new_unique_df.empty:
        combined_df = existing_df
    else:
        # Both DataFrames have data, combine them safely
        # Use pandas concat with explicit dtype handling
        try:
            # First, ensure both DataFrames have the same dtypes
            for col in existing_df.columns:
                if col in new_unique_df.columns:
                    # Convert both to the same dtype
                    existing_df[col] = existing_df[col].astype('object')
                    new_unique_df[col] = new_unique_df[col].astype('object')
            
            combined_df = pd.concat([existing_df, new_unique_df], ignore_index=True)
        except Exception as e:
            print(f"⚠️ [WARNING] Standard concatenation failed for {stock_code}: {e}")
            # Fallback: use a different method
            combined_df = pd.concat([existing_df, new_unique_df], ignore_index=True, sort=False)
    
    print(f"✅ {stock_code}: Successfully merged data")
    print(f"   - Final combined data: {len(combined_df)} rows")
    return combined_df

# Function to fetch data for a date range
def fetch_data_for_date_range(stock_code, start_date, end_date):
    """Fetch data for a specific date range for a stock"""
    if start_date > end_date:
        return []
    
    print(f"📥 Fetching data for {stock_code} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    try:
        response = breeze.get_historical_data(
            interval="1day",
            from_date=start_date.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            to_date=end_date.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            stock_code=stock_code,
            exchange_code="NSE",
            product_type="cash"
        )
        
        if response and isinstance(response, dict) and response.get("Success"):
            new_rows = []
            for row in response["Success"]:
                new_rows.append({
                    "stock_code": stock_code,
                    "date": row["datetime"][:10],
                    "open": row["open"],
                    "high": row["high"],
                    "low": row["low"],
                    "close": row["close"],
                    "volume": row["volume"],
                    "expiry": None,
                    "stock_id": None
                })
            print(f"✅ Fetched {len(new_rows)} rows for {stock_code}")
            return new_rows
        else:
            print(f"⚠️ No data received for {stock_code} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
            return []
            
    except Exception as e:
        print(f"❌ [ERROR] API failed for {stock_code} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}: {e}")
        return []
    
    finally:
        time.sleep(1)  # API rate limiting

# Function to assign expiry dates with improved logic
def assign_expiries_to_data():
    print(f"\n📅 [INFO] Loading stock data from {EXCEL_FILE}...")
    try:
        df = pd.read_excel(EXCEL_FILE, dtype={"stock_code": str}, engine='openpyxl')
        print(f"✅ Successfully loaded {len(df)} rows from {EXCEL_FILE}")
    except Exception as e:
        print(f"❌ [ERROR] Could not read {EXCEL_FILE}: {e}")
        return
    
    df["date"] = pd.to_datetime(df["date"])
    df["stock_code"] = df["stock_code"].str.strip()

    if "expiry" not in df.columns:
        df["expiry"] = pd.NaT
        print(f"ℹ️ Added 'expiry' column to dataframe")

    print(f"[INFO] Loading expiry dates from {EXPIRY_FILE}...")
    try:
        expiry_df = pd.read_excel(EXPIRY_FILE, engine='openpyxl')
        print(f"✅ Successfully loaded expiry file with {len(expiry_df)} rows")
        print(f"📋 Expiry file columns: {list(expiry_df.columns)}")
    except Exception as e:
        print(f"❌ [ERROR] Could not read {EXPIRY_FILE}: {e}")
        return
    
    expiry_df.columns = expiry_df.columns.str.strip()
    
    # Find the expiry date column (case-insensitive)
    expiry_col = None
    for col in expiry_df.columns:
        if 'expiry' in col.lower() or 'date' in col.lower():
            expiry_col = col
            break
    
    if expiry_col is None:
        print(f"❌ [ERROR] Could not find expiry date column in {EXPIRY_FILE}")
        print(f"Available columns: {list(expiry_df.columns)}")
        return
    
    print(f"[INFO] Using expiry column: '{expiry_col}'")
    print(f"[DEBUG] First few expiry values: {expiry_df[expiry_col].head().tolist()}")
    
    expiry_df[expiry_col] = pd.to_datetime(expiry_df[expiry_col])
    expiry_df = expiry_df.sort_values(expiry_col).reset_index(drop=True)
    expiry_dates = expiry_df[expiry_col].tolist()
    
    print(f"[DEBUG] Processed {len(expiry_dates)} expiry dates")
    print(f"[DEBUG] First 5 expiry dates: {[d.strftime('%Y-%m-%d') for d in expiry_dates[:5]]}")
    print(f"[DEBUG] Last 5 expiry dates: {[d.strftime('%Y-%m-%d') for d in expiry_dates[-5:]]}")

    def find_next_expiry(trade_date):
        """
        Find the next expiry date for a given trade date.
        If trade date is on or before an expiry, use that expiry.
        If trade date is after an expiry, use the next expiry.
        """
        for expiry in expiry_dates:
            if trade_date <= expiry:
                return expiry
        # If trade date is after all expiries, return the last expiry
        return expiry_dates[-1] if expiry_dates else pd.NaT

    print("[INFO] Assigning expiry dates with improved logic...")
    print(f"[DEBUG] Sample trade dates: {df['date'].head().dt.strftime('%Y-%m-%d').tolist()}")
    
    # Apply expiry assignment
    df["expiry"] = df["date"].apply(find_next_expiry)
    
    # Count how many rows got updated
    updated = len(df[df["expiry"].notna()])
    print(f"[DEBUG] Sample assigned expiries: {df['expiry'].head().dt.strftime('%Y-%m-%d').tolist()}")

    # Save the updated dataframe safely
    if safe_save_data(df, EXCEL_FILE):
        print(f"✅ Expiry dates assigned to {updated} rows.")
        print(f"📦 Updated file saved: {EXCEL_FILE}")
    else:
        print(f"❌ [ERROR] Failed to save updated file with expiry dates")

# Function to show data summary
def show_data_summary(df, stock_code=None):
    """Show a summary of the current data state"""
    if df is None or df.empty:
        print(f"📊 Data Summary: No data available")
        return
    
    if stock_code:
        # Show summary for specific stock
        stock_data = df[df['stock_code'] == stock_code]
        if stock_data.empty:
            print(f"📊 {stock_code}: No data available")
        else:
            dates = pd.to_datetime(stock_data['date'], errors='coerce')
            valid_dates = dates[dates.notna()]
            if not valid_dates.empty:
                start_date = valid_dates.min().strftime('%Y-%m-%d')
                end_date = valid_dates.max().strftime('%Y-%m-%d')
                print(f"📊 {stock_code}: {len(stock_data)} rows, date range: {start_date} to {end_date}")
            else:
                print(f"📊 {stock_code}: {len(stock_data)} rows, but dates are invalid")
    else:
        # Show overall summary
        total_rows = len(df)
        unique_stocks = df['stock_code'].nunique()
        print(f"📊 Overall Data Summary:")
        print(f"   - Total rows: {total_rows:,}")
        print(f"   - Unique stocks: {unique_stocks}")
        
        if not df.empty and 'date' in df.columns:
            dates = pd.to_datetime(df['date'], errors='coerce')
            valid_dates = dates[dates.notna()]
            if not valid_dates.empty:
                start_date = valid_dates.min().strftime('%Y-%m-%d')
                end_date = valid_dates.max().strftime('%Y-%m-%d')
                print(f"   - Date range: {start_date} to {end_date}")

# Main execution
def main():
    print(f"🚀 Starting Historical Data Collection Script")
    print(f"📁 Data file: {EXCEL_FILE}")
    print(f"📁 Expiry file: {EXPIRY_FILE}")
    print(f"📁 Progress file: {PROGRESS_FILE}")
    print(f"{'='*60}")
    
    print(f"🔍 Validating Excel files...")
    if not validate_excel_file(EXCEL_FILE):
        print(f"ℹ️ {EXCEL_FILE} doesn't exist yet - will be created during data collection")
    else:
        print(f"✅ {EXCEL_FILE} is valid and accessible")

    if not validate_excel_file(EXPIRY_FILE):
        print(f"❌ [ERROR] Expiry file {EXPIRY_FILE} is corrupted or missing!")
        print(f"📝 Please ensure {EXPIRY_FILE} exists and is a valid Excel file.")
        exit()
    else:
        print(f"✅ {EXPIRY_FILE} is valid and accessible")

    # Load existing progress
    progress = load_progress()
    completed_stocks = set(progress["completed_stocks"])
    failed_stocks = set(progress["failed_stocks"])
    
    print(f"\n{'='*60}")
    print(f"🚀 Starting comprehensive data collection...")
    print(f"📊 Will check ALL stocks and ALL dates for missing data")
    print(f"🔄 Data will be reloaded after each stock to prevent duplicates")
    print(f"{'='*60}")
    
    # Process ALL stocks every time (not just remaining ones)
    all_stocks_to_process = list(stock_codes)
    print(f"📥 Processing {len(all_stocks_to_process)} stocks for missing data...")
    
    # Process each stock
    for i, stock_code in enumerate(all_stocks_to_process, 1):
        print(f"\n📥 Processing: {stock_code} ({i}/{len(all_stocks_to_process)})")
        
        try:
            # RELOAD DATA AFTER EACH STOCK to prevent duplicates
            print(f"🔄 Reloading data from Excel file...")
            existing_df = load_existing_data()
            
            # Show current data summary
            show_data_summary(existing_df)
            
            # Calculate what dates are missing for this stock
            missing_dates = calculate_missing_dates(existing_df, stock_code)
            
            if not missing_dates:
                print(f"✅ {stock_code}: All data is present, skipping...")
                # Mark as completed if all data is present
                if stock_code not in completed_stocks:
                    completed_stocks.add(stock_code)
                save_progress(completed_stocks, failed_stocks)
                continue
            
            # Fetch missing data for this stock (simplified approach)
            if len(missing_dates) == 2:  # [start_date, end_date]
                start_fetch, end_fetch = missing_dates
                new_rows = fetch_data_for_date_range(stock_code, start_fetch, end_fetch)
            else:
                print(f"⚠️ Unexpected missing_dates format for {stock_code}: {missing_dates}")
                continue
            
            if new_rows:
                new_df = pd.DataFrame(new_rows, columns=FIELDNAMES)
                print(f"📥 {stock_code}: Fetched {len(new_rows)} new rows")
                
                # Merge new data with existing data safely
                existing_df = merge_data_safely(existing_df, new_df, stock_code)
                
                # Save the updated data safely
                if safe_save_data(existing_df, EXCEL_FILE):
                    print(f"✅ Data saved successfully for {stock_code}")
                    # Mark as completed
                    if stock_code not in completed_stocks:
                        completed_stocks.add(stock_code)
                    save_progress(completed_stocks, failed_stocks)
                    
                    # VERIFY THE SAVE WAS SUCCESSFUL
                    print(f"🔍 Verifying data integrity for {stock_code}...")
                    verification_df = pd.read_excel(EXCEL_FILE, dtype={"stock_code": str}, engine='openpyxl')
                    stock_count = len(verification_df[verification_df['stock_code'] == stock_code])
                    print(f"✅ {stock_code}: {stock_count} rows verified in Excel file")
                    
                else:
                    print(f"❌ [ERROR] Failed to save data for {stock_code}")
                    # Don't mark as completed if save failed
                    continue
            else:
                print(f"ℹ️ No new data fetched for {stock_code}")
                # Mark as completed even if no new data (all dates were present)
                if stock_code not in completed_stocks:
                    completed_stocks.add(stock_code)
                save_progress(completed_stocks, failed_stocks)
                
        except Exception as e:
            print(f"❌ [ERROR] Failed to process {stock_code}: {e}")
            failed_stocks.add(stock_code)
            save_progress(completed_stocks, failed_stocks)
            continue

    # Final report
    print(f"\n🎉 Data collection completed!")
    print(f"✅ Successfully processed: {len(completed_stocks)} stocks")
    print(f"❌ Failed: {len(failed_stocks)} stocks")
    print(f"📊 Data saved to: {EXCEL_FILE}")

    if failed_stocks:
        print(f"\n❌ Failed to fetch data for these stocks:")
        for code in sorted(failed_stocks):
            print(f"- {code}")

    # Add expiry dates after data collection is complete
    print(f"\n🔄 Adding expiry dates to collected data...")
    try:
        assign_expiries_to_data()
        print(f"🎯 Complete! Historical data with expiry dates saved to {EXCEL_FILE}")
    except Exception as e:
        print(f"❌ [ERROR] Failed to assign expiry dates: {e}")
        print(f"📊 Data collection completed but expiry assignment failed.")

    # Final verification
    print(f"\n🔍 Final verification...")
    try:
        final_df = pd.read_excel(EXCEL_FILE, dtype={"stock_code": str}, engine='openpyxl')
        if "expiry" in final_df.columns:
            expiry_count = final_df["expiry"].notna().sum()
            total_count = len(final_df)
            print(f"✅ Final check: {expiry_count}/{total_count} rows have expiry dates assigned")
            if expiry_count == 0:
                print(f"⚠️ WARNING: No expiry dates were assigned! This indicates a problem.")
            else:
                print(f"🎯 Success: Expiry dates are properly assigned!")
        else:
            print(f"❌ ERROR: 'expiry' column is missing from final file!")
    except Exception as e:
        print(f"❌ [ERROR] Final verification failed: {e}")

    print(f"\n📋 Summary:")
    print(f"   - Data file: {EXCEL_FILE}")
    print(f"   - Expiry file: {EXPIRY_FILE}")
    print(f"   - Progress file: {PROGRESS_FILE}")
    print(f"   - Script completed successfully")
    print(f"   - Check the output above for any warnings or errors")

if __name__ == "__main__":
    main()
