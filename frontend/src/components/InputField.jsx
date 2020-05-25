import React from 'react'

const InputField = ({ state, stateSetter, labelText, textArea }) => {

    const regularInputField = <input
        type="text"
        value={state}
        onChange={event => stateSetter(event.target.value)}
        className="inputField"
    />

    const textAreaField = <textarea
        type="text"
        value={state}
        onChange={event => stateSetter(event.target.value)}
        className="inputField"
    />

    return (
        <div className="fieldContainer">
            <label>
                {labelText}
                {textArea ? textAreaField : regularInputField}
            </label>
        </div>
    )
}

export default InputField
