import React from 'react'

import { BrowserRouter, Route, Switch } from 'react-router-dom'

import Logon from './pages/Logon'
import Register from './pages/Register'
import Notes from './pages/Notes'

const Routes = () => {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Logon} />
                <Route path="/register" component={Register} />
                <Route path="/notes" component={Notes} />
            </Switch>
        </BrowserRouter>
    )
}

export default Routes