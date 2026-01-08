import yfinance as yf

class FinanceTool:
    def stock_record_finder(self, stock, time):
        dat = yf.Ticker(stock)

        history = dat.history(period=time)
        history = history.reset_index()

        if 'Date' in history.columns:
            history['Date'] = history['Date'].dt.strftime('%Y-%m-%d')

        return history.to_string(index=False)

