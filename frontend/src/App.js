import React from 'react';

import LoginForm from './components/LoginForm'
import CreateNoteForm from './components/CreateNoteForm'
import NoteElement from './components/NoteElement'

const App = () => {
  return (
    <div className="App">
      <LoginForm />
      <CreateNoteForm />
      <NoteElement
        category="Test Category"
        subject="Test Subject"
        body="This is the test body. It is a little bit longer than the other two."
      />
    </div>
  );
}

export default App;
