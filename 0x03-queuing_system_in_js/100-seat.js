import express from 'express';
import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

const asyncget = promisify(client.get).bind(client);

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await asyncget('available_seats');
  return seats;
}

let reservationEnabled = true;

const queue = createQueue();

const app = express();

app.get('/available_seats', async function(req, res) {
  const seatAvailable = await getCurrentAvailableSeats();
  res.json({"numberOfAvailableSeats": seatAvailable});
});

app.get('/reserve_seat', async function(req, res) {
  if (!reservationEnabled) {
    res.json({ "status": "Reservation are blocked" });
  }
  const job = await queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ "status": "Reservation failed" });
    } else {
      res.json({ "status": "Reservation in process" });
      job.on('complete', function() {
        console.log(`Seat reservation job ${job.id} completed`);
      }).on('failed', function(message) {
        console.log(`Seat reservation job ${job.id} failed: ${message}`);
      });
    }
  });
});

app.get('/process', async function(req, res) {
  res.json({ "status": "Queue processing" });
  queue.process('reserve_seat', async function(job, done) {
    const seats = Number(await getCurrentAvailableSeats());
    if (seats == 0) {
      reservationEnabled = false;
      done(Error('No seat availabe'));
    } else {
      reserveSeat(seats - 1);
      done();
    }
  });
});

app.listen(1245, () => {
  console.log("Server is runing...");
});

reserveSeat(50);
