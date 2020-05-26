import React, { useState } from 'react'

import EditableField from './EditableField'

import api from '../services/api'
import { getToken } from '../utils/tokenHandler'

const NoteElement = ({ noteId, category, subject, body }) => {

    const [currentCategory, setCategory] = useState(category)
    const [currentSubject, setSubject] = useState(subject)
    const [currentBody, setBody] = useState(body)

    const [editMode, setEditMode] = useState(false)

    const sendEdited = () => {
        const token = getToken()

        const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }

        const noteData = {
            category: currentCategory,
            subject: currentSubject,
            body: currentBody
        }

        api.put(`notes/${noteId}`, noteData, { headers: headers })
            .then(response => {
                setEditMode(false)
            })
            .catch(error => console.log(error))
    }

    const editButtons = editing => {
        const confirmOrCancelBtn = (
            <div id="editButtons">
                <button type="button" onClick={sendEdited}>Confirm</button>
                <button type="button" onClick={() => setEditMode(false)}>Cancel</button>
            </div>
        )

        const editBtn = (
            <div id="editButtons">
                <button type="button" onClick={() => setEditMode(true)}>Edit</button>
            </div>
        )

        return editing ? confirmOrCancelBtn : editBtn
    }

    return (
        <div className="noteContainer">
            <EditableField
                isEditable={editMode}
                labelText="Category: "
                state={currentCategory}
                stateSetter={setCategory}
                textArea={false}
            />

            <EditableField
                isEditable={editMode}
                labelText="Subject: "
                state={currentSubject}
                stateSetter={setSubject}
                textArea={false}
            />

            <EditableField
                isEditable={editMode}
                labelText="Body: "
                state={currentBody}
                stateSetter={setBody}
                textArea={true}
            />

            {editButtons(editMode)}
        </div>
    )
}

export default NoteElement
