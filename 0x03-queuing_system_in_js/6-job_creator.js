import kue from 'kue';

const queue = kue.createQueue();

const object = {
  phoneNumber: '0673967061',
  message: 'verification',
}

const job = queue.create('push_notification_code', object).save(function(err) {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('completed', function() {
  console.log('Notification job completed');
}).on('failed', function() {
  console.log('Notification job failed');
});
