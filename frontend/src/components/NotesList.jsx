import React, { useState, useEffect } from 'react'

import NoteElement from './NoteElement'

import api from '../services/api'
import { getToken } from '../utils/tokenHandler'

const NotesList = props => {
    const [notesList, setNotesList] = useState([])

    const token = getToken()

    useEffect(() => {
        api.get('notes', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        }).then(response => {
            setNotesList(response.data.notes)
        })
    }, [token])

    return (
        <div className="notesListContainer">
            <ul>
                {notesList.map(note => (
                    <li key={note.id}>
                        <NoteElement
                            noteId={note.id}
                            category={note.category}
                            subject={note.subject}
                            body={note.body}
                        />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default NotesList
