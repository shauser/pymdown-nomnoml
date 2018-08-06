const path = require('path');

module.exports = {
  target: 'node',
  entry: './nomnoml.js',
  output: {
    path: path.resolve(__dirname),
    filename: 'pymdown_nomnoml.js'
  }
};
