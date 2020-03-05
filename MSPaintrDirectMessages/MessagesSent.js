import React from 'react'
import Message from './Message'

const FAKE_MESSAGE = [
    {
        username: 'Helen',
        contents: 'Hello World!'
    }

]
class MessagesSent extends React.Component {

    render() {
        return ( 
            <div className="messages-sent"> 
                {FAKE_MESSAGE.map((message, index) => {
                    return ( <div key = {index} className = "message">
                        <div className ="message-username">{message.username} </div>
                        <div className ="message-contents">{message.contents} </div>
                        </div>
                        )
                })}
            </div>
        )
    }
}