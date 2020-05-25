import React, { useState } from 'react'

import EditableField from './EditableField'

const NoteElement = ({ category, subject, body }) => {
    const [currentCategory, setCategory] = useState(category)
    const [currentSubject, setSubject] = useState(subject)
    const [currentBody, setBody] = useState(body)

    const [editMode, setEditMode] = useState(false)

    const sendEdited = async () => {
        /* Handle api connection */
        console.log(currentCategory)
        console.log(currentSubject)
        console.log(currentBody)
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
            />

            <EditableField
                isEditable={editMode}
                labelText="Subject: "
                state={currentSubject}
                stateSetter={setSubject}
            />

            <EditableField
                isEditable={editMode}
                labelText="Body: "
                state={currentBody}
                stateSetter={setBody}
            />

            {editButtons(editMode)}
        </div>
    )
}

export default NoteElement
