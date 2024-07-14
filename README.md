# Chatbot API Integration Documentation

## Overview

This document provides detailed instructions for integrating the chatbot API with a React Native application. The API is hosted on AWS Elastic Beanstalk and exposes a single endpoint for interacting with the chatbot.

## API Endpoint

**Base URL:**
http://chatbot-env.eba-umqwe8hv.eu-north-1.elasticbeanstalk.com

makefile
Copy code

**Endpoint:**
/chat

makefile
Copy code

**Method:**
POST

less
Copy code

## Request Details

### Request Headers

- `Content-Type`: `application/json`

### Request Body

The body of the POST request should be a JSON object with a single key `message` containing the user's input as a string.

#### Example Request Body

```json
{
  "message": "Hello"
}
Response Details
The API will respond with a JSON object containing a single key response which will hold the chatbot's reply as a string.

Example Response Body
json
Copy code
{
  "response": "Hi! How can I help you today?"
}
Error Handling
Common Errors
400 Bad Request: This error occurs if the message field is missing or empty.

Response Body:
json
Copy code
{
  "error": "No message provided"
}
500 Internal Server Error: This error occurs if there is an issue processing the request.

Response Body:
json
Copy code
{
  "error": "An error occurred while processing the request"
}
Integration Steps
Step 1: Install Axios
To make HTTP requests from the React Native app, you can use the Axios library. Install it using npm or yarn.

sh
Copy code
npm install axios
# or
yarn add axios
Step 2: Create an API Service
Create a file named ChatbotService.js to handle the API interactions.

javascript
Copy code
import axios from 'axios';

const BASE_URL = 'http://chatbot-env.eba-umqwe8hv.eu-north-1.elasticbeanstalk.com';

const ChatbotService = {
  sendMessage: async (message) => {
    try {
      const response = await axios.post(`${BASE_URL}/chat`, { message }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      return response.data.response;
    } catch (error) {
      console.error('Error sending message:', error.response ? error.response.data : error.message);
      throw error;
    }
  }
};

export default ChatbotService;
Step 3: Use the API in a Component
In your React Native component, import and use the ChatbotService to send messages and handle responses.

javascript
Copy code
import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import ChatbotService from './ChatbotService';

const ChatScreen = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSend = async () => {
    try {
      const botResponse = await ChatbotService.sendMessage(message);
      setResponse(botResponse);
    } catch (error) {
      setResponse('An error occurred while communicating with the chatbot.');
    }
  };

  return (
    <View>
      <Text>Chat with the Bot</Text>
      <TextInput
        value={message}
        onChangeText={setMessage}
        placeholder="Type your message"
      />
      <Button title="Send" onPress={handleSend} />
      <Text>Bot Response: {response}</Text>
    </View>
  );
};

export default ChatScreen;
Step 4: Handling Edge Cases
Ensure that the application handles edge cases, such as empty input and network errors, gracefully.

javascript
Copy code
const handleSend = async () => {
  if (!message.trim()) {
    setResponse('Please enter a message.');
    return;
  }

  try {
    const botResponse = await ChatbotService.sendMessage(message);
    setResponse(botResponse);
  } catch (error) {
    setResponse('An error occurred while communicating with the chatbot.');
  }
};
Full Example
Below is a complete example of a simple chat screen component in React Native using the chatbot API.

javascript
Copy code
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import ChatbotService from './ChatbotService';

const ChatScreen = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSend = async () => {
    if (!message.trim()) {
      setResponse('Please enter a message.');
      return;
    }

    try {
      const botResponse = await ChatbotService.sendMessage(message);
      setResponse(botResponse);
    } catch (error) {
      setResponse('An error occurred while communicating with the chatbot.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Chat with the Bot</Text>
      <TextInput
        style={styles.input}
        value={message}
        onChangeText={setMessage}
        placeholder="Type your message"
      />
      <Button title="Send" onPress={handleSend} />
      <Text style={styles.response}>Bot Response: {response}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 12,
    paddingHorizontal: 8,
  },
  response: {
    marginTop: 16,
    fontSize: 16,
    fontStyle: 'italic',
  },
});

export default ChatScreen;
Conclusion
This documentation provides all the necessary details to integrate the chatbot API with a React Native application. By following these steps, the front-end developer should be able to send messages to the chatbot and display its responses within the app. If there are any questions or additional requirements, please feel free to ask for further assistance.
