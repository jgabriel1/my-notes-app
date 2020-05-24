import React from 'react'
import api from '../services/api'

const LoginForm = props => {

    const handleSubmit = async (event) => {
        event.preventDefault()

        const formData = new FormData(event.target) // not grabbing info

        console.log(formData)

        api.post('login/token', { data: formData })
            .then(response => console.log(response.body)) // problem with CORS

    }

    return (
        <div className="loginFormContainer">
            <form onSubmit={handleSubmit}>
                <label>Username:
                <input type="text" name="username" id="username" required />
                </label>

                <label>Password:
                <input type="password" name="password" id="password" required />
                </label>

                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default LoginForm