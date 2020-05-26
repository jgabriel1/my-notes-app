import React from 'react'
import { Link, useHistory } from 'react-router-dom'

import api from '../../services/api'
import { setToken } from '../../utils/tokenHandler'

const Logon = () => {

    const history = useHistory()

    const handleSubmit = event => {
        event.preventDefault()

        const data = new FormData(event.target)
        const headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

        api.post('login/token', data, { headers: headers })
            .then(response => {
                const token = response.data.access_token
                setToken(token)
            })
            .then(() => {
                history.push('/notes')
            })
            .catch(error => {
                console.log(error) // for now
            })
    }

    return (
        <div className="logonContainer">
            <form onSubmit={handleSubmit}>
                <div id="usernameContainer">
                    <label htmlFor="usernameInput">Username:</label>
                    <input type="text" name="username" id="usernameInput" required />
                </div>

                <div id="passwordContainer">
                    <label htmlFor="passwordInput">Password:</label>
                    <input type="password" name="password" id="passwordInput" required />
                </div>

                <button>Login</button>
            </form>
            <Link to="/register">Register Now!</Link>
        </div>
    )
}

export default Logon
