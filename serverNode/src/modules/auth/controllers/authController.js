const authService = require('../service/authService');

// Controller for handling authentication-related operations
const authController = {
  async login(req, res) {
    try {
      const { username, password } = req.body;
      const token = await authService.login(username, password);
      res.json({ token });
    } catch (error) {
      console.error('Error during login:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  },

  async logout(req, res) {
    // Implement logout functionality if needed
  }
};

module.exports = authController;
