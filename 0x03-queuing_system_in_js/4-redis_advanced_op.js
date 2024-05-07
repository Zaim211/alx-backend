import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

const KeyHash = "HolbertonSchools";

client.hset(KeyHash, 'Portland', 50, print);
client.hset(KeyHash, 'Seattle', 80, print);
client.hset(KeyHash, 'New York', 20, print);
client.hset(KeyHash, 'Bogota', 20, print);
client.hset(KeyHash, 'Cali', 40, print);
client.hset(KeyHash, 'Paris', 2, print);

client.hgetall(KeyHash, function(error, output) {
  if (error) {
    throw error;
    console.log(error);
  }
  console.log(output);
});
