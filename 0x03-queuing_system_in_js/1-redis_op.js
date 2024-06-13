#!/usr/bin/node
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

let setNewSchool = function(schoolName, value) {
  client.SET(schoolName, value, print);
}

let displaySchoolValue = function(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
