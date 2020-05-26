import React from 'react'

import { BrowserRouter, Route, Switch } from 'react-router-dom'

import Logon from './pages/Logon'
import Register from './pages/Register'
import Notes from './pages/Notes'
import CreateNote from './pages/CreateNote'

const Routes = () => {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Logon} />
                <Route path="/register" component={Register} />
                <Route path="/notes" component={Notes} />
                <Route path="/create" component={CreateNote} />
            </Switch>
        </BrowserRouter>
    )
}

export default Routes