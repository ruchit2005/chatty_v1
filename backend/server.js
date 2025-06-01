const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.post('/chat', async (req, res) => {
  try {
    const { message } = req.body;

    const pythonResponse = await axios.post('https://chatty-backend-production-4b11.up.railway.app/', { message });



    res.json({ response: pythonResponse.data.response });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to get response from Python backend' });
  }
});

app.listen(PORT, () => {
  console.log(`Node.js server running on port ${PORT}`);
});
