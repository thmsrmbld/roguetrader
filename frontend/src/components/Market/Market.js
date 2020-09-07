import './Market.css'

import React from 'react';
import { Component } from 'react';


class Market extends Component {

  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      isPolling: true,
      pollSuccess: false,
      stocks: []
    };
  }

  // When this component mounts, it automatically polls for new information
  async componentDidMount() {
    // Set a schedule to use within the loop to get new data
    const fetchSchedule = (ms) => new Promise((r) => setTimeout(r, ms));
    // We need to actually set a switch for this to pause it if necessary
    while (this.state.isPolling) {

      fetch("http://localhost:8000/api/stocks/")
      .then(res => res.json())
      .then(
        (stockFetchResponse) => {
          this.setState({
            pollSuccess: true,
            stocks: stockFetchResponse
          });
          console.log(this.state.stocks)
        },
        // Handle errors here instead of a catch() block so that we don't
        // swallow exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
      await fetchSchedule(3500);
    }
  }

   render() {
    const { error, isPolling, stocks } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isPolling) {
      return <div>Loading...</div>;
    } else {

        return(
            <div className='market market-container'>
              <table className="market-table">
                 <thead>
                    <tr>
                      <th>Name</th>
                      <th>Code</th>
                      <th>Price</th>
                      <th>% Chg</th>
                      <th>Low</th>
                      <th>High</th>
                      <th>Sector</th>
                      <th>Susp.</th>
                      <th>Boom</th>
                      <th>Bust</th>
                    </tr>
                  </thead>

                  <tbody>
                    {stocks.map((stock) => (
                        <tr key={stock.id}>
                          <td>{ stock.name }</td>
                          <td>{ stock.symbol }</td>
                          <td>£{ stock.current_price }</td>
                          <td>{ stock.pct_change }</td>
                          <td>£{ stock.lowest_price }</td>
                          <td>£{ stock.highest_price }</td>
                          <td>{ stock.sector }</td>
                          <td>{ stock.suspended }</td>
                          <td>{ stock.booming }</td>
                          <td>{ stock.busting }</td>
                        </tr>
                    ))}
                  </tbody>

                </table>
            </div>
        )
    }
  }
}

export default Market