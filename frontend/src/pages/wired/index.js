import React from 'react';
import {render} from 'react-dom';
import 'wired-elements';

const styles = {
	fontFamily: "sans-serif",
	padding: "10px"
};

const buttonStyles = {
	background: "lightblue",
	margin: '0 10px'
};

const App = () => (
	<div style={styles}>
		<wired-input placeholder="Enter name"></wired-input>
		<wired-button style={buttonStyles}>Submit</wired-button>
	</div>
);

export default App