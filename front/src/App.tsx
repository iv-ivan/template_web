import React from 'react'
import { hot } from 'react-hot-loader/root'
import { MyJSComponent } from './components/MyJSComponent'
import { Counter } from './components/Counter'
import {
    BrowserRouter as Router,
    Route,
    Switch,
    Redirect
} from "react-router-dom"

const Home = () => {
    return (
        <h1>Hello home</h1>
    );
}

const Appointments = () => {
    return (
        <h1>Appointments!</h1>
    );
}

export const App = hot(_App);

export function _App(): JSX.Element | null {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path='/home'>
                        <Home />
                    </Route>
                    <Route path='/appointments'>
                        <Appointments />
                    </Route>
                    <Redirect from='/' to='/home'/>
                  </Switch>
                <MyJSComponent />
                <Counter />
            </div>
        </Router>
    )
}
