const express = require('express');
const app = express();

app.get('/', (req, res) => {
  var now = new Date();
  var current_time = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
  console.log("Current Time:", current_time);

  res.send(<p id="current-time">Current Time: ${current_time}</p>);
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});