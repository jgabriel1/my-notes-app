import React, { useState } from 'react'

import api from '../services/api'

import FieldInput from './FieldInput'

const CreateNoteForm = (props) => {
    const [category, setCategory] = useState('')
    const [subject, setSubject] = useState('')
    const [body, setBody] = useState('')

    const createNote = async (event) => {
        event.preventDefault()

        const token = sessionStorage.getItem('token')
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
            <FieldInput
                name="category"
                state={category}
                stateSetter={setCategory}
                labelText="Category: "
            />

            <FieldInput
                name="subject"
                state={subject}
                stateSetter={setSubject}
                labelText="Subject: "
            />

            <FieldInput
                name="body"
                state={body}
                stateSetter={setBody}
                labelText="Body: "
            />

            <button onClick={createNote}>Create</button>
        </div>
    )
}

export default CreateNoteForm
