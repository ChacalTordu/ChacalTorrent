// userModel.js

const mongoose = require('mongoose');

// Define user schema
const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true
  },
  password: {
    type: String,
    required: true
  },
  email: String,
  // Define other user properties as needed
});

// Create and export User model
const User = mongoose.model('User', userSchema);
module.exports = User;
