import React, { Component } from 'react';
import logo from '../img/logo.svg';
import '../css/App.css';

import Market from '../components/Market/Market'


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <Market/>
      </div>
    );
  }
}

export default App;
