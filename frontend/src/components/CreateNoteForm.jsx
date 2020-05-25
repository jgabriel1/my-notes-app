import React, { useState } from 'react'

import InputField from './InputField'

import api from '../services/api'
import { getToken } from '../utils/tokenHandler'

const CreateNoteForm = (props) => {
    const [category, setCategory] = useState('')
    const [subject, setSubject] = useState('')
    const [body, setBody] = useState('')

    const createNote = async (event) => {
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

        try {
            const response = await api.post('/notes', noteData, { headers: headers })

            const id = await response.data.id
            console.log(id)
        } catch (error) {
            console.log(error)
        }
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
        </div>
    )
}

export default CreateNoteForm
