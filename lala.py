from breeze_connect import BreezeConnect
import json
import pandas as pd
from datetime import datetime
"""
Year	Month	Expiry Date
2010	Jan	01/28/2010"""

def get_option_chain_quotes_with_error_handling(stock_code, strike_price, exchange_code, expiry_date, product_type, right):
    """
    Get option chain quotes from Breeze API with comprehensive error handling and response logging.
    
    Args:
        stock_code (str): Stock code (e.g., "NIFTY", "BANKNIFTY")
        strike_price (float): Strike price for the option
        exchange_code (str): Exchange code (e.g., "NFO" for NSE F&O)
        expiry_date (str): Expiry date in format "YYYY-MM-DD"
        product_type (str): Product type (e.g., "options")
        right (str): Option right ("CE" for call, "PE" for put)
    
    Returns:
        dict: API response data if successful, None if failed
    """
    try:
        # Initialize Breeze connection
        breeze = BreezeConnect(api_key="+8~9U1#3651u0761y4D0648r19H~550q")
        
        # Generate session
        breeze.generate_session(
            api_secret="7H5063392n5553F573iL9MS834=I3715", 
            session_token="52556614"
        )
        
        print(f"Fetching option chain quotes for {stock_code} {strike_price} {right} expiring on {expiry_date}")
        
        # Make API call
        response = breeze.get_option_chain_quotes(
            stock_code=stock_code,
            strike_price=strike_price,
            exchange_code=exchange_code,
            expiry_date=expiry_date,
            product_type=product_type,
            right=right
        )
        
        # Print the complete raw API response for debugging
        print("=== COMPLETE API RESPONSE ===")
        print(json.dumps(response, indent=2, default=str))
        print("=== END API RESPONSE ===")
        
        # Check if response contains data
        if response and isinstance(response, dict):
            # Extract LTP if available
            if 'data' in response and response['data']:
                for item in response['data']:
                    if 'ltp' in item:
                        ltp = item['ltp']
                        print(f"LTP for {stock_code} {strike_price} {right}: {ltp}")
                        return response
                print("No LTP found in response data")
            else:
                print("No data found in response")
        else:
            print("Invalid response format")
            
        return response
        
    except Exception as e:
        print("=== API ERROR OCCURRED ===")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        print(f"Error Details: {repr(e)}")
        print("=== END ERROR ===")
        return None

def test_option_chain_api():
    """
    Test function to demonstrate usage of the option chain API
    """
    # Example parameters
    stock_code = "NIFTY"
    strike_price = 19000
    exchange_code = "NFO"
    expiry_date = "2024-04-25"
    product_type = "options"
    right = "CE"
    
    print("Testing Option Chain API...")
    result = get_option_chain_quotes_with_error_handling(
        stock_code=stock_code,
        strike_price=strike_price,
        exchange_code=exchange_code,
        expiry_date=expiry_date,
        product_type=product_type,
        right=right
    )
    
    if result:
        print("API call successful!")
    else:
        print("API call failed!")

def process_stocks_from_excel():
    """
    Read stocks from output.xlsx and get option chain quotes for each one
    """
    try:
        # Read the Excel file
        print("Reading output.xlsx file...")
        df = pd.read_excel('output.xlsx')
        
        print("Excel file contents:")
        print(df.head())
        print(f"\nTotal rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        
        # Process each stock row
        for index, row in df.iterrows():
            print(f"\n{'='*50}")
            print(f"Processing row {index + 1}: {row.to_dict()}")
            print(f"{'='*50}")
            
            try:
                # Extract parameters from the row
                # You may need to adjust these column names based on your Excel structure
                stock_code = row.get('stock_code', row.get('Stock', row.get('SYMBOL', 'NIFTY')))
                strike_price = row.get('strike_price', row.get('Strike', row.get('STRIKE', 19000)))
                exchange_code = row.get('exchange_code', row.get('Exchange', 'NFO'))
                expiry_date = row.get('expiry_date', row.get('Expiry', '2024-04-25'))
                product_type = row.get('product_type', row.get('Product', 'options'))
                right = row.get('right', row.get('Right', row.get('CE/PE', 'CE')))
                
                # Convert strike_price to float if it's not already
                if isinstance(strike_price, str):
                    try:
                        strike_price = float(strike_price)
                    except ValueError:
                        print(f"Invalid strike price: {strike_price}, skipping this row")
                        continue
                
                # Convert expiry_date to string if it's a datetime
                if isinstance(expiry_date, datetime):
                    expiry_date = expiry_date.strftime('%Y-%m-%d')
                elif isinstance(expiry_date, str):
                    # Keep as is
                    pass
                else:
                    print(f"Invalid expiry date: {expiry_date}, skipping this row")
                    continue
                
                print(f"Extracted parameters:")
                print(f"  Stock Code: {stock_code}")
                print(f"  Strike Price: {strike_price}")
                print(f"  Exchange: {exchange_code}")
                print(f"  Expiry Date: {expiry_date}")
                print(f"  Product Type: {product_type}")
                print(f"  Right: {right}")
                
                # Get option chain quotes for this stock
                result = get_option_chain_quotes_with_error_handling(
                    stock_code=stock_code,
                    strike_price=strike_price,
                    exchange_code=exchange_code,
                    expiry_date=expiry_date,
                    product_type=product_type,
                    right=right
                )
                
                if result:
                    print(f"✓ Successfully processed {stock_code} {strike_price} {right}")
                else:
                    print(f"✗ Failed to process {stock_code} {strike_price} {right}")
                
            except Exception as row_error:
                print(f"Error processing row {index + 1}: {str(row_error)}")
                continue
            
            # Add a small delay between API calls to avoid rate limiting
            import time
            time.sleep(1)
            
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")
        print("Make sure output.xlsx exists and is accessible")

if __name__ == "__main__":
    # Run the Excel processing function
    process_stocks_from_excel()
