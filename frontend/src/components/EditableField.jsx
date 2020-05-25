import React from 'react'

import InputField from './InputField'

const EditableField = ({ state, stateSetter, labelText, isEditable, textArea }) => {
    /*
    This component should change from a simple text display
    to an editable field by clicking on the edit button.

    The initial state should be the text display, and it should
    recieve, from parent component, the following:
    * label name;
    * value to be displayed;
    * state;
    * state setter;
    * current type (field or display)

    */

    const displayBlock = <label>
        {labelText}
        <p className="noteDisplayValue">{state}</p>
    </label>
    
    const editableBlock = <InputField
        state={state}
        stateSetter={stateSetter}
        labelText={labelText}
        textArea={textArea}
    />

    const currentElement = isEditable ? editableBlock : displayBlock

    return (
        <div className="noteProperty">
            {currentElement}
        </div>
    )
}

export default EditableField
