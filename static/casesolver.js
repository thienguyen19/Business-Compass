const chatHeader = document.querySelector('.chat-header')
const chatMessages = document.querySelector('.chat-messages')
const chatInputForm = document.querySelector('.chat-input-form')
const chatInput = document.querySelector('.chat-input')
const clearChatBtn = document.querySelector('.clear-chat-button')


const messages =  []

async function generateAnswer(prompt) {
  const apiKey = '<API Key>'; // Replace with your OpenAI API key
  const endpoint = 'https://api.openai.com/v1/engines/text-davinci-003/completions';

  try {
      const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${apiKey}`,
          },
          body: JSON.stringify({
              prompt: prompt,
              max_tokens: 1000, 
              temperature: 0.5
          }),
      });

      const data = await response.json();
      const answer = data.choices[0].text;
      console.log(answer)
      return data.choices[0].text
  } catch (error) {
      return "Error in using OpenAI API"
  }
}



const createChatMessageElement = (message) => `
  <div class="message">
    <div class="message-sender ${message.sender === 'U' ? 'purple-bg' : 'blue-bg'}">${message.sender}</div>
    <div class="message-text">${message.text}</div>
    <div class="message-timestamp">${message.timestamp}</div>
  </div>
`

window.onload = () => {
  messages.forEach((message) => {
    chatMessages.innerHTML += createChatMessageElement(message)
  })
}

let messageSender = 'U'


const sendMessage = async (e) => {
  e.preventDefault()

  const timestamp = new Date().toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
  const message = {
    sender: messageSender,
    text: chatInput.value,
    timestamp,
  }
  
  /* Save message to local storage */
  messages.push(message)
  localStorage.setItem('messages', JSON.stringify(messages))

  /* Add message to DOM */
  chatMessages.innerHTML += createChatMessageElement(message)


  // const botText = await generateAnswer(chatInput.value);
  const botText = "OpenAI response ....";
  console.log("botText", botText );
  const message2 = {
    sender: 'BC',
    text: botText,
    timestamp,
  }

  /* Save message to local storage */
  messages.push(message2)
  localStorage.setItem('messages', JSON.stringify(message2))

  /* Add message to DOM */
  chatMessages.innerHTML += createChatMessageElement(message2)

  /* Clear input field */
  chatInputForm.reset()

  /*  Scroll to bottom of chat messages */
  chatMessages.scrollTop = chatMessages.scrollHeight
  
}

chatInputForm.addEventListener('submit', sendMessage)

clearChatBtn.addEventListener('click', () => {
  localStorage.clear()
  chatMessages.innerHTML = ''
})







// Handle send button click


