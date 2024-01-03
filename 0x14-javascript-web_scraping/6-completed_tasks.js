#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasksData = JSON.parse(body);
    const completedTasksByUser = tasksData.reduce((acc, task) => {
      if (task.completed) {
        acc[task.UserId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(completedTasksByUser);
  }
});
