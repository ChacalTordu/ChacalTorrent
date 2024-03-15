const User = require('../models/userModel');
const jwt = require('jsonwebtoken');
const { secretKey } = require('../config'); // You should define your secret key in a separate config file

// Service for handling authentication-related operations
const authService = {
  async login(username, password) {
    // Implement authentication logic here (e.g., querying database, checking credentials)
    const user = await User.findOne({ username });
    if (!user || user.password !== password) {
      throw new Error('Invalid username or password');
    }

    // Generate and return JWT token
    const token = jwt.sign({ username: user.username }, secretKey, { expiresIn: '1h' });
    return token;
  }
};

module.exports = authService;
