import { createClient, print } from 'redis';
const { promisify } = require('util');

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', err => {
  console.log(`Redis client not connected to the server, ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
};

const getAsync = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
  const output = await getAsync(schoolName).catch((error) => {
    if (error) {
      throw error;
      console.log(error);
    }
  });
  console.log(output);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
