import { createClient, print } from 'redis';


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

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(error, output) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(output);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
