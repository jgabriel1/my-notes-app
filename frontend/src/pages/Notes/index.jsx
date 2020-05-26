import React, { useState, useEffect } from 'react'

import { Link } from 'react-router-dom'

import NoteElement from '../../components/NoteElement'

import api from '../../services/api'
import { getToken } from '../../utils/tokenHandler'

const Notes = props => {
    const [notesList, setNotesList] = useState([])

    const token = getToken()

    useEffect(() => {
        api.get('notes', { headers: { 'Authorization': `Bearer ${token}` } })
            .then(response => {
                setNotesList(response.data.notes)
            })
            .catch(error => console.log(error))
    }, [token])

    const handleDelete = id => {
        api.delete(`notes/${id}`, { headers: { 'Authorization': `Bearer ${token}` } })
            .then(response => {
                setNotesList(
                    notesList.filter(value => (value.id !== id))
                )
            })
            .catch(error => console.log(error))
    }

    return (
        <div className="notesListContainer">
            <Link to="/create">Create Note</Link>
            <ul>
                {notesList.map(note => (
                    <li key={note.id}>
                        <NoteElement
                            noteId={note.id}
                            category={note.category}
                            subject={note.subject}
                            body={note.body}
                        />
                        <button type="button" onClick={() => handleDelete(note.id)}>
                            Delete
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Notes
