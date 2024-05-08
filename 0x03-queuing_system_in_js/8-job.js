import { createQueue } from 'kue';

const queue = createQueue();

export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('createPushNotificationsJobs');
  }

  jobs.forEach((data) => {
    const job = queue.create('push_notification_code_3', data)
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('complete', function() {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', function(error) {
      console.log(`Notification job ${job.id} failed: ${error}`);
    }).on('progress', function(progress, data) {
      console.lg(`Notification job {job.id} {progress}% complete`);
    });
  });
}
