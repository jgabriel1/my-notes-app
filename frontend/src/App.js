import React from 'react';

import LoginForm from './components/LoginForm'
import CreateNoteForm from './components/CreateNoteForm'

const App = () => {
  return (
    <div className="App">
      <LoginForm />
      <CreateNoteForm />
    </div>
  );
}

export default App;
