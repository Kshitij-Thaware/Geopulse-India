import plotly.graph_objects as go


#GOLD CHART
def plot_gold_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = data['gold'].index,
            y = data['gold']['Close'],
            mode = 'lines+markers',
            name = 'Gold Prices'
        )
    )

    fig.update_layout(
        title = "Gold Price Movement",
        xaxis_title = "Date",
        yaxis_title = "Price"
    )

    return fig



#OIL CHART
def plot_oil_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = data['oil'].index,
            y = data['oil']['Close'],
            mode = 'lines+markers',
            name = 'Oil Prices'
        )
    )

    fig.update_layout(
        title = "Crude Oil Price Movement",
        xaxis_title = "Date",
        yaxis_title = "Price"
    )

    return fig


#USD/INR CHART
def plot_currency_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = data['usd_inr'].index,
            y = data['usd_inr']['Close'],
            mode = 'lines+markers',
            name = 'USD/INR'
        )
    )

    fig.update_layout(
        title = "USD/INR Movement",
        xaxis_title = "Date",
        yaxis_title = "Exchange Rate"
    )

    return fig


#NIFTY CHART

def plot_stock_chart(data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = data['nifty'].index,
            y = data['nifty']['Close'],
            mode = 'lines+markers',
            name = 'Nifty 50'  
        )
    )

    fig.update_layout(
        title = "Nifty 50 Movement",
        xaxis_title = "Date",
        yaxis_title = "Index Value"
    )

    return fig
