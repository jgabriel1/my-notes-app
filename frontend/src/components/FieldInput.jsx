import React from 'react'

const FieldInput = ({ name, state, stateSetter, labelText }) => {
    return (
        <div className="fieldContainer">
            <label htmlFor={name}>{labelText}</label>
            <input
                type="textarea"
                name={name}
                id={name}
                value={state}
                onChange={event => stateSetter(event.target.value)}
            />
        </div>
    )
}

export default FieldInput
