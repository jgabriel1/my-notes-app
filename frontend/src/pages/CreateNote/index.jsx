import React, { useState } from 'react'
import { Link, useHistory } from 'react-router-dom'

import InputField from '../../components/InputField'

import api from '../../services/api'
import { getToken } from '../../utils/tokenHandler'

const CreateNote = props => {
    const [category, setCategory] = useState('')
    const [subject, setSubject] = useState('')
    const [body, setBody] = useState('')

    const history = useHistory()

    const createNote = event => {
        event.preventDefault()

        const token = getToken()
        const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }

        const noteData = {
            category: category,
            subject: subject,
            body: body
        }

        api.post('notes', noteData, { headers: headers })
            .then(response => {
                console.log(response.data.id)
                history.push('/notes')
            })
            .catch(error => console.log(error))
    }

    return (
        <div className="createNoteContainer">
            <InputField
                name="category"
                state={category}
                stateSetter={setCategory}
                labelText="Category: "
            />

            <InputField
                name="subject"
                state={subject}
                stateSetter={setSubject}
                labelText="Subject: "
            />

            <InputField
                name="body"
                state={body}
                stateSetter={setBody}
                labelText="Body: "
                textArea={true}
            />

            <button onClick={createNote}>Create</button>
            <Link to="/notes">Cancel</Link>
        </div>
    )
}

export default CreateNote
