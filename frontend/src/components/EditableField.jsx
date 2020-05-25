import React from 'react'

const EditableField = ({ isEditable, labelText, state, stateSetter }) => {
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

    const displayBlock = <p className="noteDisplayValue">{state}</p>
    const editableBlock = <input
        type="text"
        className="noteEditValue"
        value={state}
        onChange={event => stateSetter(event.target.value)}
    />

    const currentElement = isEditable ? editableBlock : displayBlock

    return (
        <div className="noteProperty">
            <label> {labelText}
                {currentElement}
            </label>
        </div>
    )
}

export default EditableField
