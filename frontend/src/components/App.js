import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

//create app extends component have to inherite constructor(props)
export default class App extends Component {
    constructor(props) {
        super(props);
    }

    //render in the page
    render() {
        return (<div className="center">
            <HomePage />
        </div>);
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);