import React from 'react'

import api from '../services/api'
import { setToken } from '../utils/tokenHandler'

import '../styles/LoginForm.css'

const LoginForm = (props) => {

    const handleSubmit = async (event) => {
        event.preventDefault()

        const data = new FormData(event.target)
        const headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

        try {
            const response = await api.post('login/token', data, { headers: headers })

            const token = await response.data.access_token
            setToken(token)
        } catch (error) {
            console.log(error)
        }

    }

    return (
        <div className="loginFormContainer">
            <form onSubmit={handleSubmit}>
                <div id="usernameContainer">
                    <label htmlFor="usernameInput">Username:</label>
                    <input type="text" name="username" id="usernameInput" required />
                </div>

                <div id="passwordContainer">
                    <label htmlFor="passwordInput">Password:</label>
                    <input type="password" name="password" id="passwordInput" required />
                </div>

                <button>Submit</button>
            </form>
        </div>
    )
}

export default LoginForm