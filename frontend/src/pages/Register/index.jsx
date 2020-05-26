import React from 'react'
import { useHistory } from 'react-router-dom'

import api from '../../services/api'

const Register = () => {

    const history = useHistory()

    const handleSubmit = event => {
        event.preventDefault()

        const { username, password } = event.target
        const userData = {
            username: username.value,
            password: password.value
        }

        const headers = { 'Content-Type': 'application/json' }

        api.post('login/register', userData, { headers: headers })
            .then(response => {
                if (response.status === 200) {
                    throw Error('Username already taken.')
                } 
                history.push('/')
            })
            .catch(error => {
                console.log(error)
            })
    }

    return (
        <div className="registerContainer">
            <form onSubmit={handleSubmit}>
                <div id="usernameContainer">
                    <label htmlFor="usernameInput">Username:</label>
                    <input type="text" name="username" id="usernameInput" required />
                </div>

                <div id="passwordContainer">
                    <label htmlFor="passwordInput">Password:</label>
                    <input type="password" name="password" id="passwordInput" required />
                </div>

                <button>Register</button>
            </form>
        </div>
    )
}

export default Register
