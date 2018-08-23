import React, {Component} from 'react';
import "wired-elements"
import './App.css';
// import {WiredCard} from "wired-card"


const buttonStyles = {
    background: "lightblue",
    margin: '0 10px'
};
const headerStyles = {
    width: '100%',
    height: '100px'
};


class App extends Component {
    render() {
        return (
            <div className="App">
                <wired-card elevation="1" style={headerStyles}>
                </wired-card>

                <wired-card elevation="1" style={{width: '800px', height: '700px'}}>
                    <div>

                    </div>
                </wired-card>
            </div>
        );
    }
}

export default App;