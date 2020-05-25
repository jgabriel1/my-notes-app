import React from 'react';

import LoginForm from './components/LoginForm'
import CreateNoteForm from './components/CreateNoteForm'
import NotesList from './components/NotesList'

const App = () => {
  return (
    <div className="App">
      <LoginForm />
      <CreateNoteForm />
      <NotesList />
    </div>
  );
}

export default App;
